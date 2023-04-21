from copy import copy as cp
from graphviz import Digraph

class node:

    child = []
    name = ""
    hidden = False
    value = None

    #Constructor
    def __init__(self,name="unnamed", value=None, list_of_child=[]):
        self.child = list_of_child
        self.value = value
        self.name = name
        self.visibility = True
        self.hidden = False

    def __repr__(self) -> str:
        return self.name

    # Addition operation - add node b as a child to node a
    def __add__(self, b):
        if isinstance(b, node):
            self.child.append(b)
            return self
        else:
            raise TypeError("unsupported operand type(s) for +: '{}' and '{}'".format(type(self), type(b)))

    # Reverse addition operation - add node a as a child to node b
    def __radd__(self, a):
        if isinstance(a, node):
            a.child.append(self)
            return a
        else:
            raise TypeError("unsupported operand type(s) for +: '{}' and '{}'".format(type(a), type(self)))

    # Subtraction operation - remove node b from the child list of node a
    def __sub__(self, b):
        if isinstance(b, node):
            if b in self.child:
                self.child.remove(b)
                return self
            else:
                raise ValueError("node '{}' is not a child of '{}'".format(b.name, self.name))
        else:
            raise TypeError("unsupported operand type(s) for -: '{}' and '{}'".format(type(self), type(b)))

    #resets the visibility of all the nodes
    def reset_visited(self):
        self.visibility = True # reset visited attribute for current node
        for i in range(len(self.child)):
            if self.child[i].visibility == False: # check if child node has not been visited
                self.child[i].reset_visited() # recursively reset visited attribute for child nodes

    #Takes a node and displays the whole tree starting from the node ( Does not reset visibility )
    def display_raw(self):
        if(self.hidden==False):
            self.display()
            self.visibility = False # mark current node as visited
            for i in range(len(self.child)):
                if self.child[i].visibility == True: # check if child node has not been visited
                    self.child[i].display_raw()

    #Takes a node and displays the whole tree starting from the node ( Resets Visibility )
    def display_all(self, draw = True):
        self.display_raw()
        self.reset_visited()
        if draw:
            return self.draw_tree()

    def display(self):
        # simple_mode if turned on, will not display values and costs
        print("\033[1;31m▞ Node:\033[1;33m" + self.name)
        print("\033[1;31m▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\033[0m")
        if self.value is not None:
            print("\033[94mValue:\033[0m \n" + str(self.value))
        if self.child:
            temp = [cp(i.name) for i in self.child]
            print("\033[94mChilds:\033[0m \n\033[1;33m" + str(temp)+"\033[0m")
            print("\033[1;31m▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂\033[0m")
            print("\033[1;31mend\033[0m\n\n")

    def draw_tree(self):

        dot = Digraph()
        dot.node_attr.update(shape='rectangle')

        self.add_node_to_graph(dot)
        self.reset_visited()
        dot.render(format='png',view=True)
        return dot

    def add_node_to_graph(self, dot):

        if(self.hidden==False):
            
            make_str = "Node: "+self.name
            if self.value is not None:
                make_str =  make_str + "\n----------\nValue: \n" + str(self.value)

            dot.node(self.name, label=make_str)
            self.visibility = False # mark current node as visited
            for i in range(len(self.child)):
                dot.edge(self.name, self.child[i].name)
                if self.child[i].visibility == True: # check if child node has not been visited
                    self.child[i].add_node_to_graph(dot)

class env:

    #single value of any type
    start_value = None
    #single goal value of type start_value
    stop_value = None
    #should be a function that returns list of child values = []
    find_child_func = None
    #should be a function that takes in a value and can name it, returns a string
    naming_conv = None

    start_node = None
    stop_node = None
    
    fitted = False

    def __init__(self,start_value=None,stop_value=None,find_child_func=None,naming_conv = None) -> None:
        
        self.start_value = start_value
        self.stop_value = stop_value
        self.find_child_func = find_child_func

        if(naming_conv == None):
            self.naming_conv = self.default_naming
        else:
            self.naming_conv = naming_conv

        self.start_node = node(name=self.naming_conv(start_value), value=self.start_value)

    def child(self,n):
        list = []
        for i in self.find_child_func(n.value):
            list.append(node(name=self.naming_conv(i), value=i))

        return list

    def default_naming(self,n):
        return str(n)