# Load CSV test cases
import sys
import os
from itertools import permutations
import csv
import time
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


def brute_force(nodes, time_limit=30):
    """
    Brute force TSP solution with a time limit.
    """
    best_path = None
    shortest_distance = float("inf")
    indicies = np.arange(1, len(nodes))  # Force starting at node 0
    start_time = time.time()

    for p in permutations(indicies):
        if time.time() - start_time > time_limit:
            return None, None, True  # Timeout, return without a solution

        p = [0] + list(p)  # Start at node 0
        dist = score(nodes, p)
        if dist < shortest_distance:
            shortest_distance = dist
            best_path = p

    return best_path, shortest_distance, False  # No timeout

def greedy(cities):
    num_cities = len(cities)
    visited = [False]*num_cities
    path = [0]  
    visited[0] = True
    total_distance = 0
    current_city = 0
    
    for _ in range(1, num_cities):
        nearest_city = None
        shortest_distance = float("inf")
        
        # Find the nearest unvisited city
        for city in range(num_cities):
            if not visited[city]:
                dist = score(cities, [current_city, city])
                if dist < shortest_distance:
                    shortest_distance = dist
                    nearest_city = city
        
        # goto the nearest city
        path.append(nearest_city)
        visited[nearest_city] = True
        total_distance += shortest_distance
        current_city = nearest_city
    
    total_distance += score(cities, [current_city, 0])
    path.append(0)
    
    return path, total_distance
def branch_and_bound(cities, time_limit=20):
    '''
    Solves for the TSP using the Branch and Bound method with a time limit.
    '''
    n = len(cities)
    start = 0
    path = None
    best_score = float('inf')
    visited = [False] * n
    visited[start] = True

    start_time = time.time()  # Start timing here

    def explore(curr_path, curr_score):
        nonlocal path, best_score

        # Check if the time limit has been exceeded
        if time.time() - start_time > time_limit:
            return  # Exit if time limit exceeded

        if len(curr_path) == n:
            tot_score = curr_score + np.linalg.norm(cities[curr_path[-1]] - cities[start])
            if tot_score < best_score:
                best_score = tot_score
                path = curr_path + [start]
            return

        for next_city in range(n):
            if not visited[next_city]:
                new_score = curr_score + np.linalg.norm(cities[curr_path[-1]] - cities[next_city])
                if new_score < best_score:
                    visited[next_city] = True
                    explore(curr_path + [next_city], new_score)
                    visited[next_city] = False

    explore([start], 0.0)

    if path is None:
        # If no path was found, return a message or estimate
        return None, float('inf')  # Indicating no path was found

    return path, best_score

test_cases = ['test_cases_1.csv','test_cases_2.csv','test_cases_3.csv','test_cases_4.csv','test_cases_5.csv']

for i,cities in enumerate(test_cases):
  print(cities)
  print()
  print('brute force test')
  nodes = read_cities(cities)
  path,distance,_ = brute_force(nodes)
  print(f'Estimated path: {path} with distance: {distance}')
  print()
  print('branch and bound')
  path,distance = branch_and_bound(nodes)
  print(f'Estimated path: {path} with distance: {distance}')
  print()










