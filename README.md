# maze-solver
Maze Solving and Vehicle Routing Algorithm

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.2624203.svg)](https://doi.org/10.5281/zenodo.2624203)
[![Build Status](https://travis-ci.com/ieee-uv-project/maze-solver.svg?branch=master)](https://travis-ci.com/ieee-uv-project/maze-solver)
[<img src="https://img.shields.io/badge/slack-invate%20link-red.svg">](https://join.slack.com/t/uv-project/shared_invite/enQtNTk5MDA0MTE4MjQ1LWJhMjEwMDkyNDhjMDg5MDQ5NDMwZDkxMzg1NDQzMDc1NjYzZmY3MTZhMTdjOTIwN2Y4NmMyYTZlYjcyZTdkZjU)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## application
First, we need to import package
```python
from mazeSolver.core import mazeSolver
```
Then, we will create object while typing maze imaze as param 1 and result folder as param 2
```python
mz = mazeSolver(BASE_DIR + '/contents/no1.png', BASE_DIR + '/results')
```
Finally, we will call function respectively
```python
mz.findPath()
mz.findRoute()
```

## findPath
It solves the given maze image and saves the path in binary format.

## findRoute
It takes the binary image and exacts the path using algorithm, then save it as datafile
