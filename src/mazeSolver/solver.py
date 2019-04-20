#!/usr/bin/env python3
__author__ = "dogukanarat"

import uuid
from mazeSolver.finder import find_path, split_image
from mazeSolver.router import find_route 

class mazeSolver(object):
    
    def __init__(self, image, TARGET_DIR, TARGET_NAME = False):
        self.uniqueKey = uuid.uuid4().hex[:8].upper()
        self.image = image
        self.keyname = ""

        if not TARGET_NAME:
            TARGET_NAME = self.uniqueKey
        
        self.fileSkel = TARGET_DIR + '/' + TARGET_NAME + '-SKEL.jpg'
        self.fileRoute = TARGET_DIR + '/' + TARGET_NAME + '.csv'
        self.fileCheck = TARGET_DIR + '/' + TARGET_NAME + '-CHECK' + '.jpg'

    findPath = find_path
    findRoute = find_route

if __name__ == "__main__":
    pass
