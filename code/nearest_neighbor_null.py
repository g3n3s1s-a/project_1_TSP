import numpy as np
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

if __name__ == '__main__':
    cities = read_cities('../test/tiny.csv')
    best_path, shortest_distance = greedy(cities)
    print(best_path, shortest_distance)

