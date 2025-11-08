#!/bin/python3
import unittest

def openFile(name):
    with open(name, 'r') as f: 
        inputs = []
        for line in f.readlines():
            inputs.append(line)
    names = inputs[0][:-1].split(',')
    instructions = inputs[2].split(",")
    return names, instructions

class TestStringMethods(unittest.TestCase):
    def test_case_1_1(self):
        names, instructions = openFile('everybody_codes_e2025_q01_p1.txt')
        self.assertEqual(findName(names, instructions), "Ascaldaros")

    def test_case_1_2(self):
        names, instructions = openFile('everybody_codes_e2025_q01_p2.txt')
        self.assertEqual(findParent(names, instructions), "Shaelardith")

    def test_case_1_3(self):
        names, instructions = openFile('everybody_codes_e2025_q01_p3.txt')
        self.assertEqual(findSecondParent(names, instructions), "Syltaril")


def findName(names, instructions):
    curr = 0 
    for i in range(len(instructions)):
        direction, position = instructions[i][0], int(instructions[i][1:]) 
        #print(direction, position)
        if direction == 'R': 
            if position + curr < len(names):
                curr = position + curr 
            else:
                curr = len(names) - 1 
        else: 
            if curr - position < 0:
                curr = 0 
            else: 
                curr = curr - position
    return names[curr]

def findParent(names, instructions):
    curr = 0 
    larg = 0 
    for i in range(len(instructions)):
        direction, position = instructions[i][0], int(instructions[i][1:]) 
        if direction == 'R': 
            if position + curr < len(names):
                curr = position + curr 
            else:
                curr = (curr + position) % len(names) 
        else: 
            if curr - position < 0:
                curr = len(names) - (abs(position % len(names)- curr))
            else: 
                curr = curr - position
    return names[curr]

def findSecondParent(names, instructions):
    for i in range(len(instructions)):
        direction, position = instructions[i][0], int(instructions[i][1:]) 
        # swap 
        if direction == "R": 
            names[0], names[position % len(names)] = names[position % len(names)], names[0]
        else: 
            names[0], names[-(position % len(names))] = names[-(position % len(names))], names[0]

    return names[0]

if __name__ == "__main__":

    unittest.main(verbosity=2)
