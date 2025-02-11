#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 7 09:15:12 2025

@author: administrador

&^Z}@{G2VWD&dY30?QR91^~7NT9Z3q4F
"""

def sum_arrays(array1, array2):
    """
    Returns a new list where each element is the sum of the corresponding elements
    from the given arrays.
    """
    result = []
    
    return [e1 + e2 for e1, e2 in zip(array1.values, array2.values)]

def difference_arrays(array1, array2):
    """
    Returns a new list where each element is the difference of the corresponding elements
    from the given arrays.
    """
    return [e2 - e1 for e1, e2 in zip(array1.values, array2.values)]

class Vector:
    '''
    Class to create the arrays
    '''
    values = []
    
    def __init__(self, min, max):
        self.values = [i for i in range(min, max)]
        
    def mean(self):
        """
        Returns the mean value of the given array.
        """
        return sum(self.values) / len(self.values)
        
      
# We declare the arrays for the first and second class
vector_1 = Vector(0, 100)
vector_2 = Vector(100, 200)

# Print the content of the arrays
print(vector_1.values)
print(vector_2.values)

# Array calculation
sum_result = sum_arrays(vector_1, vector_2)
difference_result = difference_arrays(vector_1, vector_2)

# Print the result of the sum of the arrays
print("a1 + a2: ", sum_result)
print("a1 - a2: ", difference_result)
print("First - Array mean         =  ", vector_1.mean())
print("Second - Array mean        =  ", vector_2.mean())

# We compute the maximum and minimum of the first array by iterating the lists
minv = 99999 #We initialize the value of the minimum
maxv = -1
c = g = 0

for i in range(100):
  if(vector_v1.v1[i]>maxv): maxv = vector_v1.v1[i]
  if(vector_v1.v1[i]<minv): minv = vector_v1.v1[i]
  c = c + r[i]
  g = g + f[i]

# # We show the results for the maximum and minimum 
# print('First array maximum: ', maxv)
# print('First array minimum: ', minv)
# print('Mean of the array with the sum: ', c/100)
# print('Mean of the array with the difference: ', g/100)

# # We compute the maximum and minimum of the second array by iterating the lists
# minv = 99999
# maxv = -1
# for i in range(100):
#   if(vector_v2.v2[i]>maxv): maxv = vector_v2.v2[i]
#   if(vector_v2.v2[i]<minv): minv = vector_v2.v2[i]

# print('Second array maximum: ', maxv)
# print('Second array minimum: ', minv)

# #We Compute the maximum and minimum of the array with the sum/difference
# minv = mind = 99999
# maxv = maxd = -1
# for i in range(100):
#   if(r[i]>maxv): maxv = r[i]
#   if(f[i]>maxd): maxd = f[i]
#   if(r[i]<minv): minv = r[i]
#   if(f[i]<mind): mind = f[i]

# print('Maximum of the array with the sum: ', maxv)
# print('Minimum of the array with the sum: ', minv)
# print('Maximum of the array with the difference: ', maxd)
# print('Minimum of the array with the difference: ', mind)
