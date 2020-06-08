from typing import Dict


def overlap(first: Dict[str, int], second: Dict[str, int]) -> Dict[str, int]:
    x_overlap = find_x_overlap(first, second)
    y_overlap = find_y_overlap(first, second)
    if x_overlap == 0 or y_overlap == 0:
        return {}
    else:
        return {
            'left_x': find_left_x(first, second),
            'width':  x_overlap,
            'bottom_y': find_bottom_y(first, second),
            'height': y_overlap
        }


def find_x_overlap(first: Dict[str, int], second: Dict[str, int]) -> int:
    if first['width'] <= second['width'] or second['width'] <= first['width']:
        return min(first['width'], second['width'])
    if first['left_x'] < (second['left_x'] + second['width']) and \
       first['left_x'] > second['left_x']:
        return second['left_x'] + second['width'] - first['left_x']
    if second['left_x'] < (first['left_x'] + first['width']) and \
       second['left_x'] > first['left_x']:
        return first['left_x'] + first['width'] - second['left_x']
    else:
        return 0


def find_y_overlap(first: Dict[str, int], second: Dict[str, int]) -> int:
    if first['height'] <= second['height'] or second['height'] <= first['height']:
        return min(first['height'], second['height'])
    if first['bottom_y'] < second['bottom_y'] + second['height'] and \
       first['bottom_y'] > second['bottom_y']:
        return second['bottom_y'] + second['height'] - first['bottom_y']
    if second['bottom_y'] < first['bottom_y'] + first['height'] and \
       second['bottom_y'] > first['bottom_y']:
        return first['bottom_y'] + first['height'] - second['bottom_y']
    else:
        return 0


def find_left_x(first: Dict[str, int], second: Dict[str, int]) -> int:
    return max(first['left_x'], second['left_x'])


def find_bottom_y(first: Dict[str, int], second: Dict[str, int]) -> int:
    return max(first['bottom_y'], second['bottom_y'])


print(find_x_overlap({'left_x': 1, 'width': 6}, {'left_x': 5, 'width': 3}))
print(find_x_overlap({'left_x': 5, 'width': 3}, {'left_x': 1, 'width': 6}))

print(find_x_overlap({'left_x': 5, 'width': 8}, {'left_x': 6, 'width': 2})) # should be 2

print(find_y_overlap({'bottom_y': 3, 'height': 4}, {'bottom_y': 1, 'height': 3}))
print(find_y_overlap({'bottom_y': 1, 'height': 3}, {'bottom_y': 3, 'height': 4}))


print(find_y_overlap({'bottom_y': 1, 'height': 9}, {'bottom_y': 3, 'height': 4})) #should be 4

print(overlap({'left_x': 1, 'bottom_y': 1, 'width': 6, 'height': 3}, {'left_x': 5, 'bottom_y': 2, 'width': 3, 'height': 6}))
