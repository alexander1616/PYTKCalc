#!/usr/bin/python3
############################################
# Copyright 2024 Alex Chan
# Creation Date: 2/25/2024
# Calculator
# Program to test Calculator Object
############################################

import tkinter as tk

if __name__ == "__main__":
    # world starts here
    newFrame = tk.Tk()
    import Calc5
    Calculator = Calc5.CalculatorObj(newFrame)
    newFrame.mainloop()
    sys.exit(0)
