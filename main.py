#!/usr/bin/env python3
__author__ = "dogukanarat"

import os
import cv2 as cv
import numpy as np
import skimage

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

# Map component markers to hue val
label_hue = np.uint8( 179 * markers / np.max(markers) )
blank_ch = 255 * np.ones_like( label_hue )
labeled_img = cv.merge([label_hue, blank_ch, blank_ch])

#np.where(label_hue < 5, label_hue, -1)

# cvt to BGR for display
labeled_img = cv.cvtColor(labeled_img, cv.COLOR_HSV2BGR)

# set bg label to black
labeled_img[label_hue == 0] = 0

cv.imshow('Labelled', labeled_img)
cv.waitKey()

if __name__ == '__main__':
    pass
