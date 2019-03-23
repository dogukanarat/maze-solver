#!/usr/bin/env python3
__author__ = "dogukanarat"

import os
import cv2 as cv
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# reading image
image = cv.imread(BASE_DIR + '/contents/no1.png', cv.IMREAD_GRAYSCALE)
[rows, cols] = image.shape

# normalize image
normalizedImage = cv.normalize(image, None, alpha=0, beta=1, norm_type=cv.NORM_MINMAX, dtype=cv.CV_32F)
ret , binary = cv.threshold(image, 150, 255, cv.THRESH_BINARY)

# erode image
kernel = np.ones((10, 10), np.uint8)
erosion = cv.erode(binary, kernel, iterations=3)

#print(mask)
cv.imshow("Preview", erosion)
cv.waitKey(0)

if __name__ == '__main__':
    pass
