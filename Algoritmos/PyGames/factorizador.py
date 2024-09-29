import tkinter as tk
import numpy as np
from scipy import special

class FactorizerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Factorizer")

        self.expr_label = tk.Label(master, text="Enter an expression:")
        self.expr_label.pack()

        self.expr_entry = tk.Entry(master, width=50)
        self.expr_entry.pack()

        self.factor_button = tk.Button(master, text="Factor", command=self.factorize)
        self.factor_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def factorize(self):
        expr = self.expr_entry.get()
        try:
            # Try to factorize the expression using numpy and scipy
            coeffs = np.poly1d(expr).c
            roots = np.roots(coeffs)
            factors = []
            for root in roots:
                if root.imag == 0:
                    factors.append(f"x - {root.real}")
                else:
                    factors.append(f"x - ({root.real} + {root.imag}j)")
            factored_expr = " * ".join(factors)
            self.result_label.config(text=f"The factorization of {expr} is: {factored_expr}")
        except Exception as e:
            self.result_label.config(text=f"Error: {e}")

root = tk.Tk()
my_gui = FactorizerGUI(root)
root.mainloop()