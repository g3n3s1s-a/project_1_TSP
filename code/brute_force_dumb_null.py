#!/usr/bin/env python3

from itertools import permutations
from helper_funcs_null import read_cities,score
import numpy as np
import matplotlib.pyplot as plt
import time

def brute_force(nodes):
  """
  here is where we will brute force the solution
  """
  # init out variables
  best_path =  None # 
  shortest_distance = float("inf")
  indicies = np.arange(1, len(nodes))  # we'll force starting at node 0
  for p in permutations(indicies):
    p = [0] + list(p)   # remember, we start at node 0
    dist =  score(nodes,p)
    if dist < shortest_distance:
        shortest_distance = dist
        best_path = p
  return best_path,shortest_distance

def graph(nodes,best_path,shortest_distance,data,algo,start=0):
    order = np.array(best_path) # this are the indicies of the cities

    # Reorder points based on the specified order
    ordered_points = nodes[order]
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
def test_and_time(dataset_paths):
    """
    Tests multiple datasets, times each run, and returns the results.
    """
    times = []
    vertices = []

    for data in dataset_paths:
        cities = read_cities(f'../test/{data}')
        num_vertices = len(cities)

        # Time the brute force TSP execution
        start_time = time.time()
        best_path, shortest_distance = brute_force(cities)
        elapsed_time = time.time() - start_time

        # Store the results
        times.append(elapsed_time)
        vertices.append(num_vertices)

        # Optionally, plot the path for each dataset
        graph(cities, best_path, shortest_distance, data, "brute force")
        print(f'Dataset: {data}, Time: {elapsed_time:.2f} seconds, Vertices: {num_vertices}')

    return vertices, times

def plot_time_vs_vertices(vertices, times):
    """
    Plots the number of vertices against the computation time.
    """
    plt.figure()
    plt.plot(vertices, times, marker='o', linestyle='-', color='green')
    plt.xlabel('Number of Vertices')
    plt.ylabel('Computation Time (seconds)')
    plt.title('TSP Brute Force: Time vs Number of Vertices')
    plt.grid(True)
    plt.savefig('time_vs_vertices_plot.png')
    plt.show()



if __name__ == '__main__':
    #data = 'tiny.csv'
    #nodes = read_cities(f'../test/{data}')
    #best_path, shortest_distance = brute_force(nodes)
    #graph(nodes,best_path,shortest_distance,data,"brute force")
    # List of datasets to test
    dataset_paths = ['tiny.csv', 'small.csv', 'medium.csv']

    # Run the tests and time them
    vertices, times = test_and_time(dataset_paths)

    # Plot the results
    plot_time_vs_vertices(vertices, times)


