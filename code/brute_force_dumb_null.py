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

def score(cities,path):
  """
  Calc total distance of the path (circuit)
  returns float
  """

  dist = 0.0

  for i in range(len(path)):
    prev = cities[path[i-1]] # this is ok bc we need a circuit so when i = 0, cities[-1] will get the last element
    curr = cities[path[i]] 
    dist += np.linalg.norm(prev - curr)
  return dist
  
def brute_force_tsp(cities):
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
    dist =  score(cities,p)
    if dist < shortest_distance:
        shortest_distance = dist
        best_path = p
  return best_path,shortest_distance
    

if __name__ == '__main__':
    cities = read_cities('../test/tiny.csv')
    best_path, shortest_distance = brute_force_tsp(cities)
    print(best_path,shortest_distance)


