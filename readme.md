# Hexagon

## Overview
Python script to find a solution to the Magic Hexagon (1-19) puzzle.

## Implementation
The approach taken is as follows:
* Try each of the numbers 1-19 in the center.
* Attempt to find 3 sets of 5 numbers that only have one common number (the center)
* Once found, try to fit the remaining 6 pieces into the 6 gaps in the hexagon.
* There are various checkpoints where a potential solution can be abandoned if it won't work.

There are three versions of the script:
* version1: Straight forward solution that tries each center number in turn.
* version2: A multiprocessing version that tries the numbers 1-19 for the center in parallel.
* version3: A modified multiprocessing version that uses a Pool, and has return values from the solve function.


## Installation

Just clone this repository

```bash
$ git clone https://github.com/richardadalton/hexagon.git
```


## Running Hexagon

Run the appropriate script. There are no arguments.  E.g.

```bash
$ python version1.py
```
