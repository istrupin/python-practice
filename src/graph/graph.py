from typing import Set

class GraphNode:
    label: str
    neighbors: Set
    color: str
    def __init__(self, label: str):
        self.label = label
        self.neighbors = set()
        self.color = None

