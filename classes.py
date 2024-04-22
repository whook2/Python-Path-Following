# This file holds all the classes used in the program
#
# Contains:
#   SteeringOutput: Holds the linear and angular acceleration values that are passed to the movement functions
#
#   Character: Stores the character information, as well as the character's update function
#
#   Path: Holds the information regarding the path, as well as the functions to assemble the path, get the path
#   parameter, and get the current position along the path
#
#

import helper_functions
import numpy as np


# Declaration of the SteeringOutput class
class SteeringOutput(object):
    def __init__(self):
        self.linear = np.array([0.0, 0.0])
        self.angular = 0.0


# Declaration of the Character class
class Character(object):
    def __init__(self):
        self.id = 0
        self.pos = np.array([0.0, 0.0])
        self.vel = np.array([0.0, 0.0])
        self.accel_x = 0.0
        self.accel_z = 0.0
        self.orient = 0.0
        self.max_velo = 0.0
        self.max_accel = 0.0
        self.target = self
        self.arrival_rad = 0.0
        self.slow_rad = 0.0
        self.time_to_target = 0.0
        self.steering = 2
        self.collision = False
        self.rotation = 0.0
        self.pathToFollow = 0 #added for programming assignment 2
        self.pathOffset = 0.0 #added for programming assignment 2

# Character update function
    def update(self, steering, max_speed, time):
        # Update the position and orientation
        self.pos = self.pos + self.vel * time
        self.orient += self.rotation * time

        # Update the velocity and rotation
        self.vel = self.vel + steering.linear * time
        self.rotation += steering.angular * time

        # Check for speed above max and clip
        if helper_functions.length(self.vel) > max_speed:
            self.vel = helper_functions.normalize(self.vel)
            self.vel *= max_speed



# Class definition for a Path object (used the class from the assignment #2 intro and help video)
class Path(object):
    def __init__(self):
        self.ID = 0 # unique path ID
        self.x = np.array([]) # Array of X cords
        self.z = np.array([]) # Array of Z cords
        self.params = np.array([]) # Array of path parameters at each vertex
        self.distance = np.array([]) # Array of path distance at each vertex
        self.segments = 0 # Number of segments in the path

    def pathAssemble(self, ID, X, Z):
        # Path assemble function
        self.x = X # Assigning the array of X values of the path to the path object
        self.z = Z # Assigning the array of Z values of the path to the path object

        self.segments = len(self.x) - 1 # Calculates the amount of line segments of the path

        self.distance = [0, 0, 0, 0, 0, 0, 0, 0] # Declares an empty list of distances
        for i in range(1, 8):
            # This loop starts at the second point of the path, and finds the total distance covered over the whole path
            self.distance[i] = self.distance[i - 1] + helper_functions.distance([self.x[i - 1], self.z[i - 1]], [self.x[i], self.z[i]])


        self.params = [0, 0, 0, 0, 0, 0, 0, 0] # Declares an empty list of path parameters
        for i in range(0, 8):
            # This loop finds each path parameter by dividing the current distance covered by the total path distance
            self.params[i] = self.distance[i] / self.distance[7]

        return

    def getParam(self, pos):
        # Get parameter function
        closestDistance = 99999

        # Cycle through the line segments to find the closest segment and its corresponding endpoints
        for i in range(0, 7):
            A = np.array([self.x[i], self.z[i]]) # Setting A equal to a point on the path
            B = np.array([self.x[i + 1], self.z[i + 1]]) # Setting B equal to the next point
            checkPoint = helper_functions.closestPoint(pos, A, B) # Finding the closest point of the path
            checkDistance = helper_functions.distance(pos, checkPoint) # Checking the distance from current position to that point
            if checkDistance < closestDistance: # If the distance found is the closest out of all the points
                closestPoint = checkPoint # The closest point is set as the last one checked
                closestDistance = checkDistance # Closest distance is set as the last one checked
                closestSegment = i # Closest line segment of path is set as the current one being iterated through

        A = np.array([self.x[closestSegment], self.z[closestSegment]]) # Vector A set as the start of the closest segment
        A_param = self.params[closestSegment] # A_param is the parameter of the closest line segment
        B = np.array([self.x[closestSegment + 1], self.z[closestSegment + 1]]) # B set as the endpoint of the segment
        B_param = self.params[closestSegment + 1] # B_param is the next parameter
        C = closestPoint # C represents the closest point of the path

        T = helper_functions.length(C - A) / helper_functions.length(B - A) # Length of (C - A) / length of (B - A)
        C_param = A_param + (T * (B_param - A_param)) # This equation establishes the resulting paramater of the path
        return C_param

    def getPos(self, param):
        # Get position function
        for i in range(0,8):
            if self.params[i] <= param and self.params[i + 1] >= param: # If the current parameter is greater than the current but less than the next
                A = np.array([self.x[i], self.z[i]]) # Sets a vector A as the current point on the path
                B = np.array([self.x[i + 1], self.z[i + 1]]) # Sets a vector B as the next point on the path
                T = ((param - self.params[i]) / (self.params[i + 1] - self.params[i])) #
        return A + (T * (B - A))

