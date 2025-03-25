# Introduction

This folder provides the data and code to generate the tile grid visualization for the US.

The goal is to visualize data in each US state and place the states in a grid layout that roughly mimics the US map.

## Code

- [us_tile_grid_coordinates.ipynb](us_tile_grid_coordinates.ipynb): contains the code to generate the coordinates for each state in the grid.

## Coordinates

[us_tile_grid_coordinates.json](us_tile_grid_coordinates.json) contains the coordinates for each state in the grid, which contains the following information

| Column | Value type | Description |
|--------|-------------|-------------|
| state  | key | Two-letter state abbreviation in the US |
| row    | value | Row number in the grid (0-6) |
| col    | value | Column number in the grid (0-10) |
