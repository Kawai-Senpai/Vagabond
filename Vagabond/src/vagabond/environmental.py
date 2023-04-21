from copy import copy as cp
from copy import deepcopy as dc

class bfs:

    start = None
    stop = None
    visited = []
    queue = []
    paths = []
    
    #Stores the env
    env = None

    #The constructor, calls fit automatically. Env must be passed
    def __init__(self,env):
        if(env != None):
            self.env = env
            self.fit()
        else:
            raise RuntimeError("A valid env type environment is needed")
    
    #Find and Build paths from start node to end node
    def fit(self):

        if(self.env != None):
            
            #store the start node
            self.start = self.env.start_node
            #update visited array
            self.visited = [self.env.start_node]
            #generate child of the start node and add to queue
            self.env.start_node.child  = self.env.child(self.visited[0])
            self.queue = cp(self.env.start_node.child)
            
            #Build the whole tree/paths until goal is reached
            while(len(self.queue)>0):

                #We take an element out from the queue
                pop = self.queue.pop(0)
                
                #The goal value is found
                if(pop.value == self.env.stop_value):
                    self.env.stop_node = pop
                    self.stop = pop
                    break
                
                #We get the above element's child
                pop.child  = self.env.child(pop)
                way = cp(pop.child)

                # If we already don't have way's child in queue or visited, we put it in queue
                for j in way:
                    c = True
                    for x in self.queue:
                        if(x.value == j.value):
                            c = False
                    for x in self.visited:
                        if(x.value == j.value):
                            c = False
                    if c:
                        self.queue.append(j)
                #The poped element is put inside visited
                self.visited.append(pop)

        #The environment is built, we set fitted to true
        self.env.fitted = True

    def find_nodes(self):

        if(self.env.fitted == True):
            self.start = self.env.start_node
            self.visited = [self.start]
            
            for i in self.start.child:
                self.queue.append(i)
        else:
            raise RuntimeError("Env must be fitted/build. Pass the Env to the constructor or call fit()")

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

        visited = [self.start]
        queue = []
        for i in self.start.child:
            queue.append(i)
        self.paths.append(cp(visited))

        while(len(queue)>0):

            #We take an element out from the queue
            pop = queue.pop(0)
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
                if j not in queue and j not in visited:
                    queue.append(j)
            #The poped element is put inside visited
            visited.append(pop)

        return self.paths

    def find_shortest_path(self):

        if(self.env.fitted == True):
            self.start = self.env.start_node
            self.visited = [self.start]
            start_node = self.env.start_node
            end_node = self.env.stop_node
            
            for i in self.start.child:
                self.queue.append(i)
        else:
            raise RuntimeError("Env must be fitted/build. Pass the Env to the constructor or call fit()")

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
        
    def find_longest_path(self):

        if(self.env.fitted == True):
            self.start = self.env.start_node
            self.visited = [self.start]
            start_node = self.env.start_node
            end_node = self.env.stop_node
            
            for i in self.start.child:
                self.queue.append(i)
        else:
            raise RuntimeError("Env must be fitted/build. Pass the Env to the constructor or call fit()")

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
        
    def find_path(self):
        return self.find_shortest_path()

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