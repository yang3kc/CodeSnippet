"""
Create a tile grid visualization of US states.

This module provides functionality to create a grid-based visualization where each US state
is represented as a tile positioned to roughly approximate the geographic layout of the United States.

The coordinates for each state's position in the grid are loaded from 'us_tile_grid_coordinates.json',
which contains the row and column indices for each state's tile.
"""

import numpy as np
import matplotlib.pyplot as plt
import json

with open("us_tile_grid_coordinates.json", "r") as f:
    us_tile_grid_coordinates = json.load(f)


# Grid dimensions
n_rows = max(coord["row"] for coord in us_tile_grid_coordinates.values()) + 1
n_cols = max(coord["col"] for coord in us_tile_grid_coordinates.values()) + 1

# Create the figure
fig = plt.figure(figsize=(n_cols * 2.5, n_rows * 2.5))  # Adjust figsize as needed

# Dictionary to hold the axes objects, keyed by state
axs = {}

# Iterate through the state locations and create subplots
for state, coord in us_tile_grid_coordinates.items():
    row = coord["row"]
    col = coord["col"]
    ax = fig.add_subplot(n_rows, n_cols, row * n_cols + col + 1)
    axs[state] = ax

    # Add your plots here
    plt.plot(np.random.randn(10))
    plt.title(state)

plt.tight_layout(
    rect=[0, 0, 1, 0.96]
)  # Adjust layout to prevent overlap, leave space for title
plt.show()
