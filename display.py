import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading

# Import the algorithm functions
from algorithms.backtracking import solve as backtracking
from algorithms.hill_climbing import solve as hill_climbing
from algorithms.best_first import solve as best_first
from algorithms.genetic import solve as genetic

# Helper functions to format output (same as before, but return strings)
def format_board(solution, n):
    if not solution:
        return "No solution found.\n"
    lines = []
    for row in solution:
        line = ['.'] * n
        line[row] = 'Q'
        lines.append(' '.join(line))
    return '\n'.join(lines)


def format_metrics(metrics):
    return (f"Time: {metrics.get('time', 0):.6f} sec\n"
            f"Steps: {metrics.get('steps', 'N/A')}\n"
            f"Success: {metrics.get('success', False)}")


def format_comparison(results):
    header = f"{'Algorithm':<20}{'Time (s)':<15}{'Steps':<15}{'Success':<10}\n"
    header += "-" * 60 + "\n"
    rows = []
    for m in results:
        rows.append(f"{m.get('algorithm', 'Unknown'):<20}"
                    f"{m.get('time', 0):<15.6f}"
                    f"{m.get('steps', 'N/A'):<15}"
                    f"{m.get('success', False)}")
    return header + '\n'.join(rows)


# GUI functions
def run_gui():
    """Create the main window and start the Tkinter event loop."""
    root = tk.Tk()
    root.title("N-Queens Solver")
    root.geometry("700x600")

    # Input frame
    input_frame = tk.Frame(root)
    input_frame.pack(pady=10)

    tk.Label(input_frame, text="Enter N:").pack(side=tk.LEFT, padx=5)
    n_entry = tk.Entry(input_frame, width=5)
    n_entry.pack(side=tk.LEFT, padx=5)

    # Output area
    output_text = scrolledtext.ScrolledText(root, width=80, height=30,
                                            font=("Courier", 10))
    output_text.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    # Function to run the algorithms in a separate thread
    def solve_thread(n):
        results = []
        algorithms = [
            ("Backtracking Search", backtracking),
            ("Hill Climbing Search", hill_climbing),
            ("Best First Search", best_first),
            ("Genetic Search", genetic)
        ]

        for name, algo in algorithms:
            output_text.insert(tk.END, f"\n{'='*50}\nAlgorithm: {name}\n{'='*50}\n")
            sol, met = algo(n)
            output_text.insert(tk.END, "\nBoard:\n")
            output_text.insert(tk.END, format_board(sol, n))
            output_text.insert(tk.END, "\nMetrics:\n")
            output_text.insert(tk.END, format_metrics(met))
            results.append(met)

        output_text.insert(tk.END, "\n" + "="*50 + "\n")
        output_text.insert(tk.END, "COMPARISON TABLE\n")
        output_text.insert(tk.END, "="*50 + "\n")
        output_text.insert(tk.END, format_comparison(results))

        # Re-enable the solve button
        solve_button.config(state=tk.NORMAL)

    # Function called when the Solve button is clicked
    def on_solve_click():
        try:
            n = int(n_entry.get())
            if n <= 0:
                messagebox.showerror("Invalid N", "N must be greater than 0.")
                return
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")
            return

        # Disable button, clear output, start thread
        solve_button.config(state=tk.DISABLED)
        output_text.delete(1.0, tk.END)
        threading.Thread(target=solve_thread, args=(n,), daemon=True).start()

    solve_button = tk.Button(input_frame, text="Solve", command=on_solve_click)
    solve_button.pack(side=tk.LEFT, padx=10)

    root.mainloop()