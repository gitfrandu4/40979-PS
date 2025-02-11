#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 7 09:15:12 2025

@author: administrador

&^Z}@{G2VWD&dY30?QR91^~7NT9Z3q4F
"""

class Vector:
    '''
    Class to create the arrays
    '''
    values = []
    
    def __init__(self, min = None, max = None):
        """
        Constructor of the class. It initializes the array with the given values.
        """
        if min is None or max is None:
            self.values = []
        else:
            self.values = [i for i in range(min, max)]
        
    def mean(self):
        """
        Returns the mean value of the given array.
        """
        return sum(self.values) / len(self.values)
    
    def min(self):
        """
        Returns the minimum value of the given array.
        """
        return min(self.values)
    
    def max(self):
        """
        Returns the maximum value of the given array.
        """
        return max(self.values)
        

def sum_arrays(array1, array2):
    """
    Returns a new list where each element is the sum of the corresponding elements
    from the given arrays.
    """
    result = Vector()
    
    for e1, e2 in zip(array1.values, array2.values):
        result.values.append(e1 + e2)
    
    return result

def difference_arrays(array1, array2):
    """
    Returns a new list where each element is the difference of the corresponding elements
    from the given arrays.
    """
    result = Vector()
    
    for e1, e2 in zip(array1.values, array2.values):
        result.values.append(e1 - e2)

    return result
      
# Declare the arrays for the first and second class
vector_1 = Vector(0, 100)
vector_2 = Vector(100, 200)

# Array calculations
sum_result = sum_arrays(vector_1, vector_2)
diff_result = difference_arrays(vector_2, vector_1)

# Print the results
print("a1 = ", vector_1.values, "\n")
print("a2 = ", vector_2.values, "\n")
print("a1 + a2: ", sum_result.values, "\n")
print("a1 - a2: ", diff_result.values, "\n")

# results for the first array
print("First - Array minimum      =  ", vector_1.min())
print("First - Array maximum      =  ", vector_1.max())
print("First - Array mean         =  ", vector_1.mean())

# results for the second array
print("Second - Array minimum     =  ", vector_2.min())
print("Second - Array maximum     =  ", vector_2.max())
print("Second - Array mean        =  ", vector_2.mean())

# results for the maximum
print("Sum - Array minimum        =  ", sum_result.min())
print("Sum - Array maximum        =  ", sum_result.max())
print("Sum - Array mean           = ", sum_result.mean())

# results for the minimum
print("Difference - Array minimum =  ", diff_result.min())
print("Difference - Array maximum =  ", diff_result.max())
print("Difference - Array mean    = ", diff_result.mean())
