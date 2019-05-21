#!/usr/bin/env python3
__author__ = "dogukanarat"

import uuid
import mazesolver.finder as finder
import  mazesolver.router as router

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

    findPath = finder.find_path
    findRoute = router.find_route

if __name__ == "__main__":
    pass
