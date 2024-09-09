import numpy as np
import matplotlib.pyplot as plt
from vagabond.systems import node
from vagabond.environmental import astar
import numpy as np

#example free space grids (1 is free, 0 is occupied)
free_space_grid = np.array([
    [1, 0.8, 0.5, 0.5, 0.8],
    [0.9, 0, 0, 0.8, 0.6],
    [0, 0.8, 0.9, 0.9, 0.9],
    [0.8, 0.9, 0, 0, 0.9],
    [0.6, 0.5, 0.2, 0.2, 1]
])

# Assuming robot_cell is defined
robot_cell = (0, 0)
end_cell = (4, 4)

start_node = node(value=robot_cell, name="({}, {})".format(robot_cell[0], robot_cell[1]))
end_node = node(value=end_cell, name="({}, {})".format(end_cell[0], end_cell[1]))

# Generate a random end cell
map_height, map_width = free_space_grid.shape

#! A* functions ----------------------------------------------------

# if a cell is given, return the 4-connected neighbors
# probability  high -----> cost low -----> high priority
def get_neighbors(parent_node):

    neighbors = []
    x, y = parent_node.value

    # Check if the neighbor is within the map and is free
    if x > 0 and free_space_grid[x - 1,y] != 0:
        neighbors.append(node(value=(x - 1, y), parent=parent_node, cost=(cost(parent_node, (x - 1, y)))+heuristic((x - 1, y), end_cell), name="({}, {})".format(x - 1, y)))
    if x < map_width - 1 and free_space_grid[x + 1,y] != 0:    
        neighbors.append(node(value=(x + 1, y), parent=parent_node, cost=(cost(parent_node, (x + 1, y)))+heuristic((x + 1, y), end_cell), name="({}, {})".format(x + 1, y)))
    if y > 0 and free_space_grid[x, y - 1] != 0:
        neighbors.append(node(value=(x, y - 1), parent=parent_node, cost=(cost(parent_node, (x, y - 1)))+heuristic((x, y - 1), end_cell), name="({}, {})".format(x, y - 1)))
    if y < map_height - 1 and free_space_grid[x, y + 1] != 0:
        neighbors.append(node(value=(x, y + 1), parent=parent_node, cost=(cost(parent_node, (x, y + 1)))+heuristic((x, y + 1), end_cell), name="({}, {})".format(x, y + 1)))

    return neighbors

def cost(current_cell, neighbor):

    if(current_cell.parent):
        parent = current_cell.parent.value
    else:
        parent = current_cell.value

    current = current_cell.value

    #check if direction has not changed
    direction1 = (parent[0] - current[0], parent[1] - current[1])
    direction2 = (current[0] - neighbor[0], current[1] - neighbor[1])

    if direction1 == direction2:
        penalty = 0.1
    else:
        penalty = 0.5

    return penalty + round(1 - free_space_grid[neighbor],2)

def heuristic(current_cell, end_cell):
    return abs(current_cell[0] - end_cell[0]) + abs(current_cell[1] - end_cell[1])

#! A* algorithm ----------------------------------------------------

# Create an instance of the astar class
astar_obj = astar(get_neighbors)

# Find the path
path = astar_obj.path(start_node, end_node)
astar_obj.display_path(filename="astar_path")
print("Path: ", path)

#! Plot the path ----------------------------------------------------

plt.figure()
plt.imshow(free_space_grid, cmap='gray', origin='upper')

# Plot the path as a line
path = np.array(astar_obj.get_raw())

#plot simplified dots
plt.plot(path[:, 1], path[:, 0], 'r')
plt.scatter(robot_cell[1], robot_cell[0], color='r', marker='x')
plt.scatter(end_cell[1], end_cell[0], color='g', marker='x')
plt.show()
