# Will Hooker 
# CS 330-01
# UAH Spring 2024
# Programming assignment 2 - Path following
# This program is a continuation of the first dynamic movement program. Using the same seek function, this program
# implements a path following behavior, given the coordinates for a certain path.
# The movement algorithms are sourced from pseudocode from the textbook "Artificial Intelligence for Games, 3rd Edition"
# by Millington
#
#
import math
import classes
import move_functions
import numpy as np

#---------------------------------------------------------------------------------------------------------------------

# Opening the text file in write mode
f = open("CS 330, Dynamic Trajectory Data.txt", "w")

# Function that prints all character data to the text file in CSV form
def print_character(player, sim_time):
    f.write(str(sim_time) + ',' + str(player.id) + ',' + str(player.pos[0]) + ',' + str(player.pos[1]) + ',' +
            str(player.vel[0]) + ',' + str(player.vel[1]) + ',' + str(player.accel_x) + ',' + str(player.accel_z) +
            ',' + str(player.orient) + ',' + str(player.steering) + ',' + (str(player.collision).upper()))
    f.write('\n')

#---------------------------------------------------------------------------------------------------------------------

# Creation of the path following character
p5 = classes.Character()
p5.id = 2701
p5.steering = 11
p5.pos = np.array([20,95])
p5.vel = np.array([0,0])
p5.orient = 0
p5.max_velo = 4
p5.max_accel = 2
p5.pathToFollow = 1
p5.pathOffset = 0.04

# Initialization of time and timestep
time = 0
timestep = 0.5

#---------------------------------------------------------------------------------------------------------------------

# Printing the initial character values
print_character(p5, time)

# For loop that is used to increment the time and call the movement and update functions
for x in range(0, 251):
    # Increments the time by delta-t
    time += timestep

    # Creating of the path object
    path = classes.Path()
    X = [0, -20, 20, -40, 40, -60, 60, 0] # List of X values of the path points
    Z = [90, 65, 40, 15, -10, -35, -60, -85] # List of Z values of the path points
    path.pathAssemble(1, X, Z) # Function call to assemble the path

    result = move_functions.followPath(p5, path) # Steering result from the followPath function

    p5.accel_x = result.linear[0] # Saving the linear acceleration in the X direction
    p5.accel_z = result.linear[1] # Saving the linear acceleration in the Z direction

    p5.update(result, p5.max_velo, timestep) # Calling the update function to update the characters values

    print_character(p5, time) # Calling the pring function to print the character values to the output file

#---------------------------------------------------------------------------------------------------------------------

f.close()