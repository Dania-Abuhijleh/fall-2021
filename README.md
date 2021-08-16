# fall-2021

This program takes a propositional formula and returns a list of formulas similar to the original one by substituting the operations in all possible combinations. You must provide a list of lists of operators, the operators in the same list can be substituted for one another. For example if I provide [['∨', '∧'], ['→', '↔'], ['¬']] this means '∨' and '∧' are interchangable for each other but not for '¬'. Mathematical operators and integers are also supported.

Download Python

Download Git

Download z3:
```
git clone https://github.com/Z3Prover/z3.git
cd z3

python3 scripts/mk_make.py --python
cd build
make
sudo make install

pip3 install z3-solver
```
also do `pip3 install pythonds`

then download fall-2021 from this git repo

then run an example file like so:

Input a file with the formula on one line and the list of lists of operators on the next line.

Run main.exe by going into the dist directory and typing 'cmd /k main.exe' on a command line, then 

Invoke the command from your terminal with the file path: python main.py '/path/to/example.txt'
