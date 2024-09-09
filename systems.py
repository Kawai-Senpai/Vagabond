
class node:

    childs = []
    parent = None
    cost = 0
    name = ""
    value = None

    #Constructor
    def __init__(self, value=None, childs=[], parent=None, cost=0, name=None):

        self.childs = childs
        self.value = value
        self.name = name
        self.parent = parent
        self.cost = cost

    #print function / string representation
    def __repr__(self) -> str:

        if(self.name):
            return self.name
        else:
            try:
                return str(self.value)
            except:
                return "un-named node"
        
    #equality function
    def __eq__(self, o: object) -> bool:
        return self.value == o.value
    
    # Addition operation - add node b as a child to node a
    def __add__(self, b):
        if isinstance(b, node):
            self.childs.append(b)
            return self
        else:
            raise TypeError("unsupported operand type(s) for +: '{}' and '{}'".format(type(self), type(b)))
        
    # Reverse addition operation - add node a as a child to node b
    def __radd__(self, a):
        if isinstance(a, node):
            a.childs.append(self)
            return a
        else:
            raise TypeError("unsupported operand type(s) for +: '{}' and '{}'".format(type(a), type(self)))
        
    # Subtraction operation - remove node b from the child list of node a
    def __sub__(self, b):
        if isinstance(b, node):
            if b in self.childs:
                self.childs.remove(b)
                return self
            else:
                raise ValueError("node '{}' is not a child of '{}'".format(b.name, self.name))
        else:
            raise TypeError("unsupported operand type(s) for -: '{}' and '{}'".format(type(self), type(b)))
    
    # Subtraction operation - remove node b from the child list of node a
    def __rsub__(self, a):
        if isinstance(a, node):
            if a in self.childs:
                self.childs.remove(a)
                return a
            else:
                raise ValueError("node '{}' is not a child of '{}'".format(a.name, self.name))
        else:
            raise TypeError("unsupported operand type(s) for -: '{}' and '{}'".format(type(a), type(self)))

    # Make it hashable
    def __hash__(self):
        return hash(self.value)
    
    # Add a child to the node
    def add_child(self, child):
        if not isinstance(child, node):
            raise TypeError("child must be an instance of the node class. Got '{}' instead".format(type(child)))
        self.childs.append(child)

    # Remove a child from the node
    def remove_child(self, child):
        if not isinstance(child, node):
            raise TypeError("child must be an instance of the node class. Got '{}' instead".format(type(child)))
        self.childs.remove(child)

    # Clear the children list
    def clear(self):
        self.childs = []

    # Get the children list
    def get_children(self):
        return self.childs
    
    # Get the parent node
    def get_parent(self):
        return self.parent
    
    # Set the parent node
    def set_parent(self, parent):
        if not isinstance(parent, node):
            raise TypeError("parent must be an instance of the node class. Got '{}' instead".format(type(parent)))
        self.parent = parent

    # Get the cost of the node
    def get_cost(self):
        return self.cost
    
    # Set the cost of the node
    def set_cost(self, cost):
        self.cost = cost

    # Get the name of the node
    def get_name(self):
        return self.name
    
    # Set the name of the node
    def set_name(self, name):
        self.name = name

    # Get the value of the node
    def get_value(self):
        return self.value
    
    # Set the value of the node
    def set_value(self, value):
        self.value = value
