from collections import defaultdict

from aoc_input import AOCInput

INP = AOCInput(7)
NODES = set()
DAG = defaultdict(list)
for line in INP.value.split('\n'):
    words = line.split()
    node_1 = words[1]
    node_2 = words[7]
    DAG[node_1].append(node_2)  # creates an adjacency list
    NODES.add(node_1)
    NODES.add(node_2)


def part_a():
    out = []
    degree = defaultdict(int)
    for node in NODES:
        for connected in DAG[node]:
            degree[connected] += 1
    zero_list = [node for node in NODES if degree[node] == 0]

    while len(zero_list) > 0:
        v = min(zero_list)
        zero_list.remove(v)
        out.append(v)
        for w in DAG[v]:
            degree[w] -= 1
            if degree[w] == 0:
                zero_list.append(w)

    return ''.join(out)


if __name__ == '__main__':
    print(part_a())
