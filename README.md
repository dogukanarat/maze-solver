# maze-solver
Maze Solving and Vehicle Routing Algorithm

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.2624203.svg)](https://doi.org/10.5281/zenodo.2624203)
[![Build Status](https://travis-ci.com/ieee-uv-project/maze-solver.svg?branch=master)](https://travis-ci.com/ieee-uv-project/maze-solver)
[<img src="https://img.shields.io/badge/slack-invate%20link-red.svg">](https://join.slack.com/t/uv-project/shared_invite/enQtNTk5MDA0MTE4MjQ1LWJhMjEwMDkyNDhjMDg5MDQ5NDMwZDkxMzg1NDQzMDc1NjYzZmY3MTZhMTdjOTIwN2Y4NmMyYTZlYjcyZTdkZjU)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## application
First, we need to import package
```python
from modules.MazeSolver import MazeSolver
```
Then, we will create object while typing maze imaze as param 1 and result folder as param 2
```python
# call the object defining the maze image
mz = MazeSolver(BASE_DIR + '/contents/no4.png',
                 BASE_DIR + '/results', "RESULTFILE")
```
Finally, we will call function respectively
```python
mz.FourPointTransformation()  # rotating the image for operation
mz.ShowResult() # showing result image
mz.FindPath()  # finding the path ino the maze image
mz.ShowResult() # showing result image
mz.FindRoute()  # finding the route in the maze image
mz.ShowResult() # showing result image
```

## FourPointTransformation()
It transform the image, which was naturally tilted due to camera angle, to proper image for algorithm

## FindPath()
It solves the given maze image and saves the path in binary format.

## FindRoute()
It takes the binary image and exacts the path using algorithm, then save it as datafile

## ShowResult()
It shows the previous process result
