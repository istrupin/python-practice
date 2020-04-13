from graph import GraphNode
from typing import List

def color_graph(graph: List[GraphNode], colors:List[str]) -> None:
    for node in graph:
        illegal_colors = set([neighbor.color for neighbor in node.neighbors if neighbor.color])
        for color in colors:
            if color not in illegal_colors:
                node.color = color
                break

        