# This file holds all of the helper functions used throughout the program
#
# Contains:
#   length: Calculates the length of a 2D vector
#
#   normalize: Function normalizes a given 2D vector
#
#   dotProduct: Calculates the dot product of 2 vectors
#
#   distance: Calculates the Euclidean distance between two points
#
#   closestPoint: Calculates the point on a line segment closest to the query point
#
#
import math
import numpy as np


def length(vel):
    return math.sqrt(vel[0] ** 2 + vel[1] ** 2)


def normalize(vel):
    velLength = length(vel)
    if velLength != 0:
        result = np.array([vel[0]/velLength, vel[1]/velLength])
        return result
    else:
        return vel


def dotProduct(A, B):

    return sum(A * B)


def distance(A, B):
    
    return math.sqrt(((B[0] - A[0]) ** 2) + ((B[1] - A[1]) ** 2))


def closestPoint(Q, A, B):

    T = dotProduct((Q - A), (B - A)) / dotProduct((B - A), (B - A))
    if T <= 0:
        return A
    elif T >= 1:
        return B
    else:
        return (A + (T * (B - A)))
