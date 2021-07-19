# insert root formula and operators to consider
# then abstract the formula
# then produce all permutations of the abstracted formula by changing operators
# can I use z3 for this by abstracting operators into unknown functions (like f represents and, or) then enumerate all models and reconstruct formula for each model?
from typing import Set
from z3 import *
from pythonds.basic import Stack
from pythonds.trees import BinaryTree
import operator
import string
import propParser

def main(f, operators):
    result = []

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        elif i in ['∧', '∨', '→', '↔']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif i == ')':
            currentTree = pStack.pop()

        elif i not in ['∧', '∨', '→', '↔']:
            try:
                currentTree.setRootVal(i)
                parent = pStack.pop()
                currentTree = parent

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))
    return eTree

def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def absTree(tree):
    if tree != None:
        absTree(tree.getLeftChild())
        absTree(tree.getRightChild())
        if tree.getRootVal() in ['∧', '∨']:
            tree.setRootVal('t1')
        elif tree.getRootVal() in ['→', '↔']:
            tree.setRootVal('t2')
            
# def abs(fpexp):
#     fplist = fpexp.split()
#     for index, value in enumerate(fplist):
#         if value == '∧' or value == '∨':
#             fplist[index] = 't1'
#         elif value == '→' or value == '↔':
#             fplist[index] = 't2'
#     print(' '.join(fplist))

def numConc(str):
    if str == 't1':
        return 2
    elif str == 't2':
        return 2
    else:
        return 1

def numOfConcretizations(abstractedTree):
    res = 1
    if abstractedTree != None:
        res *= numConc(abstractedTree.getRootVal())
    return res

var = string.ascii_lowercase
global idx 
idx = 0
def freshVariable():
    global idx
    res = var[idx]
    idx += 1
    return Int(res)

s = Solver()
def conc(abstractedTree, solver):
    if abstractedTree.getRootVal() == 't1' or  abstractedTree.getRootVal() == 't2':
        x = freshVariable()
        numConc = numOfConcretizations(abstractedTree)
        
        solver.add(0<=x, x<numConc)
        if abstractedTree != None:
            conc(abstractedTree.getLeftChild(), solver)
            conc(abstractedTree.getRightChild(), solver)

def getModels():
    result = []
    while s.check() == sat:
        m = s.model()
        result.append(m)
        # Create a new constraint the blocks the current model
        block = []
        for d in m:
            # d is a declaration
            if d.arity() > 0:
                raise Z3Exception("uninterpreted functions are not supported")
            # create a constant from declaration
            c = d()
            if is_array(c) or c.sort().kind() == Z3_UNINTERPRETED_SORT:
                raise Z3Exception("arrays and uninterpreted sorts are not supported")
            block.append(c != m[d])
        s.add(Or(block))
    return result

T1 = ['∨', '∧']
T2 = ['→', '↔']
global modelIdx
def getFormulas(listOfModels, abstractedTree):
    result = []
    print("what")
    print(listOfModels)
    for l in listOfModels:
        print("hi")
        print(l)
    #for i in range(len(var)):
        global modelIdx
        modelIdx = 0
        list = getFormula(l, abstractedTree)
        print("list: ")
        print(list)
        result.append(" ".join(list))
    return result

def getFormula(model, abstractedTree):  
    formula = []
    #i = 0
    global modelIdx
    x = var[modelIdx] #x = var[i]
    print("x: ")
    print(x)
    print("model: ")
    print(model[Int(x)])
    if abstractedTree != None:
        formula.extend(getFormula(model, abstractedTree.getLeftChild()))
        if abstractedTree.getRootVal() == 't1':
            idx = model[Int(var[modelIdx])].as_long() #model[i].index("= ") + len("= ")
            print("x and idx")
            print(var[modelIdx])
            print(idx)
            formula.append(T1[idx])
            modelIdx += 1 # i += 1
        elif abstractedTree.getRootVal() == 't2':
            idx = model[Int(var[modelIdx])].as_long() #model[i].index("= ") + len("= ")
            print(var[modelIdx])
            print(idx)
            formula.append(T2[idx])
            modelIdx += 1 # i += 1
        else:
            formula.append(abstractedTree.getRootVal())
        formula.extend(getFormula(model, abstractedTree.getRightChild()))
    return formula

def checkSat(z3_exp):
    # parser = propParser()
    solver = Solver()
    # z3_exp = parser.parse(str)
    solver.add(z3_exp)
    return solver.check()

def checkValid(z3_exp):
    solver = Solver()
    solver.add(Not(z3_exp))
    if s.check() == unsat:
        return 'valid'
    return 'invalid'

#     strList = str.split()
#     v1 = Bool('v1')
#     v2 = Bool('v2')
#     for s in strList:
#         if s == '∨':
#             v1 = Or(v1, v2)
#         elif s == '∧':
#             v1 = And(v1, v2)
#         elif s == '→'

#abs('(P ∨ P) ↔ P')

pt = buildParseTree("( ( P ∨ P ) ↔ P )")
#pt = buildParseTree("( ( ( P → P ) → P ) → P )") 
#pt = buildParseTree("( ( ( P → Q ) → P ) → ( x > 0 ) )") 
pt.postorder() 
absTree(pt)
pt.postorder()

conc(pt, s)
print(s)
print(s.check())
print(numOfConcretizations(pt))
#print(getModels())
print(getFormulas(getModels(), pt))
#print(getModels().sort())
# while s.check() == sat:
#   print(s.model())
  #s.add(Or(a != s.model()[a], b != s.model()[b])) # prevent next model from using the same assignment as a previous model
