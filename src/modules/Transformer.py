#!/usr/bin/env python3

import cv2 as cv
import numpy as np
from skimage import io
from functools import reduce


def FourPointTransformation(self):
    '''
    Definition: This module transform image into useful format for other process of object\n
    Usage: Object.FourPointTransformation()
    '''

    # reading image
    image = cv.imread(self.image)

    # convert to gray scale
    grayImage = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # invert gray scale
    grayImage = cv.bitwise_not(grayImage)

    # find the firt non-empty coordinates
    coordinates = np.column_stack(np.where(grayImage > 0))

    # find the angle of min area rectangle
    angle = cv.minAreaRect(coordinates)[-1]

    # rescale the angle
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle

    # find the size of the image
    height, width = image.shape[:2]

    # find the center of the image
    centerOfImage = (width / 2, height / 2)

    # operate rotation with found parameters
    rotationMatrix = cv.getRotationMatrix2D(centerOfImage, angle, 1.0)
    rotatedImage = cv.warpAffine(
        image, rotationMatrix, (width, height), borderMode=cv.BORDER_REFLECT)

    grayScale = cv.cvtColor(rotatedImage, cv.COLOR_BGR2GRAY)
    grayScaleTranspose = np.transpose(grayScale)

    rowIndex = 0
    columnIndex = 0

    for item in grayScale:
        sumOfArray = sum(item)
        averageOfArray = sumOfArray / len(item)
        if averageOfArray <= 150:
            topTrim = rowIndex
            break
        rowIndex += 1

    for item in grayScaleTranspose:
        sumOfArray = sum(item)
        averageOfArray = sumOfArray / len(item)
        if averageOfArray <= 150:
            leftTrim = columnIndex
            break
        columnIndex += 1

    croppedImage = rotatedImage[topTrim:(
        height-topTrim), leftTrim:(width-leftTrim)]

    rotatedImage = croppedImage

    rotatedImage = rotatedImage.astype(np.uint8)
    io.imsave(fname=self.fileRotated, arr=rotatedImage)
    self.level = rotatedImage
    print('Rotation image was successfully operated!')

    return None


if __name__ == "__main__":
    pass
