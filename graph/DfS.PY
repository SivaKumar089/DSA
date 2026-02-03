

class Graph:
    def __init__(self):
        self.graph={}

    def AddVertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]


    def AddEdeged(self,vertex1,vertex2,isDirect=False):
        self.AddVertex(vertex1)
        self.AddVertex(vertex2)

        self.graph[vertex1].append(vertex2)

        if not isDirect:
            self.graph[vertex2].append(vertex1)

    def Display(self):
        for key,value in self.graph.items():
            print(f'{key} => {value}')

    def GetVertices(self):
        for i in self.graph:
            print(i)

    def GetEdges(self):
        for key,value in self.graph.items():
            for vertex in value:
                print(f'({key},{vertex})')

    def RemoveVertex(self,vertex):
        if vertex in self.graph:
            del self.graph[vertex]
        for key,value in self.graph.items():
            if vertex in value:
                value.remove(vertex)

    def isEdge(self,vertex1,vertex2):
        return vertex1 in self.graph[vertex2] or vertex2 in self.graph[vertex1]

    def RemoveEdge(self,vertex1,vertex2,isDirect=False):
        if self.isEdge(vertex1,vertex2):

            self.graph[vertex1].remove(vertex2)

            if not isDirect:
                self.graph[vertex2].remove(vertex1)

    def Dfs_Traversel(self,start,Visited):
        if start not in Visited:
            Visited.add(start)
            print(start,end=' ')

        
        for child in self.graph[start]:
            if child not in Visited:
                self.Dfs_Traversel(child,Visited)


graph1=Graph()


graph1.AddEdeged("A","B")
graph1.AddEdeged("B","C")
graph1.AddEdeged("B","D")
graph1.AddEdeged("C","D")
graph1.Display()
# graph1.GetVertices()
# graph1.GetEdges()
# graph1.RemoveEdge('A','B')
# graph1.Display()
graph1.Dfs_Traversel('A',Visited=set())

