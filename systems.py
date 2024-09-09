class node:

    """
    A class representing a node in a tree structure.

    Attributes:
    - value: The value associated with the node.
    - childs: A list of child nodes.
    - parent: The parent node.
    - cost: The cost associated with the node.
    - name: The name of the node.

    Methods:
    - __init__(self, value=None, childs=[], parent=None, cost=0, name=None): Initializes a node object.
    - __repr__(self) -> str: Returns a string representation of the node.
    - __eq__(self, o: object) -> bool: Checks if two nodes are equal.
    - __add__(self, b): Adds a node as a child to the current node.
    - __radd__(self, a): Adds the current node as a child to another node.
    - __sub__(self, b): Removes a child node from the current node.
    - __rsub__(self, a): Removes the current node from the child list of another node.
    - __hash__(self): Makes the node hashable.
    - add_child(self, child): Adds a child node to the current node.
    - remove_child(self, child): Removes a child node from the current node.
    - clear(self): Clears the list of child nodes.
    - get_children(self): Returns the list of child nodes.
    - get_parent(self): Returns the parent node.
    - set_parent(self, parent): Sets the parent node.
    - get_cost(self): Returns the cost of the node.
    - set_cost(self, cost): Sets the cost of the node.
    - get_name(self): Returns the name of the node.
    - set_name(self, name): Sets the name of the node.
    - get_value(self): Returns the value of the node.
    - set_value(self, value): Sets the value of the node.
    """

    childs = []
    parent = None
    cost = 0
    name = ""
    value = None

    #Constructor
    def __init__(self, value=None, childs=[], parent=None, cost=0, name=None):

        """
        Initialize a Vagabond system object.
        Parameters:
        - value (optional): The value of the system.
        - childs (optional): A list of child systems.
        - parent (optional): The parent system.
        - cost (optional): The cost of the system.
        - name (optional): The name of the system.
        """

        self.childs = childs
        self.value = value
        self.name = name
        self.parent = parent
        self.cost = cost

    #print function / string representation
    def __repr__(self) -> str:

        """
        Returns a string representation of the object.
        If the object has a name attribute, it returns the name.
        If the object does not have a name attribute, it tries to convert the value attribute to a string and returns it.
        If the conversion fails or the object does not have a value attribute, it returns "un-named node".
        """

        if(self.name):
            return self.name
        else:
            try:
                return str(self.value)
            except:
                return "un-named node"
        
    #equality function
    def __eq__(self, o: object) -> bool:

        """
        Compare the value of this object with another object.

        Parameters:
            o (object): The object to compare with.

        Returns:
            bool: True if the values are equal, False otherwise.
        """
        
        return self.value == o.value
    
    # Addition operation - add node b as a child to node a
    def __add__(self, b):

        """
        Adds a node to the list of child nodes.

        Parameters:
            b (node): The node to be added.

        Returns:
            self: The updated object with the added node.

        Raises:
            TypeError: If the operand type is not supported.

        """

        if isinstance(b, node):
            self.childs.append(b)
            return self
        else:
            raise TypeError("unsupported operand type(s) for +: '{}' and '{}'".format(type(self), type(b)))
        
    # Reverse addition operation - add node a as a child to node b
    def __radd__(self, a):

        """
        Right addition method for the 'node' class.

        Parameters:
        - a: An object of type 'node' or its subclass.

        Returns:
        - If 'a' is an instance of 'node', appends 'self' to the 'childs' list of 'a' and returns 'a'.
        - Raises a TypeError if 'a' is not an instance of 'node'.

        """

        if isinstance(a, node):
            a.childs.append(self)
            return a
        else:
            raise TypeError("unsupported operand type(s) for +: '{}' and '{}'".format(type(a), type(self)))
        
    # Subtraction operation - remove node b from the child list of node a
    def __sub__(self, b):

        """
        Subtract a node from the current node's list of children.

        Parameters:
        - b: The node to be subtracted from the current node's children.

        Returns:
        - self: The current node after removing the specified node from its children.

        Raises:
        - ValueError: If the specified node is not a child of the current node.
        - TypeError: If the operand type is not supported.

        """

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

        """
        Subtract a node from the current node's list of children.

        Parameters:
        - a (node): The node to be subtracted from the current node's children.

        Returns:
        - a (node): The subtracted node.

        Raises:
        - ValueError: If the given node is not a child of the current node.
        - TypeError: If the operand types are not supported for subtraction.
        """

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

        """
        Return the hash value of the object.

        Returns:
            int: The hash value of the object.
        """

        return hash(self.value)
    
    # Add a child to the node
    def add_child(self, child):

        """
        Adds a child node to the current node.

        Parameters:
        - child: An instance of the node class representing the child node.

        Raises:
        - TypeError: If the provided child is not an instance of the node class.

        Returns:
        - None
        """

        if not isinstance(child, node):
            raise TypeError("child must be an instance of the node class. Got '{}' instead".format(type(child)))
        self.childs.append(child)

    # Remove a child from the node
    def remove_child(self, child):

        """
        Removes a child node from the current node.

        Parameters:
            child (node): The child node to be removed.

        Raises:
            TypeError: If the `child` parameter is not an instance of the `node` class.

        Returns:
            None
        """

        if not isinstance(child, node):
            raise TypeError("child must be an instance of the node class. Got '{}' instead".format(type(child)))
        self.childs.remove(child)

    # Clear the children list
    def clear(self):

        """
        Clears the list of child elements.

        Parameters:
            None

        Returns:
            None
        """

        self.childs = []

    # Get the children list
    def get_children(self):

        """
        Returns the children of the current object.

        Returns:
            list: A list of child objects.
        """

        return self.childs
    
    # Get the parent node
    def get_parent(self):

        """
        Returns the parent of the current object.

        Returns:
            The parent object.
        """

        return self.parent
    
    # Set the parent node
    def set_parent(self, parent):

        """
        Sets the parent of the current node.

        Parameters:
        - parent: An instance of the node class.

        Raises:
        - TypeError: If the parent is not an instance of the node class.

        Returns:
        - None
        """

        if not isinstance(parent, node):
            raise TypeError("parent must be an instance of the node class. Got '{}' instead".format(type(parent)))
        self.parent = parent

    # Get the cost of the node
    def get_cost(self):

        """
        Returns the cost of the object.

        :return: The cost of the object.
        :rtype: float
        """

        return self.cost
    
    # Set the cost of the node
    def set_cost(self, cost):

        """
        Set the cost of the system.

        Parameters:
        - cost: The cost value to be set.

        Returns:
        None
        """

        self.cost = cost

    # Get the name of the node
    def get_name(self):

        """
        Returns the name of the object.

        Returns:
            str: The name of the object.
        """

        return self.name
    
    # Set the name of the node
    def set_name(self, name):

        """
        Sets the name of the object.

        Parameters:
        - name (str): The name to be set.

        Returns:
        None
        """

        self.name = name

    # Get the value of the node
    def get_value(self):

        """
        Returns the value of the object.

        Returns:
            The value of the object.
        """

        return self.value
    
    # Set the value of the node
    def set_value(self, value):

        """
        Set the value of the object.

        Parameters:
        - value: The value to be set.

        Returns:
        None
        """
        
        self.value = value
