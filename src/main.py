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
    mz = MazeSolver(BASE_DIR + '/contents/no4.png',
                    BASE_DIR + '/results', "RESULTFILE")
    mz.FourPointTransformation()  # rotating the image for operation
    mz.ShowResult()
    mz.FindPath()  # finding the path ino the maze image
    # mz.ShowResult()
    mz.FindRoute()  # finding the route in the maze image
    # mz.ShowResult()
