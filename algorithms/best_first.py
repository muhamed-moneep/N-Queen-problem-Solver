import time
import heapq
from utils import generate_random_board, calculate_conflicts


def solve(n):

    start_time = time.time()
    steps = 0

    #initial state
    initial = generate_random_board(n)

    #priority queue (min-heap)
    pq = []
    heapq.heappush(pq, (calculate_conflicts(initial), initial))

    visited = set()
    best_solution = None

    #search loop
    while pq:
        steps += 1

        conflicts, state = heapq.heappop(pq)

        state_tuple = tuple(state)

        if state_tuple in visited:
            continue

        visited.add(state_tuple)

        #goal state
        if conflicts == 0:
            best_solution = state
            break

        #generate neighbors
        for row in range(n):
            for col in range(n):
                if state[row] == col:
                    continue

                neighbor = state[:]
                neighbor[row] = col

                heapq.heappush(
                    pq,
                    (calculate_conflicts(neighbor), neighbor)
                )

    end_time = time.time()

    metrics = {
        "algorithm": "Best First Search",
        "time": end_time - start_time,
        "steps": steps,
        "success": best_solution is not None
    }

    return best_solution, metrics