#!/usr/bin/python3
############################################
# Copyright 2024 Alex Chan
# Creation Date: 2/25/2024
# Calculator
# Program to test Calculator Object
############################################

import tkinter as tk
import sys
import TKCalculator as TKC

def testCalculator():
    Calculator = TKC.CalculatorObj()

def testCalculator_module():
    newFrame = tk.Tk()
    Calculator = TKC.CalculatorObj(newFrame)
    newFrame.mainloop()

if __name__ == "__main__":
    
    testCalculator()
    #testCalculator_module()
    sys.exit(0)
