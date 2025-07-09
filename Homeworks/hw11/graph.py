# This file left intentionally blank.
# This file left intentionally blank.
from queue2050 import Queue
from stack2050 import Stack

class Graph:
    def __init__(self):
        raise NotImplementedError()

    def connected(self, E, V):
        
        visited = set()
        Queue = [E]

        while Queue:
            vertex = Queue.pop()
            if vertex == V:
                return True
            if vertex not in visited:
                visited.add(vertex)
                Queue.extend(self.neighbors(vertex))
        return False

    def bfs(self, v):
      
        bfs_tree = {v: None}
        queue = Queue()
        queue.enqueue(v)

        while not queue.is_empty():
            vertex = queue.dequeue()
            for neighbor in self.neighbors(vertex):
                if neighbor not in bfs_tree:
                    bfs_tree[neighbor] = vertex
                    queue.enqueue(neighbor)
        return bfs_tree

    def dfs(self, v):
      
        dfs_tree = {v: None}
        stack = Stack()
        stack.push(v)

        while not stack.is_empty():
            vertex = stack.pop()
            for neighbor in self.neighbors(vertex):
                if neighbor not in dfs_tree:
                    dfs_tree[neighbor] = vertex
                    stack.push(neighbor)
        return dfs_tree

    def shortest_path(self, v1, v2):
       
        bfs_tree = self.bfs(v1)
        if v2 not in bfs_tree:
            return float("inf"), None

        path = []
        current = v2
        while current is not None:
            path.insert(0, current)
            current = bfs_tree[current]

        return len(path) - 1, list(zip(path[:-1], path[1:]))

    def has_cycle(self):
        for v1 in self:
            for v2 in self:
                if v1 != v2:
                    if self.connected(v1, v2):
                        if self.connected(v2, v1):
                            path1 = self.shortest_path(v1, v2)
                            path2 = self.shortest_path(v2, v1)
                            l1, p1 = path1
                            l2, p2  = path2
                            cycle = p1 + p2
                            return (True, cycle)
        else:
            return(False, None)
class AdjacencySetGraph(Graph):
    def __init__(self, V=None, E=None):
        if V is None:
            V = set()
        if E is None:
            E = set()
        self.adj_list = {v: set() for v in V}
        for u, v in E:
            self.add_edge(u, v)

    def __iter__(self):
        return iter(self.adj_list)

    def add_vertex(self, v):
        if v not in self.adj_list:
            self.adj_list[v] = set()

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj_list[u].add(v)

    def neighbors(self, v):
        return self.adj_list[v]


class EdgeSetGraph(Graph):
    def __init__(self, V=None, E=None):
        if V is None:
            V = set()
        if E is None:
            E = set()
        self.vertices = V
        self.edges = set(E)

    def __iter__(self):
        return iter(self.vertices)

    def add_vertex(self, v):
        self.vertices.add(v)

    def add_edge(self, u, v):
        self.edges.add((u, v))

    def neighbors(self, v):
        return (v2 for v1, v2 in self.edges if v1 == v)