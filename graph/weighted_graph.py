class WeightGraph:
    def __init__(self):
        self.graph={}

    
    def add_vertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]={}

    def Display(self):
        for key,value in self.graph.items():
            print(f'{key} => {value}')
        
    
    def add_edge(self,from_vertex,to_vertex,weight,isDirect=False):
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)

        self.graph[from_vertex][to_vertex]=weight

        if not isDirect:
            self.graph[to_vertex][from_vertex]=weight

    def RemoveVertex(self,vertex):
        if vertex in self.graph:
            del self.graph[vertex]

        for vertex in self.graph:
            if vertex_in in vertex:
                pass

    def RemoveEdge(self,from_vertex,to_vertex):

        if from_vertex in self.graph and to_vertex in self.graph[from_vertex]:
            del self.graph[from_vertex][to_vertex]
    
        if to_vertex in self.graph and from_vertex in self.graph[to_vertex]:
            del self.graph[to_vertex][from_vertex]
    



graph1=WeightGraph()
graph1.add_edge("Chennai","Mumbai",400)
graph1.add_edge("Chennai","Devathanam",600)
graph1.Display()

graph1.Display()

