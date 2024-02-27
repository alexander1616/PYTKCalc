#!/usr/bin/python3
############################################
# Copyright 2024 Alex Chan
# Creation Date: 2/25/2024
# Calculator
# Program to demonstrate TKinter in Python
############################################

import tkinter as tk
import numpy as np
import sys
from functools import partial

class CalculatorObj:
    def __init__(self, root=None):
        import StateMap
        self.StateObj = StateMap.StateMap()
        self.calculation = ""
        self.text_result = None
        if root is None:
            self.root = tk.Tk()
        else:
            self.root = root
        self.button_font = "Arial"
        self.button_fs = 14
        self.button_width = 5
        self.create_calculator()
        
        # run as standard function
        if root is None:
            self.main_loop()

    def main_loop(self):
        self.root.mainloop()

    def create_buttons(self):
        #button_list = [(row, col, key)]
        button_list = [(2, 1, "1"), (2, 2, "2"), (2, 3, "3"), (2, 4, "+")
                      ,(3, 1, "4"), (3, 2, "5"), (3, 3, "6"), (3, 4, "-")
                      ,(4, 1, "7"), (4, 2, "8"), (4, 3, "9"), (4, 4, "*")
                      ,(5, 1, "("), (5, 2, "0"), (5, 3, ")"), (5, 4, "/")
                      ,(6, 1, "."), (6, 2, "c"), (6, 3, "%"), (6, 4, "=")
                      ]
        for (row, col, key) in button_list:
            event_func = None
            if key == "c":
                event_func = self.clear_field
            elif key == "=":
                event_func = self.evaluate_calculation
            else:
                event_func = partial(self.add_to_calculation, key)
            new_button = tk.Button(self.root, text=key, command=event_func,
                                width=self.button_width, font=(self.button_font, self.button_fs))
            new_button.grid(row=row, column=col)

    def create_calculator(self):
        self.root.geometry("300x275")
        self.root.title("Alex Calc")
        self.root.configure(background="light green")
        self.text_result = tk.Text(self.root, height=2, width=17, font=("Arial", 24))

        # bind text event
        self.text_result.configure(state='disabled')
        self.text_result.bind("<Key>", self.process_event)
        self.text_result.grid(columnspan=5)
        
        #creating buttons
        self.create_buttons()
    
    def add_to_calculation(self, symbol):
        self.text_result
        self.text_result.configure(state='normal')
        self.calculation += str(symbol)
        self.text_result.delete(1.0, "end")
        self.text_result.insert(1.0, self.calculation)
        self.text_result.configure(state='disabled')

    def remove_from_calculation(self):
        self.text_result.configure(state='normal')
        self.calculation = self.calculation[:-1]
        self.text_result.delete(1.0, "end")
        self.text_result.insert(1.0, self.calculation)
        self.text_result.configure(state='disabled')

    def evaluate_calculation(self):
        self.text_result.configure(state='normal')
        try:
            self.calculation = str(eval(self.calculation))
            self.text_result.delete(1.0, "end")
            self.text_result.insert(1.0, self.calculation)
        except:
            self.clear_field()
            self.text_result.insert(1.0, "Error")
        self.text_result.configure(state='disabled')

    def clear_field(self):
        self.text_result.configure(state='normal')
        self.calculation = ""
        self.text_result.delete(1.0, "end")
        self.text_result.configure(state='disabled')

    def process_event(self, event):
        state = 0

        #print(event)
        if event.char == '':
            return 0
        state = self.StateObj.getState(event.char)
        self.check_event(event, state)

    def check_event(self, event, state):
        if state == 0:
            return
        if state == 1:
            self.add_to_calculation(event.char)
            return
        if state == 2:
            self.evaluate_calculation()
            return
        if state == 3:
            self.remove_from_calculation()
            return

def calculator():
    root = tk.Tk()
    Calculator = CalculatorObj(root)
    root.mainloop()

if __name__ == "__main__":
    # world starts here
    calculator()
    sys.exit(0)
