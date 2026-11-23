
def unify(x, y, theta=None):
    if theta is None:
        theta = {}

    if x == y:
        return theta

    if isinstance(x, str) and x.islower():
        if x in theta:
            return unify(theta[x], y, theta)
        if isinstance(y, str) and y.islower() and y in theta:
            return unify(x, theta[y], theta)
        if occurs(x, y, theta):
            return None
        theta[x] = y
        return theta

    if isinstance(y, str) and y.islower():
        return unify(y, x, theta)

    if isinstance(x, tuple) and isinstance(y, tuple):
        if len(x) != len(y) or x[0] != y[0]:
            return None

        for a, b in zip(x[1:], y[1:]):
            theta = unify(a, b, theta)
            if theta is None:
                return None

        return theta

    return None


def occurs(var, term, theta):
    if var == term:
        return True

    if isinstance(term, str) and term in theta:
        return occurs(var, theta[term], theta)

    if isinstance(term, tuple):
        return any(occurs(var, item, theta) for item in term[1:])

    return False


x = ("P", "x", "a")
y = ("P", "b", "y")

print("Expression 1:", x)
print("Expression 2:", y)

result = unify(x, y)

if result is not None:
    print("MGU:", result)
else:
    print("Unification Failed")
