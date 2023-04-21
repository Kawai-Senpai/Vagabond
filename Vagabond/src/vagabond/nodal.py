from copy import copy as cp
from copy import deepcopy as dc

class bfs:

    start = None
    stop = None
    visited = []
    queue = []
    paths = []
    
    env = None

    def __init__(self):
        pass
    
    def find_nodes(self,start_point):

        self.start = start_point
        self.visited = [self.start]
        
        for i in self.start.child:
            self.queue.append(i)

        while(len(self.queue)>0):

            #We take an element out from the queue
            pop = self.queue.pop(0)
            #We get the above element's child
            way = pop.child
            # If we already don't have way's child in queue or visited, we put it in queue
            for j in way:
                if j not in self.queue and j not in self.visited:
                    self.queue.append(j)
            #The poped element is put inside visited
            self.visited.append(pop)

        return self.visited
    
    def get_paths(self):

        self.visited = [self.start]
        self.queue = []
        for i in self.start.child:
            self.queue.append(i)
        self.paths.append(cp(self.visited))

        while(len(self.queue)>0):

            #We take an element out from the queue
            pop = self.queue.pop(0)
            #print(pop.name)
            #Compare and add to parents
            for i in range(len(self.paths)):
                #print("path = ",self.paths)
                #print(str(pop)+" in "+str(self.paths[i][-1].child),pop in self.paths[i][-1].child)
                if(pop in self.paths[i][-1].child):
                    tmp = [] 
                    for j in self.paths[i]:
                        tmp.append(j)
                    tmp.append(pop)
                    self.paths.append(tmp)
                    #print(i)
                    #print(self.paths)

            #We get the above element's child
            way = cp(pop.child)
            # If we already don't have way's child in queue or visited, we put it in queue
            for j in way:
                if j not in self.queue and j not in self.visited:
                    self.queue.append(j)
            #The poped element is put inside visited
            self.visited.append(pop)

        return self.paths

    def find_shortest_path(self, start_node, end_node):

        self.start = start_node
        self.visited = [self.start]
        
        for i in self.start.child:
            self.queue.append(i)

        route = None

        for i in self.get_paths():
            if(i[0]==start_node and i[-1]==end_node):
                if(route != None):
                    if(len(route)>len(i)):
                        route = i
                else:
                    route = i

        if(route == None):
            
            print("No Route Found :")
            return None
        
        else:
            
            print("Shortest Route Found :")

            for i in range(len(route)-1):
                print(route[i].name+" --> ",end="")
            print(route[-1])

            first = dc(route[0])
            ini = first

            for i in range(len(route)-1):
                ini.child = []
                tmp = dc(route[i+1])
                ini.child = [tmp]
                ini = tmp

            ini.child = []
            diagram = first.display_all()

            return route,first,diagram
        
    def find_longest_path(self, start_node, end_node):

        self.start = start_node
        self.visited = [self.start]
        
        for i in self.start.child:
            self.queue.append(i)

        route = None

        for i in self.get_paths():
            if(i[0]==start_node and i[-1]==end_node):
                if(route != None):
                    if(len(route)<len(i)):
                        route = i
                else:
                    route = i

        if(route == None):
            
            print("No Route Found :")
            return route
        
        else:
            
            print("Longest Route Found :")

            for i in range(len(route)-1):
                print(route[i].name+" --> ",end="")
            print(route[-1])

            first = dc(route[0])
            ini = first

            for i in range(len(route)-1):
                ini.child = []
                tmp = dc(route[i+1])
                ini.child = [tmp]
                ini = tmp

            ini.child = []
            diagram = first.display_all()
            
            return route,first,diagram
        
    def find_path(self, start_node=None, end_node=None):
        return self.find_shortest_path(start_node,end_node)

    def display_visited(self):

        for i in self.visited:
            print(i.name,end=" ")
        print("")

        return self.visited

    def display_queue(self):

        for i in self.queue:
            print(i.name,end =" ")
        print("")

        return self.queue