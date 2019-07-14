#!/usr/bin/env python3

import os
import warnings
import uuid
from modules.MazeSolver import MazeSolver  # importing our package

warnings.filterwarnings("ignore")

# defining file path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # defining base dire

if __name__ == '__main__':

    # call the object defining the maze image
    mz = MazeSolver(BASE_DIR + '/contents/no2.png',
                    BASE_DIR + '/results', "RESULTFILE")
    
    # rotating the image for operation
    mz.FourPointTransformation()
    # finding the path ino the maze image
    mz.FindPath() 
    # finding the route in the maze image
    mz.FindRoute()  
