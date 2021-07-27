# fall-2021

This program takes a propositional formula and returns a list of formulas similar to the original one by substituting the operations in all possible combinations. You must provide a list of lists of operators, the operators in the same list can be substituted for one another. For example if I provide [['∨', '∧'], ['→', '↔'], ['¬']] this means '∨' and '∧' are interchangable for each other but not for '¬'. Mathematical operators and integers are also supported.

Input a file with the formula on one line and the list of lists of operators on the next line.

Invoke the command from your terminal with the file path: python main.py '<filepath>'
