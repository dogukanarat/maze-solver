#!/usr/bin/env python3
__author__ = "dogukanarat"

import os
import cv2 as cv
import numpy as np
from skimage.viewer import ImageViewer

# defining file path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# reading image
image = cv.imread(BASE_DIR + '/skel.jpg', cv.IMREAD_GRAYSCALE)
[rows, cols] = image.shape

normalizedImage = cv.normalize(
    image, None, alpha=0, beta=1, norm_type=cv.NORM_MINMAX, dtype=cv.CV_32F)
ret, binary = cv.threshold(image, 150, 255, cv.THRESH_BINARY)

# finding the starting point
done, i, j = False, 0, 0

while( not done ):
    for item in binary[i]:
        if item == 255:
            row = i
            col = j
            done = True
        j += 1
    j = 0
    i += 1

# finding the path
next = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
prev = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
router = [[1, 2, 3], [4, 5, 6], [7, 8 ,9]]
path = []

done = 2
while( not (done == 0) ):
    for i in (-1,0,1):
        for j in (-1, 0, 1):
            if binary[row+i][col+j] == 255 and not i == 0 and not j == 0:
                next[i+1][j+1] = 1
                path.append(router[i+1][j+1])
                row = row + i
                col = col + j
            else:
                pass
    done = done - 1

print(path)

if __name__ == "__main__":
    pass
