#!/usr/bin/env python3
__author__ = "dogukanarat"

import os
import cv2 as cv
import numpy as np
from skimage.morphology import skeletonize

# split function definition
def split_image(image, lower_treshold, upper_treshold):

    comp = np.zeros_like(image)
    for i in range(len(image)):
        for j in range(len(image[i])):
            if image[i][j] >= lower_treshold and image[i][j] <= upper_treshold:
                comp[i][j] = 255
            else:
                comp[i][j] = 0
    
    return comp

# defining file path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# reading image
image = cv.imread(BASE_DIR + '/contents/no1.png', cv.IMREAD_GRAYSCALE)
[rows, cols] = image.shape

# normalize image
normalizedImage = cv.normalize(image, None, alpha=0, beta=1, norm_type=cv.NORM_MINMAX, dtype=cv.CV_32F)
ret , binary = cv.threshold(image, 150, 255, cv.THRESH_BINARY)

# invert image
binary = 255 - binary

# erode, dilate image
dilation = cv.dilate(binary, np.ones((6, 6), np.uint8), iterations=3)

# marker labelling
ret, markers = cv.connectedComponents(dilation)

# map component markers to hue val
labeling = np.uint8( 179 * markers / np.max(markers) )

# spliting image into component
component_1 = split_image(labeling, 10, 150)
component_2 = split_image(labeling, 150, 255)

# erode, dilate component
dilated_component_1 = cv.dilate(
    component_1, np.ones((7, 7), np.uint8), iterations=3)
eroded_component_1 = cv.erode(
    dilated_component_1, np.ones((7, 7), np.uint8), iterations=3)

# erode, dilate component
dilated_component_2 = cv.dilate(
    component_2, np.ones((7, 7), np.uint8), iterations=3)
eroded_component_2 = cv.erode(
    dilated_component_2, np.ones((7, 7), np.uint8), iterations=3)

# merging components
merged_image = eroded_component_1 + eroded_component_2

final_image = 255 - merged_image 

#skeleton = skeletonize(image)

cv.imshow('Labelled', final_image)
cv.waitKey()

if __name__ == '__main__':
    pass
