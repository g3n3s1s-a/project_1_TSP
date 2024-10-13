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

def graph(cities,best_path,shortest_distance,data,algo,start=0):
    order = np.array(best_path) # this are the indicies of the cities

    # Reorder points based on the specified order
    ordered_points = cities[order]
    # Add the starting city to the end to complete the circuit
    ordered_points = np.vstack([ordered_points, ordered_points[start]])

    x = ordered_points[:,0]
    y = ordered_points[:,1]

    #Create the plot
    plt.plot(x, y, marker='o', linestyle='-', color='blue', label=f'Total Distance : {round(shortest_distance,2)}')
    #Add labels and title
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.title(f'{algo} : {data} path')
    plt.legend()

    # Save the plot to a file
    name,_ = data.split('.')
    plt.savefig(f'{algo}_{name}_plot.png')


if __name__ == '__main__':
    data = 'tiny.csv'
    cities = read_cities(f'../test/{data}')
    best_path, shortest_distance = brute_force_tsp(cities)
    graph(cities,best_path,shortest_distance,data,"brute force")
    print(best_path,shortest_distance)


