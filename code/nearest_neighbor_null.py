#!/usr/bin/env python3

import time
import numpy as np
import matplotlib.pyplot as plt
from helper_funcs_null import read_cities, score


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


def test_and_time(dataset_paths):
    times = []
    paths = []
    distances = []

    for data in dataset_paths:
        cities = read_cities(f'../data/{data}')
        num_vertices = len(cities)

        start_time = time.time()
        path, total_distance = greedy(cities)

        elapsed_time = time.time() - start_time

        time_in_minutes = elapsed_time / 60
        times.append(time_in_minutes)
        paths.append(path)
        distances.append(total_distance)

    return times, distances, paths

if __name__ == '__main__':
    dataset_paths = ['10_tiny_null.csv', '30_small_null.csv', '50_medium_null.csv', '100_medium_null.csv','120_large_null.csv'] 
    times, distances, paths = test_and_time(dataset_paths)
    times = np.array(times)
    vertices = np.array([10, 30, 50, 100, 120])
    plt.plot(vertices, times, marker='o')
    plt.savefig('../output/nearest_neighbor_graph_null.png')
    plt.show()
    print('done')
