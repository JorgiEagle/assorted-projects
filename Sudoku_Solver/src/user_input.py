import tkinter as tk
from solver import SudokuSolver


class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku")
        self.entries = [[tk.Entry(root, width=2, font=('Arial', 24), justify='center') for _ in range(9)] for _ in range(9)]
        self.create_grid()
        self.submit_button = tk.Button(root, text="Submit", command=self.submit)
        self.submit_button.grid(row=9, columnspan=9)
        self.error_label = tk.Label(root, text="", fg="red")
        self.error_label.grid(row=10, columnspan=9)
        self.solver = SudokuSolver()

    def create_grid(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].grid(row=i, column=j, padx=(2 if j % 3 == 0 else 0, 2 if (j+1) % 3 == 0 else 0), pady=(2 if i % 3 == 0 else 0, 2 if (i+1) % 3 == 0 else 0))

    def submit(self):
        values = []
        for i in range(9):
            for j in range(9):
                value = self.entries[i][j].get()
                if value:
                    try:
                        values.append(int(value))
                    except ValueError:
                        values.append(None)
                else:
                    values.append(None)
        self.solver.set_initial_grid(values)
        invalid_indices = self.solver.validate(values)
        if invalid_indices:
            self.highlight_errors(invalid_indices)
            self.error_label.config(text="Invalid input detected. Please correct the highlighted cells.")
        else:
            self.error_label.config(text="")
            new_values = self.solver.solve()
            self.fill_grid(new_values)

    def highlight_errors(self, indices):
        for i in range(9):
            for j in range(9):
                idx = i * 9 + j
                if idx in indices:
                    self.entries[i][j].config(bg="#FA8072")
                else:
                    self.entries[i][j].config(bg="white")       

    def fill_grid(self, values):
        for i in range(9):
            for j in range(9):
                value = values[i * 9 + j]
                self.entries[i][j].delete(0, tk.END)
                if value is not None:
                    self.entries[i][j].insert(0, str(value))


if __name__ == "__main__":
    root = tk.Tk()
    gui = SudokuGUI(root)
    sample_values = [i if i % 2 == 0 else None for i in range(81)]  # Sample data to fill the grid
    gui.fill_grid(sample_values)
    root.mainloop()
