#!/usr/bin/env python3
__author__ = "dogukanarat"

import os
import operations.finder
import operations.router
import warnings
import uuid

warnings.filterwarnings("ignore")

# defining file path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def operate(maze_image):

    unique_key = uuid.uuid4().hex[:8].upper()
    target_dir = "/results"

    skel_file  = BASE_DIR + target_dir + '/' + unique_key + '.jpg'
    route_file = BASE_DIR + target_dir + '/' + unique_key + '.csv'
    check_file = BASE_DIR + target_dir + '/' + unique_key + '-CHECK' + '.jpg'

    operations.finder.find_path(maze_image, skel_file)
    operations.router.find_route(skel_file, route_file, check_file)

    return 0

if __name__ == '__main__':
    operate(BASE_DIR + '/contents/no1.png')
