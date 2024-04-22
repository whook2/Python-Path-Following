# This file holds the movement functions used determine the character's values
#
# Contains:
#
#   Seek: The Seek movement function from the textbook pseudocode. This movement behavior makes the character chase
#   the targets position
#
#   followPath: The follow path function from the textbook pseudocode. This movement behavior calculates a point on the
#   path for the character to follow, and then passes that information to the seek function.
#
#
import classes
import helper_functions
import numpy as np


def seek(character, target):
    # Create output structure
    result = classes.SteeringOutput()
    result.linear = np.array([0.0, 0.0])
    result.angular = 0.0

    # Get the direction to the target
    result.linear[0] = target.pos[0] - character.pos[0]
    result.linear[1] = target.pos[1] - character.pos[1]

    # Accelerate at maximum rate
    result.linear = helper_functions.normalize(result.linear)
    result.linear[0] *= character.max_accel
    result.linear[1] *= character.max_accel

    # Output steering
    result.angular = 0
    return result


def followPath(character, path):
    # Find current position on path
    currentParam = path.getParam(character.pos)

    # Offset it
    targetParam = min(1, currentParam + character.pathOffset)

    # Get the target position
    target = classes.Character()
    target.pos = path.getPos(targetParam)

     # Send to seek
    return seek(character, target)
