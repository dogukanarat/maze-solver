#!/usr/bin/env python3
__author__ = "dogukanarat"

import os
import cv2 as cv
import numpy as np
from skimage.morphology import skeletonize
from skimage.filters import threshold_otsu
from skimage.viewer import ImageViewer
from skimage import io

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

# path finder defition
def find_path(image_file, target_file):

    # reading image
    image = cv.imread(image_file, cv.IMREAD_GRAYSCALE)
    [rows, cols] = image.shape

    # thresholding image
    _, binary = cv.threshold(image, 150, 255, cv.THRESH_BINARY)

    # inverting image
    binary = 255 - binary

    # eroding, dilating image
    dilation = cv.dilate(binary, np.ones((6, 6), np.uint8), iterations=3)

    # marker labelling
    _, markers = cv.connectedComponents(dilation)

    # maping component markers to hue value
    labeling = np.uint8( 179 * markers / np.max(markers) )

    # spliting image into component
    component_1 = split_image(labeling, 10, 150)
    component_2 = split_image(labeling, 150, 255)

    # eroding, dilating component
    dilated_component_1 = cv.dilate(
        component_1, np.ones((7, 7), np.uint8), iterations=3)
    eroded_component_1 = cv.erode(
        dilated_component_1, np.ones((7, 7), np.uint8), iterations=3)

    # eroding, dilating component
    dilated_component_2 = cv.dilate(
        component_2, np.ones((7, 7), np.uint8), iterations=3)
    eroded_component_2 = cv.erode(
        dilated_component_2, np.ones((7, 7), np.uint8), iterations=3)

    # merging components
    merged_image = eroded_component_1 + eroded_component_2

    # inverting the image
    final_image = 255 - merged_image 

    # skeleton algorithm
    kernel = np.ones((1, 1), np.uint8)
    opening = cv.morphologyEx(final_image, cv.MORPH_OPEN, kernel)
    blur = cv.GaussianBlur(opening, (1, 1), 0)
    _, th4 = cv.threshold(blur, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
    th4[th4 == 255] = 1
    skel = skeletonize(th4)

    # saving the image as skeleton structure
    skel = skel * 255
    skel = skel.astype(np.uint8)
    io.imsave(fname=target_file, arr=skel)

    print('Finding path was successfully operated!')
    
    return 0

if __name__ == '__main__':
    pass