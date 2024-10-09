#!/usr/bin/env python3

import numpy as np


def read_cities(filepath):
    """
    Load a TSP dataset from a CSV file.

    Returns:
    cities (np.ndarray): NumPy array of city coordinates.

    """
    
    cities = np.loadtxt(filepath, delimiter=',')
    return cities

if __name__ == '__main__':
    cities = read_cities('../test/tiny.csv')

