import time
from utils import generate_random_board, calculate_conflicts


def solve(n):

    start_time = time.time()
    steps = 0

    #initial state
    current = generate_random_board(n)
    current_conflicts = calculate_conflicts(current)

    best = current[:]
    best_conflicts = current_conflicts

    #hill climbing loop
    while current_conflicts > 0:
        steps += 1

        neighbors = []

        #generate neighbors
        for row in range(n):
            for col in range(n):
                if current[row] == col:
                    continue

                neighbor = current[:]
                neighbor[row] = col
                neighbors.append(neighbor)

        #find best neighbor
        next_state = current
        next_conflicts = current_conflicts

        for state in neighbors:
            c = calculate_conflicts(state)

            if c < next_conflicts:
                next_state = state
                next_conflicts = c

        #if no improvement -> stuck (local minimum)
        if next_conflicts >= current_conflicts:
            break

        current = next_state
        current_conflicts = next_conflicts

        #track best
        if current_conflicts < best_conflicts:
            best = current[:]
            best_conflicts = current_conflicts

    end_time = time.time()

    metrics = {
        "algorithm": "Hill Climbing",
        "time": end_time - start_time,
        "steps": steps,
        "final_conflicts": current_conflicts,
        "success": current_conflicts == 0
    }

    return best, metrics