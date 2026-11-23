
from itertools import product

print("KNOWLEDGE BASE")
print("P => Q")
print("Q => R")
print("P")

print("\nTRUTH TABLE")
print("P\tQ\tR\tP=>Q\tQ=>R\tKB")

entails = True

for P, Q, R in product([True, False], repeat=3):

    rule1 = (not P) or Q
    rule2 = (not Q) or R
    KB = rule1 and rule2 and P

    print(
        P, "\t", Q, "\t", R, "\t",
        rule1, "\t", rule2, "\t", KB
    )

    if KB and not R:
        entails = False

print("\nQUERY: R")

if entails:
    print("KB entails the query")
else:
    print("KB does not entail the query")
