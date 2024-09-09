from systems import node
from graphviz import Digraph

# This is a class that will be have all the different path finding algorithms
class env:
    
    """
    A class representing an environment.
    Attributes:
    - get_neighbors (function): A function that returns the neighbors of a node.
    - path (list): A list representing the path in the environment.
    Methods:
    - __init__(get_neighbors_func): Initializes the environment with the given get_neighbors function.
    - __getitem__(index): Returns the node at the specified index in the path.
    - __len__(): Returns the length of the path.
    - __repr__(): Returns a string representation of the path.
    - __str__(): Returns a string representation of the path.
    - __iter__(): Returns an iterator for the path.
    - get(): Returns the path as a list of nodes.
    - add(node): Adds a node to the path.
    - remove(node): Removes a node from the path.
    - clear(): Clears the path.
    - get_raw(): Returns an array of values from the path.
    - display_path(filename='graph', directory='.'): Displays the path in a graph and saves it as a PNG file.
    """

    #Functions -- Important Functions
    get_neighbors = None

    #Other Variables
    path = []

    #Constructor
    def __init__(self, get_neighbors_func):
        self.get_neighbors = get_neighbors_func
    
        if not self.get_neighbors:
            raise ValueError("get_neighbors function is not defined")

    # Get a node from the path
    def __getitem__(self, index):
        try:
            return self.path[index]
        except IndexError:
            raise IndexError("Index out of range") from None

    # Get the length of the path
    def __len__(self):
        return len(self.path)
    
    # Print the path
    def __repr__(self):
        return str(self.path)
    
    # Print the path
    def __str__(self):
        return str(self.path)
    
    # Make it iterable
    def __iter__(self):
        return iter(self.path)
    
    # Get the path as a list of nodes
    def get(self):
        return self.path
    
    #Add a node to the path
    def add(self, node):
        if not isinstance(node, node):
            raise TypeError("node must be an instance of the node class. Got '{}' instead".format(type(node)))
        self.path.append(node)

    # Remove a node from the path
    def remove(self, node):
        if not isinstance(node, node):
            raise TypeError("node must be an instance of the node class. Got '{}' instead".format(type(node)))
        self.path.remove(node)

    # Clear the path
    def clear(self):
        self.path = []
    
    # Get array of values from the path
    def get_raw(self):
        if self.path == []:
            return []
        else:
            return [node.value for node in self.path]

    # display the path in a graph
    def display_path(self, filename='graph', directory='.'):

        """
        Display the path as a graph.
        Args:
            filename (str, optional): The name of the file to save the graph as. Defaults to 'graph'.
            directory (str, optional): The directory to save the graph in. Defaults to '.'.
        Returns:
            dot: The graph object.
        Raises:
            ValueError: If the path is empty.
        """

        if not self.path:
            raise ValueError("Path is empty. Cannot display graph.")

        dot = Digraph()
        dot.node_attr.update(shape='rectangle')

        for node in self.path:
            make_str = "Node: " + node.name
            if node.value is not None:
                make_str += "\n----------\nValue: \n" + str(node.value)
            dot.node(node.name, label=make_str)

            if node.parent:
                dot.edge(node.parent.name, node.name)

        filepath = f"{directory}/{filename}"
        dot.render(filepath, format='png', view=True)
        print(f"Graph saved as '{filename}.png' in directory '{directory}'")
        return dot

