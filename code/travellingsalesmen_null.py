#!/usr/bin/env python3

import csv
from itertools import permutations


def read_cities(filepath):
  """
  Load a TSP dataset from a CSV file located in /test.
  tiny.csv - 10 cities
  small.csv - 30 cities
  medium.csv - 100 cities
  large.csv - 1000 cities
  the data is formated as a city per line with x,y cords

  Returns:
  cities list of lists [[x,y],[x,y]...]

  """

  cities = []
  with open(filepath, 'r') as file:
    for line in file:
      x, y = line.strip().split(',')
      cities.append([float(x), float(y)])
  return cities

def brute_force_tsm(cities):
  """
  here is where we will brute force the solution
  """
  # init out variables
  best_path =  None # 
  shortest_distance = float("inf")
  indicies = list(range(1,len(cities)))  # starting at city 0
  for p in permutations(indicies):
    p = [0] + list(p)   # remember, we start at city 0
    ##TODO: calc distance between the vector

if __name__ == '__main__':
    cities = read_cities('../test/tiny.csv')
    brute_force_tsm(cities)


