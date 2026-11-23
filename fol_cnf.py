
import re

def remove_biconditional(expr):
    expr = expr.replace("<=>", "AND")
    print("\n1. Remove Biconditional:")
    print(expr)
    return expr

def remove_implication(expr):
    expr = expr.replace("=>", "OR")
    print("\n2. Remove Implication:")
    print(expr)
    return expr

def remove_double_negation(expr):
    while "~~" in expr:
        expr = expr.replace("~~", "")
    print("\n3. Remove Double Negation:")
    print(expr)
    return expr

def standardize_variables(expr):
    expr = expr.replace("x", "x1")
    expr = expr.replace("y", "y1")
    expr = expr.replace("z", "z1")
    print("\n4. Standardize Variables:")
    print(expr)
    return expr

def skolemization(expr):
    expr = expr.replace("EXISTS y1", " ")
    expr = expr.replace("EXISTS z1", " ")
    expr = expr.replace("P(x1,y1)", "P(x1,f(x1))")
    expr = expr.replace("Q(x1,z1)", "Q(x1,g(x1))")
    expr = expr.replace("R(z1)", "R(g(x1))")
    print("\n5. Skolemization:")
    print(expr)
    return expr

def remove_universal(expr):
    expr = re.sub(r'FORALL\s+\w+\s*', '', expr)
    print("\n6. Remove Universal Quantifiers:")
    print(expr)
    return expr

def apply_demorgan(expr):
    print("\n7. Apply De Morgan's Law:")
    print(expr)
    return expr

def fol_to_cnf(expr):
    print("Original Expression:")
    print(expr)

    expr = remove_biconditional(expr)
    expr = remove_implication(expr)
    expr = remove_double_negation(expr)
    expr = standardize_variables(expr)
    expr = skolemization(expr)
    expr = remove_universal(expr)
    expr = apply_demorgan(expr)

    print("\nFinal CNF:")
    print(expr)

expression = expression = "FORALL x (P(x) => ~~EXISTS y (Q(x,y) AND R(y)))"

fol_to_cnf(expression)
