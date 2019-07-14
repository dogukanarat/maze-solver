#!/usr/bin/env python3

import os
import cv2 as cv
import numpy as np
import sys
import time
from skimage.viewer import ImageViewer
from skimage import io

# router algorithm defition


def FindRoute(self):
    '''
    Definition: This module process for finding route into skeletonized image\n
    Usage: Object.FindRoute()
    '''

    # reading image
    image = cv.imread(self.fileSkeletone, cv.IMREAD_GRAYSCALE)
    [rows, cols] = image.shape

    # creating test image
    blankImage = np.zeros((rows, cols, 3), np.uint8)

    # thresholding image
    _, binary = cv.threshold(image, 150, 255, cv.THRESH_BINARY)

    # finding the starting point
    done, i, j = False, 0, 0
    while(not done):
        for item in binary[i]:
            if item == 255:
                row = i
                col = j
                done = True
            j += 1
        j = 0
        i += 1

    # preparing the algorithm
    router = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    path = []
    done = False
    rowTemp, colTemp = 0, 0

    # finding the path
    while(not done):
        rowTemp = row
        colTemp = col
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if((binary[row+i][col+j] == 255) and not((i == 0) and (j == 0))):
                    path.append(router[i+1][j+1])

                    # test image
                    blankImage[row, col] = (0, 0, 255)

                    binary[row][col] = 0
                    row = row + i
                    col = col + j

                    #print("Status: [{},{}] in [{}, {}] was processed!".format(row, col, rows, cols), end="\r", flush=True)
                else:
                    pass
        if(rowTemp == row and colTemp == col):
            done = True

    # saving the result
    np.savetxt(self.fileRoute, path, delimiter=',', fmt='%1u')

    # saving the test file
    blankImage = blankImage.astype(np.uint8)
    io.imsave(fname=self.fileCheck, arr=blankImage)

    self.level = blankImage
    print('Creating route file was successfully done!')

    return None


if __name__ == "__main__":
    pass
