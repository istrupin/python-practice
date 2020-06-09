from typing import Dict, Type


# def overlap(first: Dict[str, int], second: Dict[str, int]) -> Dict[str, int]:
#     x_overlap = find_x_overlap(first, second)
#     y_overlap = find_y_overlap(first, second)
#     if x_overlap == 0 or y_overlap == 0:
#         return {}
#     else:
#         return {
#             'left_x': find_left_x(first, second),
#             'width':  x_overlap,
#             'bottom_y': find_bottom_y(first, second),
#             'height': y_overlap
#         }

def overlap(first: Dict[str, int], second: Dict[str, int]) -> Dict[str, int]:
    x_overlap = find_overlap(first['left_x'], first['width'],
                             second['left_x'], second['width'])
    y_overlap = find_overlap(first['bottom_y'], first['height'],
                             second['bottom_y'], second['height'])

    if x_overlap == (0, 0) or y_overlap == (0, 0):
        return {}
    else:
        left_x, width = x_overlap
        bottom_y, height = y_overlap
        return {
            'left_x': left_x,
            'width': width,
            'bottom_y': bottom_y,
            'height': height
        }


def find_x_overlap(first: Dict[str, int], second: Dict[str, int]) -> int:
    if is_inside(first['left_x'], first['width'], 
                 second['left_x'], second['width']):
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
    if is_inside(first['bottom_y'], first['height'],
                 second['bottom_y'], second['height']):
        return min(first['height'], second['height'])
    if first['bottom_y'] < second['bottom_y'] + second['height'] and \
       first['bottom_y'] > second['bottom_y']:
        return second['bottom_y'] + second['height'] - first['bottom_y']
    if second['bottom_y'] < first['bottom_y'] + first['height'] and \
       second['bottom_y'] > first['bottom_y']:
        return first['bottom_y'] + first['height'] - second['bottom_y']
    else:
        return 0


def find_overlap(first_point, first_len, second_point, second_len):
    max_start = max(first_point, second_point)
    min_end = min(first_point + first_len, second_point + second_len)
    if max_start < min_end:
        return(max_start, min_end - max_start)
    else:
        return (0, 0)


def find_left_x(first: Dict[str, int], second: Dict[str, int]) -> int:
    return max(first['left_x'], second['left_x'])


def find_bottom_y(first: Dict[str, int], second: Dict[str, int]) -> int:
    return max(first['bottom_y'], second['bottom_y'])


def is_inside(first_point: int, first_len: int,
              second_point: int, second_len: int):
    return (first_point <= second_point and
            first_len + first_point >= second_len + second_point) or \
           (second_point <= first_point and
            second_len + second_point >= first_len + first_point)


# print(find_x_overlap({'left_x': 1, 'width': 6}, {'left_x': 5, 'width': 3}))
# print(find_x_overlap({'left_x': 5, 'width': 3}, {'left_x': 1, 'width': 6}))

# print(find_x_overlap({'left_x': 5, 'width': 8}, {'left_x': 6, 'width': 2})) # should be 2

# print(find_y_overlap({'bottom_y': 3, 'height': 4}, {'bottom_y': 1, 'height': 3}))
# print(find_y_overlap({'bottom_y': 1, 'height': 3}, {'bottom_y': 3, 'height': 4}))


# print(find_y_overlap({'bottom_y': 1, 'height': 9}, {'bottom_y': 3, 'height': 4})) #should be 4

print(overlap({'left_x': 1, 'bottom_y': 1, 'width': 6, 'height': 3},
              {'left_x': 5, 'bottom_y': 2, 'width': 3, 'height': 6}))


print(overlap({'left_x': 1, 'bottom_y': 1, 'width': 6, 'height': 3},
              {'left_x': 5, 'bottom_y': 9, 'width': 3, 'height': 6}))


print(overlap({'left_x': 1, 'bottom_y': 1, 'width': 6, 'height': 6},
              {'left_x': 3, 'bottom_y': 2, 'width': 3, 'height': 3}))
