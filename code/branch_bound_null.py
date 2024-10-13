#!/usr/bin/env python3

from helper_funcs_null import read_cities
import numpy as np
import matplotlib.pyplot as plt

def branch_and_bound(cities):
    '''
    Solves for the TSP using the Branch and Bound method.
    '''
    n = len(cities)
    start = 0  
    path = None
    best_score = float('inf')
    visited = [False] * n
    visited[start] = True  

    def explore(curr_path, curr_score):
        nonlocal path, best_score 

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
    return path, best_score

def plot_graph(cities, path):
    '''
    Plots the cities and the path taken.
    '''
    plt.figure(figsize=(10, 6))
    plt.scatter(cities[:, 0], cities[:, 1], color='red', label='Cities', s=100)

    for i in range(len(path) - 1):
        plt.plot(
            [cities[path[i], 0], cities[path[i + 1], 0]], 
            [cities[path[i], 1], cities[path[i + 1], 1]], 
            color='blue'
        )

    plt.scatter(cities[path[0], 0], cities[path[0], 1], color='green', label='Start', s=150, marker='*')
    plt.title('Traveling Salesman Problem Path')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.legend()
    plt.grid()
    plt.savefig('Branch & Bound.png')  
    plt.show() 

if __name__ == '__main__':
    data = 'tiny.csv'
    cities = read_cities(f'../test/{data}')
    best_path, shortest_distance = branch_and_bound(cities)
    plot_graph(cities, best_path)
    print("Best Path:", best_path)
    print("Shortest Distance:", shortest_distance)