class astar(env):

    """
    A* algorithm implementation for pathfinding in a graph.
    Args:
        get_neighbors_func (function): A function that returns the neighbors of a given node.
    Attributes:
        path (list): The path found by the A* algorithm.
    Methods:
        path(start_node, end_node): Finds the shortest path from start_node to end_node using the A* algorithm.
    """
    
    """
    Initializes the A* algorithm.
    Args:
        get_neighbors_func (function): A function that returns the neighbors of a given node.
    """
    """
    Finds the shortest path from start_node to end_node using the A* algorithm.
    Args:
        start_node (node): The starting node of the path.
        end_node (node): The end node of the path.
    Returns:
        list: The shortest path from start_node to end_node.
    Raises:
        TypeError: If start_node or end_node is not an instance of the node class.
        ValueError: If start_node or end_node is not defined.
    """

    def __init__(self, get_neighbors_func):
        super().__init__(get_neighbors_func)
        
    def path(self, start_node = None, end_node = None):

        """
        Finds the shortest path between two nodes in the graph.
        Parameters:
            start_node (node): The starting node of the path.
            end_node (node): The ending node of the path.
        Returns:
            list: The shortest path as a list of nodes.
        Raises:
            TypeError: If start_node or end_node is not an instance of the node class.
            ValueError: If start_node or end_node is not defined.
        """
        
        if start_node is not None:
            if not isinstance(start_node, node):
                raise TypeError("start_node must be an instance of the node class. Got '{}' instead".format(type(start_node)))
        else:
            raise ValueError("start_node is not defined")
        
        if end_node is not None:
            if not isinstance(end_node, node):
                raise TypeError("end_node must be an instance of the node class. Got '{}' instead".format(type(end_node)))
        else:
            raise ValueError("end_node is not defined")
        
        unvisited = []
        visited = []

        # Add the start node to the unvisited list
        unvisited.append(start_node)

        while unvisited:

            # Get the node with the minimum cost
            current_node = min(unvisited, key=lambda x: x.cost)

            # Remove the current node from the unvisited list
            unvisited.remove(current_node)

            # Add the current node to the visited list
            visited.append(current_node)

            # Check if the current node is the end node
            if current_node == end_node:
                path = []
                while current_node:
                    path.append(current_node)
                    current_node = current_node.parent

                self.path = path[::-1]
                return self.path

            # Get the neighbors of the current node
            neighbors = self.get_neighbors(current_node)

            # Loop through the neighbors
            for neighbor_node in neighbors:
                
                # Check if the neighbor is in the visited list
                if neighbor_node in visited:
                    continue

                # Check if the neighbor is in the unvisited list
                if neighbor_node not in unvisited:
                    unvisited.append(neighbor_node)
                else:
                    # Replace the neighbor node with the new node if the new node has a lower cost
                    for i, node_ in enumerate(unvisited):
                        if node_ == neighbor_node and node_.cost > neighbor_node.cost:
                            unvisited[i] = neighbor_node
        return None

class bfs(env):

    """
    Initializes a breadth-first search algorithm.
    Parameters:
    - get_neighbors_func: A function that takes a node as input and returns a list of its neighboring nodes.
    """
    """
    Finds the shortest path from start_node to end_node using breadth-first search algorithm.
    Parameters:
    - start_node: The starting node of the path. Must be an instance of the node class.
    - end_node: The ending node of the path. Must be an instance of the node class.
    Returns:
    - path: A list of nodes representing the shortest path from start_node to end_node.
        Returns None if no path is found.
    """

    def __init__(self, get_neighbors_func):
        super().__init__(get_neighbors_func)
        
    def path(self, start_node=None, end_node=None):

        """
        Finds the path from start_node to end_node using breadth-first search algorithm.
        Args:
            start_node (node, optional): The starting node. Defaults to None.
            end_node (node, optional): The target node. Defaults to None.
        Raises:
            TypeError: If start_node or end_node is not an instance of the node class.
            ValueError: If start_node or end_node is not defined.
        Returns:
            list: The path from start_node to end_node, represented as a list of nodes.
                Returns None if no path is found.
        """

        if start_node is not None:
            if not isinstance(start_node, node):
                raise TypeError("start_node must be an instance of the node class. Got '{}' instead".format(type(start_node)))
        else:
            raise ValueError("start_node is not defined")
        
        if end_node is not None:
            if not isinstance(end_node, node):
                raise TypeError("end_node must be an instance of the node class. Got '{}' instead".format(type(end_node)))
        else:
            raise ValueError("end_node is not defined")
        
        queue = [start_node]
        visited = set()
        parent_map = {start_node: None}

        while queue:
            current_node = queue.pop(0)
            if current_node == end_node:
                path = []
                while current_node:
                    path.append(current_node)
                    current_node = parent_map[current_node]
                self.path = path[::-1]
                return self.path
            
            visited.add(current_node)
            neighbors = self.get_neighbors(current_node)
            for neighbor in neighbors:
                if neighbor not in visited and neighbor not in queue:
                    parent_map[neighbor] = current_node
                    queue.append(neighbor)
        return None

