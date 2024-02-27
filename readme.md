############################################
# Copyright 2024 Alex Chan
# Creation Date: 2/25/2024
# Python TK Calculator
############################################


# Python Calculator with Tkinter

A simple calculator implemented in Python using Tkinter, supporting basic arithmetic operations, exponents, decimals, and parenthesis.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Usage as a Module](#usage-as-a-module)
- [Keyboard Input](#keyboard-input)

## Installation

Ensure you have Python installed on your system. Clone the repository and navigate to the project directory.

```bash
git clone https://github.com/alexander1616/PYTKCalc
```

## Usage

Run the calculator as an independent program:

```bash
python3 testCalculator.py
```
### Usage as a Module

Run the Calculator as a Module:

```bash
import TKCalculator as TKC
root = tk.Tk()
Calculator = TKC.CalculatorObj(root)
root.mainloop()
```

### Keyboard Input

The calculator captures input from the keyboard when clicking the "screen", allowing users to type expressions directly. It validates input to ensure only number keys and approved functions are accepted.




## Features

- Addition
- Subtraction
- Multiplication
- Division
- Exponents
- Decimals
- Parenthesis
