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


def graph(cities, best_path, shortest_distance, data, start=0):
    order = np.array(best_path)  # These are the indices of the cities

    # Reorder points based on the specified order
    ordered_points = cities[order]

    # Add the starting city to the end to complete the circuit
    ordered_points = np.vstack([ordered_points, ordered_points[start]])

    x = ordered_points[:, 0]
    y = ordered_points[:, 1]

    # Create the plot
    plt.figure(figsize=(8, 6))

    # Plot the path with markers and arrows for clarity
    plt.plot(x, y, marker='o', markersize=8, color='blue', linestyle='-', label=f'Total Distance: {round(shortest_distance, 2)}')

    # Add direction arrows
    for i in range(len(x) - 1):
        plt.annotate('', xy=(x[i + 1], y[i + 1]), xytext=(x[i], y[i]),
                     arrowprops=dict(facecolor='black', arrowstyle='->'))

    # Add city labels
    for i, (x_coord, y_coord) in enumerate(zip(x, y)):
        plt.text(x_coord, y_coord, f'{i}', fontsize=12, ha='right')

    # Add labels and title
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.title(f'nearest_neighbor: {data} Path')
    plt.legend()

    # Save the plot to a file
    name, _ = data.split('.')
    plt.savefig(f'../output/nearest_neighbor_{name}_matplotlib.png')

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

def graph_all(dataset_paths, times, distances, paths):
    for dataset, time, distance, path in zip(dataset_paths, times, distances, paths):
        cities = read_cities(f'../data/{dataset}')
        graph(cities, path, distance, dataset, start=0)

if __name__ == '__main__':
    dataset_paths = ['10_tiny_null.csv', '30_small_null.csv', '50_medium_null.csv', '100_medium_null.csv','120_large_null.csv'] 
    times, distances, paths = test_and_time(dataset_paths)
    graph_all(dataset_paths, times, distances, paths)
    times = np.array(times)
    vertices = np.array([10, 30, 50, 100, 120])
    plt.plot(vertices, times, marker='o')
    plt.savefig('../graphs/nearest_neighbor_graph_null.png')
    plt.show()
    print('done')
