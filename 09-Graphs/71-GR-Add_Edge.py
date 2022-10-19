class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    # add edge between vertex 1 and vertex 2
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():   # check if v1 and v2 are vertex's that we created. if we didn't make them, they can't be added 
            self.adj_list[v1].append(v2)                                #       append v2 to v1's list
            self.adj_list[v2].append(v1)                                #       append v1 to v2's list
            return True
        return False




my_graph = Graph()

my_graph.add_vertex(1)
my_graph.add_vertex(2)

my_graph.add_edge(1,2)
my_graph.print_graph()

print()
my_graph.add_edge(1,3)
my_graph.print_graph()

"""
    EXPECTED OUTPUT:
    ----------------
    1 : [2]
    2 : [1]

"""