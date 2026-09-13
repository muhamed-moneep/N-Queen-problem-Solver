import time

def solve(n):

    start_time = time.time()
    steps = 0

    #Board Index = ROW (x-axis)
    #board[x] = y  (x = row, y = column)

    board = [-1] * n  # board[row] = column of queen in that row

    def is_safe(x, y):  # x = proposed row, y = proposed column
        for r in range(x):  # Check all previously placed rows (0 to x-1)
            c = board[r]  # Column of queen in row 'r'

            #check if same column
            if c == y:
                return False

            #check if same diagonal
            # Distance in X (rows) must equal Distance in Y (columns)
            if abs(r - x) == abs(c - y):
                return False
        return True


    def backtrack(x):  #x = current row we are trying to fill
        nonlocal steps
        steps += 1

        #base case: all rows filled
        if x == n:
            return True

        #try placing queen in each column of the current row
        for y in range(n):
            if is_safe(x, y):
                board[x] = y  # Place queen at (x, y)

                if backtrack(x + 1):
                    return True

                board[x] = -1  #undo

        return False

    success = backtrack(0)
    end_time = time.time()

    metrics = {
        "algorithm": "Backtracking",
        "time": end_time - start_time,
        "steps": steps,
        "success": success
    }

    # Return format: board[x] = y
    return board if success else None, metrics