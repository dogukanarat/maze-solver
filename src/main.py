#!/usr/bin/env python3
__author__ = "dogukanarat"

import os
import warnings
import uuid
from modules.Solver import MazeSolver  # importing our package

warnings.filterwarnings("ignore")

# defining file path
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # defining base dire

if __name__ == '__main__':

    mz = MazeSolver(BASE_DIR + '/contents/no1.png', BASE_DIR + '/results', "RESULTFILE") # call the object defining the maze image
    mz.FindPath() # finding the path ino the maze image
    mz.FindRoute() # finding the route in the maze image
