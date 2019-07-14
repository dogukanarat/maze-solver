#!/usr/bin/env python3

import uuid
from .Finder import FindPath, SplitImage
from .Router import FindRoute
from .Transformer import FourPointTransformation
import cv2 as cv


class MazeSolver(object):
    '''
    Definition: This object includes all maze solver functions.\n
    Usage: Object = MazeSolver(IMAGE_FILE, TARGET_DIR, TARGET_NAME)
    '''

    def __init__(self, IMAGE_FILE, TARGET_DIR, TARGET_NAME=False):
        self.uniqueKey = uuid.uuid4().hex[:8].upper()
        self.image = IMAGE_FILE
        self.keyname = ""
        self.level = ""

        if not TARGET_NAME:
            TARGET_NAME = self.uniqueKey

        self.fileRotated = TARGET_DIR + '/' + TARGET_NAME + '-ROTATED.jpg'
        self.fileSkeletone = TARGET_DIR + '/' + TARGET_NAME + '-SKEL.jpg'
        self.fileRoute = TARGET_DIR + '/' + TARGET_NAME + '.csv'
        self.fileCheck = TARGET_DIR + '/' + TARGET_NAME + '-CHECK' + '.jpg'

    FindPath = FindPath
    SplitImage = SplitImage
    FindRoute = FindRoute
    FourPointTransformation = FourPointTransformation

    def ShowResult(self):
        cv.imshow('image', self.level)
        cv.waitKey(0)
        cv.destroyAllWindows()

        return None


if __name__ == "__main__":
    pass
