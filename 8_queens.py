import random
import math

def heuristic(state):
    conflicts = 0
    n = len(state)

    for i in range(n):
        for j in range(i + 1, n):
            if abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts


def simulated_annealing(n):
    current = [random.randint(0, n - 1) for _ in range(n)]
    T = 1000
    alpha = 0.99
    min_temp = 0.001

    while T > min_temp:
        current_cost = heuristic(current)

        if current_cost == 0:
            return current

        next_state = current.copy()

        col = random.randint(0, n - 1)
        next_state[col] = random.randint(0, n - 1)

        next_cost = heuristic(next_state)

        delta_E = current_cost - next_cost

        if delta_E > 0:
            current = next_state
        else:
            probability = math.exp(delta_E / T)

            if random.random() < probability:
                current = next_state

        T = T * alpha

    return current


n = 8
solution = simulated_annealing(n)

print("N-Queens Problem using Simulated Annealing")
print("Final Board:")

for row in range(n):
    for col in range(n):
        if solution[col] == row:
            print("Q", end=" ")
        else:
            print(".", end=" ")
    print()

print("Queen Positions:", solution)
print("Number of Conflicts:", heuristic(solution))

if heuristic(solution) == 0:
    print("Solution Found!")
else:
    print("Solution Not Found!")