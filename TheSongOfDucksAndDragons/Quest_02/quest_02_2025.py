#!/bin/python3
import unittest

'''
def openFile(name):
    with open(name, 'r') as f: 
        inputs = []
        for line in f.readlines():
            inputs.append(line)
    names = inputs[0][:-1].split(',')
    instructions = inputs[2].split(",")
    return names, instructions
'''

class TestStringMethods(unittest.TestCase):
    def test_case_2_1(self):
        self.assertEqual(findNumber([155,53]), [357,862])


def findNumber(A): 
    R = [0,0] # the result 
    print()
    for _ in range(3): 

        #R = [0,0] [0,0]
        # Myltiply the result by itself
        R[0], R[1] = R[0]*R[0]-R[1]*R[1], R[0]*R[1] + R[0]*R[1]
        print(f' After Multi: {R}')
        # Divide the result by [10,10]
        R[0], R[1] = R[0]//10, R[1]//10
        print(f' After Divide: {R}')
        # Add A to the result 
        R[0], R[1] = R[0]+A[0], R[1]+A[1]
        print(f' After Add: {R}')
    return R

    return [357,862]

if __name__ == "__main__":
    unittest.main(verbosity=2)


