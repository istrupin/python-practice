from typing import List, Dict
from collections import deque

def shortest_path(graph:Dict[str, List[str]], start_node: str, end_node: str) -> List[str]:
    to_visit = deque([start_node])
    parents = {start_node: None}
    while len(to_visit) > 0:
        current = to_visit.popleft()
        if current == end_node:
             path = [current]
             p = parents[current]
             while(p):
                path.append(p)
                p = parents[p]
             path.reverse()
             return path
        for neighbor in graph[current]:
            if neighbor not in parents:
                parents[neighbor] = current
                to_visit.append(neighbor)
    return None




network = {
    'Min'     : ['William', 'Jayden', 'Omar'],
    'William' : ['Min', 'Noam'],
    'Jayden'  : ['Min', 'Amelia', 'Ren', 'Noam'],
    'Ren'     : ['Jayden', 'Omar'],
    'Amelia'  : ['Jayden', 'Adam', 'Miguel'],
    'Adam'    : ['Amelia', 'Miguel', 'Sofia', 'Lucas'],
    'Miguel'  : ['Amelia', 'Adam', 'Liam', 'Nathan'],
    'Noam'    : ['Nathan', 'Jayden', 'William'],
    'Omar'    : ['Ren', 'Min', 'Scott'],
}


print(shortest_path(network, "Ren", "Amelia"))