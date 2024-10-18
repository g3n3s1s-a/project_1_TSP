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
    plt.title(f'nearest_neighbor: {data} Path')
    plt.legend()

    # Save the plot to a file
    name, _ = data.split('.')
    plt.savefig(f'../output/nearest_neighbor_{name}_matplotlib.png')

def test_and_time(dataset_paths, vertices):
    times = []
    paths = []
    distances = []

    for data, vertex_count in zip(dataset_paths, vertices):
        cities = read_cities(f'../data/{data}')
        num_vertices = len(cities)

        start_time = time.time()
        path, total_distance = greedy(cities)

        elapsed_time = time.time() - start_time

        times.append(elapsed_time)
        paths.append(path)
        distances.append(total_distance)

        print(f"{data} has {vertex_count} vertices. Completed Greedy Nearest Neighbor Algorithm in {1000 * elapsed_time:.3f} miliseconds, resulting in a distance of {total_distance:.2f}")

    return times, distances, paths

def graph_all(dataset_paths, times, distances, paths):
    for dataset, time, distance, path in zip(dataset_paths, times, distances, paths):
        cities = read_cities(f'../data/{dataset}')
        graph(cities, path, distance, dataset, start=0)

if __name__ == '__main__':
    vertices = [3, 10, 30, 50, 100, 120]
    dataset_paths = ['3_tiny_null.csv', '10_tiny_null.csv', '30_small_null.csv', '50_medium_null.csv', '100_medium_null.csv','120_large_null.csv'] 
    times, distances, paths = test_and_time(dataset_paths, vertices)

    # graph the actual outputs
    graph_all(dataset_paths, times, distances, paths)

    # graph the computation time vs the number of vertices
    plt.figure(figsize=(8, 6))
    vertices = np.array(vertices)
    plt.plot(vertices, times, marker='o')
    plt.title('Greedy/Nearest-Neighbor Algorithm: Computation Time vs Vertex Count for TSP')
    plt.xlabel('vertex count')
    plt.ylabel('computation time (seconds)')
    plt.savefig('../graphs/nearest_neighbor_timeGraph_null.png')
    plt.show()
    print('done')
