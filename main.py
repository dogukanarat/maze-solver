#!/usr/bin/env python3
__author__ = "dogukanarat"

import os
import operations.finder
import operations.router
import warnings

warnings.filterwarnings("ignore")

# defining file path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    operations.finder.find_path(
        BASE_DIR + '/contents/no1.png', BASE_DIR + '/skeleton.jpg')
    operations.router.find_route(
        BASE_DIR + '/skeleton.jpg', BASE_DIR + '/route.out')
