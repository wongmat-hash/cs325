# Kruskal's algorithm in Python


class Graph:
    def __init__(g, vertices):
        g.V = vertices
        g.graph = []

    def add_edge(g, u, v, w):
        g.graph.append([u, v, w])

    # Search function

    def find(g, parent, i):
        if parent[i] == i:
            return i
        return g.find(parent, parent[i])

    def apply_union(g, parent, rank, x, y):
        xroot = g.find(parent, x)
        yroot = g.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    #  Applying Kruskal algorithm
    def kruskal(g):
        result = []
        i, e = 0, 0
        g.graph = sorted(g.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(g.V):
            parent.append(node)
            rank.append(0)
        while e < g.V - 1:
            u, v, w = g.graph[i]
            i = i + 1
            x = g.find(parent, u)
            y = g.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                g.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))


g = Graph(6)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 2)
g.add_edge(1, 0, 4)
g.add_edge(2, 0, 4)
g.add_edge(2, 1, 2)
g.add_edge(2, 3, 3)
g.add_edge(2, 5, 2)
g.add_edge(2, 4, 4)
g.add_edge(3, 2, 3)
g.add_edge(3, 4, 3)
g.add_edge(4, 2, 4)
g.add_edge(4, 3, 3)
g.add_edge(5, 2, 2)
g.add_edge(5, 4, 3)
g.kruskal()
