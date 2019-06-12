#!/usr/bin/env python3

import cv2 as cv
import numpy as np
from skimage import io


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

    rotatedImage = rotatedImage.astype(np.uint8)
    io.imsave(fname=self.fileRotated, arr=rotatedImage)

    print('Rotation image was successfully operated!')


if __name__ == "__main__":
    pass
