#!/usr/bin/env python3

from itertools import permutations
import numpy as np


def read_cities(filepath):
  """
  Load a TSP dataset from a CSV file located in /test.
  tiny.csv - 10 cities
  small.csv - 30 cities
  medium.csv - 100 cities
  large.csv - 1000 cities
  the data is formated as a city per line with x,y cords

  Returns:
  cities np array with each city being cords (x,y)

  """
  cities = np.loadtxt(filepath, delimiter=',')
  return cities 

def brute_force_tsm(cities):
  """
  here is where we will brute force the solution
  """
  # init out variables
  best_path =  None # 
  shortest_distance = float("inf")
  indicies = np.arange(1, len(cities))  # we'll force starting at city 0
  for p in permutations(indicies):
    p = [0] + list(p)   # remember, we start at city 0
    ##TODO: calc distance between the vector

if __name__ == '__main__':
    cities = read_cities('../test/tiny.csv')
    brute_force_tsm(cities)


