Which of the following apply to the formulas below: satisfiable, unsatisfiable, falsifiable, valid 
for valid formulas: Prove the following
hwk05
P ∨ P ↔ P
P ∨ Q → P ∨ Q
x → (y → z) ↔ x ∧ y → z 
(xor P Q) ↔ (xor Q P)
P ∧ (P ∨ Q) ↔ P
A ∧ (B ∨ C) ↔ (A ∧ B) ∨ (A ∧ C)

Create a text file with the formula (in smt-lib 2.0 format) and operators (in z3 format) to replace:
![image](https://user-images.githubusercontent.com/57302458/130230314-7dea95e4-e581-4c5f-90aa-acdee3eb3073.png)
Then on the command line enter the command to generate similar formulas:
![image](https://user-images.githubusercontent.com/57302458/130230423-e410b002-e2a0-4607-b635-d6d1b16f0918.png)

The formula entered is P ∨ P ↔ P and the generated results are:

'(P ∨ P → P) valid sat'

'(P ∧ P <=> P) valid sat'

'(P ∧ P → P) valid sat'

'(P ∨ P <=> P) valid sat'

From this I create 4 questions of the type: Prove the following formula.

Another formula:
![image](https://user-images.githubusercontent.com/57302458/130232495-b6278d99-b7ad-48fa-a242-ef25072af7fd.png)
the generated formulas:
![image](https://user-images.githubusercontent.com/57302458/130232547-01fba8a0-c924-422b-a386-668dfb4b4944.png)

Another formula:
![image](https://user-images.githubusercontent.com/57302458/130237068-1e3f8b76-aba5-4ee8-9a15-3429e2fb4ae2.png)
the generated formulas:
![image](https://user-images.githubusercontent.com/57302458/130237126-1ad72c1c-180b-4f03-8f1a-e14aa3d1a7f8.png)


For these I create the question:

Which of the following apply to the formulas below: satisfiable, unsatisfiable, falsifiable, valid? If any formula is valid, write it's proof.


--------------------- Sample HW -------------------------

Q1. Prove the following:

- P ∨ P → P, proof:

- P ∧ P <=> P, proof:

Q2. Which of the following apply to the formulas below: satisfiable, unsatisfiable, falsifiable, valid? If any formula is valid, write it's proof.

- (P → Q) → ((P → Q) ∧ (Q → P))  invalid, satisfiable

- (P <=> Q) → ((P → Q) ∧ (Q → P)) valid, satisfiable. proof:

- (1 > x) == (0 < x) invalid, unsatisfiable

- (1 > x) == (0 > x) invalid, satisfiable
