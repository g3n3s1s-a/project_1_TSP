#!/usr/bin/env python3

from itertools import permutations
from helper_funcs_null import read_cities,score
import numpy as np
import matplotlib.pyplot as plt

  
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
    dist =  score(cities,p)
    if dist < shortest_distance:
        shortest_distance = dist
        best_path = p
  return best_path,shortest_distance

def graph(cities,best_path,shortest_distance):
    order = np.array(best_path) # this are the indicies of the cities

    # Reorder points based on the specified order
    ordered_points = cities[order]
    
    x = ordered_points[:,0]
    y = ordered_points[:,1]
    
    # Create the plot
    plt.plot(x, y, marker='o', linestyle='-', color='blue', label='Ordered Path')
    # Add labels and title
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.title('Plot of Points in Custom Order')
    plt.legend()

    # Save the plot to a file
    plt.savefig('custom_order_plot.png')
    

if __name__ == '__main__':
    cities = read_cities('../test/tiny.csv')
    best_path, shortest_distance = brute_force_tsp(cities)
    graph(cities,best_path,shortest_distance)
    print(best_path,shortest_distance)


