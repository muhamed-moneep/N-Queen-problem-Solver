# N-Queens Solver

A Python application that solves the classic **N-Queens problem** using four different search/optimization algorithms, with a Tkinter GUI to run and compare them side by side.

The N-Queens problem asks: how can **N** queens be placed on an **N×N** chessboard so that no two queens attack each other (no shared row, column, or diagonal)?

## Features

- Solves N-Queens using **four different algorithms**
- Simple **Tkinter GUI** — enter a value of N and click **Solve**
- Runs all four algorithms back-to-back and displays each solution board
- Reports **performance metrics** (time taken, steps/iterations, success) for each algorithm
- Prints a final **comparison table** summarizing all four runs

## Algorithms Implemented

| Algorithm | File | Approach |
|---|---|---|
| **Backtracking Search** | `algorithms/backtracking.py` | Recursively places a queen in each row, backtracking whenever no safe column is available. Guaranteed to find a solution if one exists. |
| **Hill Climbing** | `algorithms/hill_climbing.py` | Starts from a random board and repeatedly moves to the neighboring state with the fewest conflicts, stopping if it reaches a local minimum. |
| **Best First Search** | `algorithms/best_first.py` | Uses a priority queue (min-heap) to always expand the state with the fewest conflicts first, exploring neighbors until a conflict-free board is found. |
| **Genetic Algorithm** | `algorithms/genetic.py` | Evolves a population of random boards over generations using selection, crossover, and mutation, guided by a fitness function based on conflict count. |

## Project Structure

```
n_queen_project/
├── main.py                     # Entry point — launches the GUI
├── display.py                  # Tkinter GUI and output formatting
├── utils.py                    # Shared helpers (random board generation, conflict counting)
└── algorithms/
    ├── backtracking.py         # Backtracking search
    ├── hill_climbing.py        # Hill climbing search
    ├── best_first.py           # Best-first search
    └── genetic.py              # Genetic algorithm
```

## How It Works

- A board is represented as a list `board`, where `board[row] = column` — i.e. the index is the row and the value is the column containing the queen in that row. This guarantees exactly one queen per row by construction.
- **Conflicts** between queens are calculated in `utils.calculate_conflicts`, checking for shared columns and shared diagonals between every pair of queens.
- Each algorithm's `solve(n)` function returns a tuple: `(solution_board_or_None, metrics_dict)`, where `metrics_dict` includes the algorithm name, execution time, number of steps, and whether a solution was found.

## Requirements

- Python 3 (developed/tested with Python 3.14)
- Tkinter (included with most standard Python installations)

No external/third-party packages are required.

## Usage

Run the application from the project root:

```bash
python main.py
```

1. Enter a value for **N** (board size / number of queens) in the input box.
2. Click **Solve**.
3. The app runs all four algorithms in a background thread and displays, for each one:
   - The resulting board (as a grid of `.` and `Q`)
   - Its performance metrics (time, steps, success)
4. A comparison table summarizing all four algorithms is shown at the end.

> **Note:** Hill Climbing, Best First Search, and Genetic Algorithm start from random boards and are not guaranteed to succeed on every run (Hill Climbing can get stuck in local minima; Genetic Algorithm may not converge within its generation limit). Backtracking always finds a solution if one exists for the given N.

## Example Output (conceptual)

```
==================================================
Algorithm: Backtracking Search
==================================================

Board:
. Q . .
. . . Q
Q . . .
. . Q .

Metrics:
Time: 0.000123 sec
Steps: 15
Success: True
...

==================================================
COMPARISON TABLE
==================================================
Algorithm           Time (s)       Steps          Success
------------------------------------------------------------
Backtracking         0.000123       15             True
Hill Climbing        0.000456       8              True
Best First Search    0.002310       142            True
Genetic Algorithm    0.015420       37             True
```

## Possible Improvements

- Add configurable parameters (population size, mutation rate, max generations) to the GUI for the Genetic Algorithm.
- Add a visual chessboard rendering instead of text-based output.
- Add random restarts for Hill Climbing to escape local minima more reliably.
- Allow exporting results/comparison table to a file (CSV).
