#!/usr/bin/env python3

from itertools import permutations
from helper_funcs_null import read_cities, score
import numpy as np
import matplotlib.pyplot as plt
import time
import math

def brute_force(nodes, time_limit):
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

def test_and_time(dataset_paths, time_limit=60):
    """
    Tests multiple datasets, times each run with a timeout.
    """
    times = []
    vertices = []
    timeouts = []
    estimated_times = []

    for data in dataset_paths:
        cities = read_cities(f'../test/{data}')
        num_vertices = len(cities)

        # Time the brute force TSP execution
        start_time = time.time()
        best_path, shortest_distance, timeout = brute_force(cities, time_limit)
        elapsed_time = time.time() - start_time

        # Estimate the time for timeout cases
        if timeout:
            num_permutations = math.factorial(num_vertices - 1)
            estimated_time = time_limit / (elapsed_time / num_permutations)
            estimated_times.append(estimated_time / 60)  # Convert to minutes
        else:
            estimated_times.append(elapsed_time / 60)  # Convert to minutes

        # Store the results
        times.append(elapsed_time / 60)  # Convert to minutes
        vertices.append(num_vertices)
        timeouts.append(timeout)

        # Indicate if timeout occurred
        if timeout:
            print(f'Dataset: {data}, Timeout after {time_limit / 60:.2f} minutes, Vertices: {num_vertices}')
        else:
            print(f'Dataset: {data}, Time: {elapsed_time / 60:.2f} minutes, Vertices: {num_vertices}')

    return vertices, times, timeouts, estimated_times

def plot_time_vs_vertices(vertices, times, timeouts, estimated_times, time_limit):
    """
    Plots the number of vertices against the computation time.
    Indicate timeouts on the graph.
    """
    plt.figure(figsize=(10, 6))

    # Initialize flags to track if the labels have been used
    estimated_time_label_used = False
    completed_label_used = False

    # Plot normal points where no timeout occurred
    for i in range(len(vertices)):
        if timeouts[i]:
            if not estimated_time_label_used:
                plt.scatter(vertices[i], estimated_times[i], color='red', marker='x', s=100, label='Estimated Time')
                estimated_time_label_used = True
            else:
                plt.scatter(vertices[i], estimated_times[i], color='red', marker='x', s=100)
        else:
            if not completed_label_used:
                plt.scatter(vertices[i], times[i], color='green', label='Completed')
                completed_label_used = True
            else:
                plt.scatter(vertices[i], times[i], color='green')

    plt.plot(vertices, times, linestyle='-', color='blue', label='Computation Time')

    # Add horizontal line for timeout
    plt.axhline(y=time_limit / 60, color='red', linestyle='dotted', label=f'Timeout Limit ({time_limit / 60:.2f} minutes)')

    plt.xlabel('Number of Vertices')
    plt.ylabel('Computation Time (minutes)')
    plt.title(f'TSP Brute Force: Time vs Number of Vertices (Timeout={time_limit / 60:.2f} minutes)')
    plt.yscale('log')  # Logarithmic scale for y-axis
    plt.grid(True, which='both')  # Grid for both major and minor ticks
    plt.legend()
    plt.xticks(vertices)

    # Save and show the plot
    plt.tight_layout()
    plt.savefig('time_vs_vertices_plot_with_timeout_log.png')

if __name__ == '__main__':
    # List of datasets to test
    dataset_paths = ['tiny.csv', 'small.csv', 'medium.csv']

    # Set a time limit for each dataset (e.g., 60 seconds)
    time_limit = 60  # in seconds

    # Run the tests and time them
    vertices, times, timeouts, estimated_times = test_and_time(dataset_paths, time_limit)

    # Plot the results with timeouts
    plot_time_vs_vertices(vertices, times, timeouts, estimated_times, time_limit)

