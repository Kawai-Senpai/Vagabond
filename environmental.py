from systems import node
from graphviz import Digraph

# This is a class that will be have all the different path finding algorithms
class env:

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

    def __init__(self, get_neighbors_func):
        super().__init__(get_neighbors_func)
        
    def path(self, start_node = None, end_node = None):
        
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
    def __init__(self, get_neighbors_func):
        super().__init__(get_neighbors_func)
        
    def path(self, start_node=None, end_node=None):
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
    def __init__(self, get_neighbors_func):
        super().__init__(get_neighbors_func)
        
    def path(self, start_node=None, end_node=None):
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
    def __init__(self, get_neighbors_func):
        super().__init__(get_neighbors_func)
        
    def path(self, start_node=None, end_node=None):
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
