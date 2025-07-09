class Entry:
    """Represents an entry in the priority queue."""

    def __init__(self, priority, process_id):
        """Initializes an Entry object with a given priority and process ID."""
        self.priority = priority
        self.process_id = process_id

    def __repr__(self):
        """Returns a string representation of the Entry object."""
        return f"Entry(priority={self.priority}, process_id={self.process_id})"

    def __gt__(self, other):
        """Compares the priority of this entry with another entry.
        Returns: bool: True if this entry has higher priority than the other, False otherwise."""
        return self.priority > other.priority

    def __eq__(self, other):
        """Checks if this entry is equal to another entry based on priority.
        Returns: bool: True if the priorities are equal, False otherwise."""
        return self.priority == other.priority


class MaxHeap:
    """Represents a max heap data structure."""

    def __init__(self):
        """Initializes a MaxHeap object."""
        self._heap = []

    def put(self, entry):
        """Inserts an entry into the max heap."""
        self._heap.append(entry)
        self._upheap(len(self._heap) - 1)

    def remove_max(self):
        """Removes and returns the entry with the maximum priority from the max heap.
        Returns: The process ID that was removed from the queue. Raise IndexError if the heap is empty."""
        if not self._heap:
            raise IndexError("Heap is empty")
        max_entry = self._heap[0]
        last_entry = self._heap.pop()
        if self._heap:
            self._heap[0] = last_entry
            self._downheap(0)
        return max_entry.process_id

    def change_priority(self, process_id, new_priority):
        """Changes the priority of a process in the max heap.
        Returns: bool: True if the priority change was successful, False otherwise."""
        for entry in self._heap:
            if entry.process_id == process_id:
                old_priority = entry.priority
                entry.priority = new_priority
                if new_priority > old_priority:
                    self._upheap(self._heap.index(entry))
                else:
                    self._downheap(self._heap.index(entry))
                return True
        return False

    def _upheap(self, index):
        """Performs up-heap operation to maintain heap property after insertion."""
        while index > 0:
            parent_index = (index - 1) // 2
            if self._heap[index] > self._heap[parent_index]:
                self._heap[index], self._heap[parent_index] = self._heap[parent_index], self._heap[index]
                index = parent_index
            else:
                break

    def _downheap(self, index):
        """Performs down-heap operation to maintain heap property after removal."""
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            largest = index
            if left_child_index < len(self._heap) and self._heap[left_child_index] > self._heap[largest]:
                largest = left_child_index
            if right_child_index < len(self._heap) and self._heap[right_child_index] > self._heap[largest]:
                largest = right_child_index
            if largest != index:
                self._heap[index], self._heap[largest] = self._heap[largest], self._heap[index]
                index = largest
            else:
                break

    def __len__(self):
        """len is the number of items in the PQ"""
        return len(self._heap)


class TaskManager:
    """Manages the execution of processes using a priority queue."""

    def __init__(self):
        """Initializes a TaskManager object."""
        self.processor_queue = MaxHeap()

    def add_process(self, entry):
        """Adds a process to the processor queue."""
        self.processor_queue.put(entry)

    def remove_process(self):
        """Removes and returns the process with the highest priority from the processor queue."""
        try:
            return self.processor_queue.remove_max()
        except IndexError:
            raise IndexError