from parser import Parser
from z3 import *

class PropParser(Parser):
    def start(self):
        return self.expression()

    def expression(self):
        rv = self.match('term')
        while True:
            op = self.maybe_keyword('→', '↔')
            if op is None:
                break

            term = self.match('term')
            if op == '→':
                rv = Implies(rv, term)
            else:
                rv = rv == term

    def term(self):
        rv = self.match('factor')
        while True:
            op = self.maybe_keyword('∧', '∨')
            if op is None:
                break
            term = self.match('factor')
            if op == '∧':
                rv = And(rv, term)
            else:
                rv = Or(rv, term)
        return rv
    
    def factor(self):
        if self.maybe_keyword('('):
            rv = self.match('expression')
            self.keyword(')')
            return rv
        elif self.maybe_keyword('¬'):
            rv = self.match('variable')
            rv = Not(rv)
            return rv
        return self.match('variable')

    def variable(self):
        chars = []
        chars.append(self.char('A-Za-z'))
        while True:
            char = self.maybe_char('A-Za-z')
            if char is None:
                break
            chars.append(char)
            rv = ''.join(chars)
            return rv