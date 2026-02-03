

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

    def Shotest_path(self,start,end):
        Visited={start}
        Queue=[(start,[start])]

        while len(Queue)>0:
            current,path=Queue.pop(0)

            for child in self.graph[current]:
                if child == end:
                    return path+[child]
                if child not in Visited:
                    Queue.append((child,path+[child]))
                    Visited.add(child)





graph1=Graph()


graph1.AddEdeged("A","B")
graph1.AddEdeged("B","E")
graph1.AddEdeged("B","C")
graph1.AddEdeged("C","D")
graph1.AddEdeged("B","D")
graph1.Display()
# graph1.GetVertices()
# graph1.GetEdges()
# graph1.RemoveEdge('A','B')
# graph1.Display()
print(graph1.Shotest_path("A","D"))



def twoSum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i


nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums, target))   # [0, 1]
