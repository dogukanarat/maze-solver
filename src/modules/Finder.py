#!/usr/bin/env python3

import os
import cv2 as cv
import numpy as np
from skimage.morphology import skeletonize
from skimage.filters import threshold_otsu
from skimage.viewer import ImageViewer
from skimage import io


# split function definition


def SplitImage(self, image, LOWER_TRESHOLD, UPPER_TRESHOLD):
    '''
    Definition: This module process to split an image into its components\n
    Usage: Object.SplitImage()
    '''

    tempImage = np.zeros_like(image)
    for i in range(len(image)):
        for j in range(len(image[i])):
            if image[i][j] >= LOWER_TRESHOLD and image[i][j] <= UPPER_TRESHOLD:
                tempImage[i][j] = 255
            else:
                tempImage[i][j] = 0

    return tempImage

# path finder defition


def FindPath(self):
    '''
    Definition: This module process to find a route into given image\n
    Usage: Object.FindPath()
    '''

    # reading image
    image = cv.imread(self.fileRotated, cv.IMREAD_GRAYSCALE)

    # thresholding image
    _, binary = cv.threshold(image, 150, 255, cv.THRESH_BINARY)

    # inverting image
    binary = 255 - binary

    # eroding, dilating image
    dilation = cv.dilate(binary, np.ones((6, 6), np.uint8), iterations=3)

    # marker labelling
    _, markers = cv.connectedComponents(dilation)

    # maping component markers to hue value
    labeling = np.uint8(179 * markers / np.max(markers))

    # spliting image into component
    componentOne = self.SplitImage(labeling, 10, 150)
    componentTwo = self.SplitImage(labeling, 150, 255)

    # eroding, dilating component
    dilatedComponentOne = cv.dilate(
        componentOne, np.ones((7, 7), np.uint8), iterations=3)
    erodedComponentOne = cv.erode(
        dilatedComponentOne, np.ones((7, 7), np.uint8), iterations=3)

    # eroding, dilating component
    dilatedComponentTwo = cv.dilate(
        componentTwo, np.ones((7, 7), np.uint8), iterations=3)
    erodedComponentTwo = cv.erode(
        dilatedComponentTwo, np.ones((7, 7), np.uint8), iterations=3)

    # merging components
    mergedImage = erodedComponentOne + erodedComponentTwo

    # inverting the image
    finalImage = 255 - mergedImage

    # skeleton algorithm
    kernel = np.ones((1, 1), np.uint8)
    opening = cv.morphologyEx(finalImage, cv.MORPH_OPEN, kernel)
    blur = cv.GaussianBlur(opening, (1, 1), 0)
    _, threshHolded = cv.threshold(
        blur, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
    threshHolded[threshHolded == 255] = 1
    skeletoneImage = skeletonize(threshHolded)

    # saving the image as skeleton structure
    skeletoneImage = skeletoneImage * 255
    skeletoneImage = skeletoneImage.astype(np.uint8)
    io.imsave(fname=self.fileSkeletone, arr=skeletoneImage)

    self.level = skeletoneImage
    print('Finding path was successfully operated!')

    return None


if __name__ == '__main__':
    pass
