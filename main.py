#!/usr/bin/env python3
__author__ = "dogukanarat"

import os
import warnings
import uuid
from mazeSolver.core import mazeSolver

warnings.filterwarnings("ignore")

# defining file path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':

    mz = mazeSolver(BASE_DIR + '/contents/no1.png', BASE_DIR + '/results')
    mz.findPath()
    mz.findRoute()
