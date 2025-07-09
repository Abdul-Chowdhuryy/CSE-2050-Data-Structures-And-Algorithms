import math

# the Entry class
class Entry:
    def __init__(self, i, p):
        self.item = i
        self.priority = p
    
    def lt(self, other):
        return self.priority < other.priority
    
    def eq(self, other):
        return self.item == other.item and self.priority == other.priority

# unordered list of queue
class PQ_UL:
    def __init__(self):
        self.queue = []
        self.len = 0
    
    def insert(self, item, priority):
        en = Entry(item, priority)
        self.len += 1
        self.queue.append(en)
    
    def find_min(self):
        minpri, minit = math.inf, None
        for each in self.queue:
            if each.priority < minpri:
                minpri = each.priority
                minit = each
        return minit
    
    def remove_min(self):
        minit = self.find_min()
        self.len -= 1
        self.queue.remove(minit)
        return minit
    
    def __len__(self):
        return self.len

# ordered list of queue
class PQ_OL:
    def __init__(self):
        self.queue = []
        self.len = 0
    
    def insert(self, item, priority):
        en = Entry(item, priority)
        self.queue.append(en)
        self.len += 1
        for i in range(len(self.queue)-2, -1, -1):
            if self.queue[i].priority > self.queue[i+1].priority:
                self.queue[i], self.queue[i+1] = self.queue[i+1], self.queue[i]
            else:
                return
    
    def find_min(self):
        return self.queue[0]
    
    def remove_min(self):
        minit = self.find_min()
        self.len -= 1
        self.queue.remove(minit)
        return minit
    
    def __len__(self):
        return self.len
