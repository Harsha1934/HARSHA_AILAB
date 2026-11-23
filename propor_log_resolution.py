
def resolve(c1, c2):
    resolvents = []

    for literal in c1:
        opposite = literal[1:] if literal.startswith("~") else "~" + literal

        if opposite in c2:
            new_clause = (c1 - {literal}) | (c2 - {opposite})
            resolvents.append(new_clause)

    return resolvents


KB = [
    {"~P", "Q"},
    {"~Q", "R"},
    {"P"}
]

query = "R"

print("Knowledge Base:")
for clause in KB:
    print(clause)

clauses = KB + [{"~" + query}]

print("\nNegated Query:", "~" + query)

while True:
    new_clauses = []

    for i in range(len(clauses)):
        for j in range(i + 1, len(clauses)):
            result = resolve(clauses[i], clauses[j])

            for clause in result:
                if not clause:
                    print("\nEmpty clause obtained")
                    print("Query is PROVED")
                    exit()

                new_clauses.append(clause)

    if all(c in clauses for c in new_clauses):
        print("\nQuery cannot be proved")
        break

    for clause in new_clauses:
        if clause not in clauses:
            clauses.append(clause)