class dfs(env):

    """
    Initializes a depth-first search algorithm.
    Parameters:
    - get_neighbors_func: A function that returns the neighbors of a given node.
    Returns:
    None
    """
    """
    Finds a path from the start node to the end node using depth-first search.
    Parameters:
    - start_node: The starting node of the path. Must be an instance of the node class.
    - end_node: The ending node of the path. Must be an instance of the node class.
    Returns:
    - path: A list of nodes representing the path from the start node to the end node.
        Returns None if no path is found.
    """

    def __init__(self, get_neighbors_func):
        super().__init__(get_neighbors_func)
        
    def path(self, start_node=None, end_node=None):

        """
        Finds a path from the start_node to the end_node using a depth-first search algorithm.
        Args:
            start_node (node): The starting node of the path.
            end_node (node): The target node to reach.
        Returns:
            list: A list of nodes representing the path from start_node to end_node, 
                or None if no path is found.
        Raises:
            TypeError: If start_node or end_node is not an instance of the node class.
            ValueError: If start_node or end_node is not defined.
        """

        if start_node is not None:
            if not isinstance(start_node, node):
                raise TypeError("start_node must be an instance of the node class. Got '{}' instead".format(type(start_node)))
        else:
            raise ValueError("start_node is not defined")
        
        if end_node is not None:
            if not isinstance(end_node, node):
                raise TypeError("end_node must be an instance of the node class. Got '{}' instead".format(type(end_node)))
        else:
            raise ValueError("end_node is not defined")
        
        stack = [start_node]
        visited = set()
        parent_map = {start_node: None}

        while stack:
            current_node = stack.pop()
            if current_node == end_node:
                path = []
                while current_node:
                    path.append(current_node)
                    current_node = parent_map[current_node]
                self.path = path[::-1]
                return self.path
            
            visited.add(current_node)
            neighbors = self.get_neighbors(current_node)
            for neighbor in neighbors:
                if neighbor not in visited and neighbor not in stack:
                    parent_map[neighbor] = current_node
                    stack.append(neighbor)
        return None

class dijkstra(env):

    """
    Initializes a Dijkstra object.
    Parameters:
    - get_neighbors_func (function): A function that returns the neighbors of a given node.
    Returns:
    - None
    """
    """
    Finds the shortest path between two nodes using Dijkstra's algorithm.
    Parameters:
    - start_node (node): The starting node of the path.
    - end_node (node): The ending node of the path.
    Returns:
    - list: The shortest path from start_node to end_node, represented as a list of nodes.
    - None: If no path is found.
    """

    def __init__(self, get_neighbors_func):
        super().__init__(get_neighbors_func)
        
    def path(self, start_node=None, end_node=None):
        
        """
        Finds the shortest path between two nodes in the graph.
        Args:
            start_node (node): The starting node of the path.
            end_node (node): The ending node of the path.
        Returns:
            list: The shortest path as a list of nodes.
        Raises:
            TypeError: If start_node or end_node is not an instance of the node class.
            ValueError: If start_node or end_node is not defined.
        """
        
        if start_node:
            if not isinstance(start_node, node):
                raise TypeError("start_node must be an instance of the node class. Got '{}' instead".format(type(start_node)))
        else:
            raise ValueError("start_node is not defined")
        
        if end_node:
            if not isinstance(end_node, node):
                raise TypeError("end_node must be an instance of the node class. Got '{}' instead".format(type(end_node)))
        else:
            raise ValueError("end_node is not defined")
        
        unvisited = []
        visited = []
        start_node.cost = 0
        unvisited.append(start_node)

        while unvisited:
            current_node = min(unvisited, key=lambda x: x.cost)
            unvisited.remove(current_node)
            visited.append(current_node)

            if current_node == end_node:
                path = []
                while current_node:
                    path.append(current_node)
                    current_node = current_node.parent
                self.path = path[::-1]
                return self.path

            neighbors = self.get_neighbors(current_node)
            for neighbor in neighbors:
                if neighbor in visited:
                    continue
                new_cost = current_node.cost + neighbor.cost
                if neighbor not in unvisited or new_cost < neighbor.cost:
                    neighbor.cost = new_cost
                    neighbor.parent = current_node
                    if neighbor not in unvisited:
                        unvisited.append(neighbor)
        return None
