#!/usr/bin/python3
############################################
# Copyright 2024 Alex Chan
# Creation Date: 2/25/2024
# State Map
# Object to determine Input State
############################################

import numpy as np

class StateMap:
    def __init__(self):
        self.alexarray = np.zeros(256)
        self.create_allowed_table()

    def create_allowed_table(self):
        for i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '+', '%', '/', '*', '(', ')']:
            self.alexarray[ord(i)]=1
        self.alexarray[ord('=')]=2
        self.alexarray[13]=2
        self.alexarray[10]=2
        self.alexarray[8]=3
        
    def getState(self, c):
        state = self.alexarray[ord(c)]
        return state
