#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cleaned code example using SOLID and clean code best practices.
"""

class Vector:
    """
    Represents an integer range as a list of values.
    """
    def __init__(self, start=None, end=None):
        if start is None or end is None:
            self.values = []
        else:
            self.values = [i for i in range(start, end)]

    def get_min(self):
        """
        Returns the minimum value of the vector.
        """
        if not self.values:
            return None
        return min(self.values)

    def get_max(self):
        """
        Returns the maximum value of the vector.
        """
        if not self.values:
            return None
        return max(self.values)

    def get_mean(self):
        """
        Returns the mean value of the vector.
        """
        if not self.values:
            return None
        return sum(self.values) / len(self.values)

def add_vectors(vec1, vec2):
    """
    Returns a new Vector containing element-wise sums of the given vectors.
    """
    result = Vector()
    for v1, v2 in zip(vec1.values, vec2.values):
        result.values.append(v1 + v2)
    return result

def subtract_vectors(vec1, vec2):
    """
    Returns a new Vector containing element-wise differences of the given vectors.
    """
    result = Vector()
    for v1, v2 in zip(vec1.values, vec2.values):
        result.values.append(v1 - v2)
    return result

# Example usage
vector_1 = Vector(0, 100)
vector_2 = Vector(100, 200)

sum_result = add_vectors(vector_1, vector_2)
diff_result = subtract_vectors(vector_2, vector_1)

print("a1 = ", vector_1.values, "\n")
print("a2 = ", vector_2.values, "\n")
print("a1 + a2:", sum_result.values, "\n")
print("a2 - a1:", diff_result.values, "\n")

print("First - Array minimum  =", vector_1.get_min())
print("First - Array maximum  =", vector_1.get_max())
print("First - Array mean     =", vector_1.get_mean())

print("Second - Array minimum =", vector_2.get_min())
print("Second - Array maximum =", vector_2.get_max())
print("Second - Array mean    =", vector_2.get_mean())

print("Sum - Array minimum    =", sum_result.get_min())
print("Sum - Array maximum    =", sum_result.get_max())
print("Sum - Array mean       =", sum_result.get_mean())

print("Diff - Array minimum   =", diff_result.get_min())
print("Diff - Array maximum   =", diff_result.get_max())
print("Diff - Array mean      =", diff_result.get_mean())
