import matplotlib.pyplot as plt
import numpy as np

def display_grid_graphically(taxi_pos, passengers, bushes):
    grid_size = 15
    grid = np.zeros((grid_size, grid_size, 3))

    # Set colors for elements
    for x in range(grid_size):
        for y in range(grid_size):
            if (x + 1, y + 1) == taxi_pos:
                grid[y, x] = [1, 1, 0]
            elif (x + 1, y + 1) in passengers:
                grid[y, x] = [0, 0, 1]
            elif (x + 1, y + 1) in bushes:
                grid[y, x] = [0, 1, 0]
            elif (x + 1, y + 1) in dropoff_positions:
                grid[y,x] = [0,0,0]
            else:
                grid[y, x] = [1, 1, 1]

    plt.imshow(grid, interpolation='nearest')
    plt.xticks(ticks=np.arange(grid_size), labels=np.arange(1, grid_size + 1))
    plt.yticks(ticks=np.arange(grid_size), labels=np.arange(1, grid_size + 1))
    plt.grid(False)
    plt.show()

# Initial setup
taxi_position = (5, 8)  # Taxi starts at (1, 1)
passenger_positions = [(8,7), (14,3), (5,12)]  # Passengers' initial positions
dropoff_positions = [(11,3), (1,6), (8,6)]
bush_positions = [(3,4), (3,3), (4,4), (4,3), (5,10), (5,11), (6,10), (6,11)]  # Bush positions

# Display the grid graphically
display_grid_graphically(taxi_position, passenger_positions, bush_positions)