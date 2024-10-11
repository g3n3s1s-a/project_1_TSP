#!/usr/bin/env python3

from itertools import permutations
from helper_funcs_null import read_cities,score
import numpy as np

  
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


