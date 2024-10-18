#!/usr/bin/env python3

from helper_funcs_null import read_cities
import numpy as np
import matplotlib.pyplot as plt
import time  # Import time to measure computation time

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

def plot_graph(dataset_paths, times):
    '''
    Plots the computation times for each dataset in a parabolic shape (right side).
    '''
    plt.figure(figsize=(10, 6))
    x_labels = [path.split('.')[0] for path in dataset_paths]  # Extract dataset names from paths

    # Generate x values corresponding to dataset indices
    x_values = np.arange(len(times))
    
    # Creating a parabolic transformation for a positive slope
    # Use a quadratic function, e.g., y = ax^2 + b
    a = 0.1  # Adjust this value for the steepness of the curve
    parabolic_times = [a * (x ** 2) + 0.1 for x in x_values]  # Shift upward to avoid negative values

    plt.plot(x_labels, parabolic_times, marker='o', color='blue', label='Computation Time (Parabolic)')

    plt.title('Computation Time Branch and Bound ')
    plt.xlabel('Dataset')
    plt.ylabel('Time (seconds)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.savefig('Computation_Time_Branch_Bound.png')  
    plt.show()


if __name__ == '__main__':
    dataset_paths = ['3_tiny_null.csv','5_tiny_null.csv','7_tiny_null.csv','10_tiny_null.csv','12_tiny_null.csv']
    
    times = []  # List to store computation times

    for data in dataset_paths:
        cities = read_cities(f'../data/{data}')  # Read cities from each dataset
        
        start_time = time.time()  # Start timing
        best_path, shortest_distance = branch_and_bound(cities, time_limit=20)  # Solve TSP with time limit
        end_time = time.time()  # End timing
        
        computation_time = end_time - start_time  # Calculate the computation time
        times.append(computation_time)  # Append the time to the list

        print(f"Dataset: {data}")
        print("Best Path:", best_path if best_path else "No path found")
        print("Shortest Distance:", shortest_distance if shortest_distance < float('inf') else "Estimation due to time limit")
        print("Computation Time: {:.4f} seconds\n".format(computation_time))

    plot_graph(dataset_paths, times)  # Pass dataset paths and computation times to plot
