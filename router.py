#!/usr/bin/env python3
__author__ = "dogukanarat"

import os
import cv2 as cv
import numpy as np

# defining file path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# reading image
image = cv.imread(BASE_DIR + '/skel.jpg', cv.IMREAD_GRAYSCALE)
[rows, cols] = image.shape

#core algorithm

if __name__ == "__main__":
    pass