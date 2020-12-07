import numpy as np

SLOPE = (1, 3)

def part1(input_str):
    input_split = input_str.split('\n')
    data = np.zeros((len(input_split), len(input_split[0])), dtype=str)
    for row, line in enumerate(input_split):
        data[row, :] = np.array([char for char in line])

    out = ''
    for row in range(data.shape[0]):
        for col in range(data.shape[1]):
            out += data[row, col]
        out += '\n'
    out = out[:-1]
    assert input_str == out

    travel_path = [(0, 0)]
    while travel_path[-1][0] < data.shape[0] - SLOPE[0]:
        travel_path.append(tuple(sum(x) for x in zip(travel_path[-1], SLOPE)))
        if travel_path[-1][1] >= data.shape[1]:
            travel_path[-1] = (travel_path[-1][0], travel_path[-1][1] - data.shape[1])
    output = data.copy()
    for idx in travel_path[2:]:
        output[idx] = 'X' if data[idx] == '#' else 'O'
    num_trees = len(output[output == 'X'])
    return num_trees
