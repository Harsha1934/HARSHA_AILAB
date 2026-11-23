import random

N = 4

def cost(b):
    h = 0
    for i in range(N):
        for j in range(i+1, N):
            if b[i] == b[j] or abs(b[i]-b[j]) == abs(i-j):
                h += 1
    return h

def hill_climbing():

    b = [random.randint(0, 3) for i in range(N)]

    while True:
        c = cost(b)

        print("\nCurrent State:", b)
        print("Current Cost:", c)

        if c == 0:
            print("Goal State Reached!")
            break

        best = b[:]
        best_cost = c

        print("\nNeighbor Nodes:")

        for col in range(N):
            for row in range(N):
                new = b[:]
                new[col] = row

                if new == b:
                    continue

                nc = cost(new)
                print(new, "Cost =", nc)

                if nc < best_cost:
                    best_cost = nc
                    best = new

                if best_cost == 0:
                    break
            if best_cost == 0:
                break

        if best_cost < c:
            b = best
        else:
            print("No better neighbor. Restarting...")
            b = [random.randint(0, 3) for i in range(N)]

    print("\nFinal Solution:", b)

hill_climbing()