class Graph_ES:
    def __init__(self, vertices=None, edges=None):
        self.vertices = set(vertices) if vertices else set()
        self.edges = set(edges) if edges else set()

    def __len__(self):
        return len(self.vertices)

    def __iter__(self):
        return iter(self.vertices)

    def add_vertex(self, v):
        self.vertices.add(v)

    def remove_vertex(self, v):
        if v not in self.vertices:
            raise KeyError
        self.vertices.remove(v)
        # Remove any edges incident to the removed vertex
        self.edges = {(u, w) for u, w in self.edges if u != v and w != v}

    def add_edge(self, e):
        u, v = e
        if u not in self.vertices or v not in self.vertices:
            raise KeyError
        self.edges.add(e)

    def remove_edge(self, e):
        if e not in self.edges:
            raise KeyError(f"Edge {e} not in graph")
        u, v = e
        self.edges.remove((v, u))  # Remove edge (v, u)
        self.edges.remove((u, v))  # Remove edge (u, v)

    def _neighbors(self, v):
        neighbors = set()
        for u, w in self.edges:
            if u == v:
                neighbors.add(w)
            elif w == v:
                neighbors.add(u)
        return neighbors

    
class Graph_AS:
    def __init__(self, vertices=None, edges=None):
        self.adjacency = {v: set() for v in vertices} if vertices else {}

        if edges:
            for u, v in edges:
                self.add_edge((u, v))

    def __len__(self):
        return len(self.adjacency)

    def __iter__(self):
        return iter(self.adjacency)

    def add_vertex(self, v):
        self.adjacency.setdefault(v, set())

    def remove_vertex(self, v):
        if v not in self.adjacency:
            raise KeyError
        del self.adjacency[v]
        # Remove any incident edges to the removed vertex
        for u in self.adjacency:
            self.adjacency[u] = {w for w in self.adjacency[u] if w != v}

    def add_edge(self, e):
        u, v = e
        if u not in self.adjacency or v not in self.adjacency:
            raise KeyError
        self.adjacency[u].add(v)
        self.adjacency[v].add(u)

    def remove_edge(self, e):
        u, v = e
        if u not in self.adjacency or v not in self.adjacency[u]:
            raise KeyError
        self.adjacency[u].remove(v)
        self.adjacency[v].remove(u)

    def _neighbors(self, v):
        return self.adjacency[v]
