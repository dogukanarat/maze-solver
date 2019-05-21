#!/usr/bin/env python3
__author__ = "dogukanarat"

import os
import warnings
import uuid
import mazesolver.solver as solver # importing our package

warnings.filterwarnings("ignore")

# defining file path
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # defining base dire

if __name__ == '__main__':

    mz = solver.mazeSolver(BASE_DIR + '/contents/no1.png', BASE_DIR + '/results', "RESULTFILE") # call the object defining the maze image
    mz.findPath() # finding the path ino the maze image
    mz.findRoute() # finding the route in the maze image