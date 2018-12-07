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
    zero_list = {node for node in NODES if degree[node] == 0}

    while len(zero_list) > 0:
        v = min(zero_list)
        zero_list.remove(v)
        out.append(v)
        for w in DAG[v]:
            degree[w] -= 1
            if degree[w] == 0:
                zero_list.add(w)

    return ''.join(out)


def task_time(l):
    return 61 + (ord(l) - ord('A'))


def part_b():
    degree = defaultdict(int)
    for node in NODES:
        for connected in DAG[node]:
            degree[connected] += 1
    zero_list = {node for node in NODES if degree[node] == 0}

    # there's GOTTA be a better algorithm than this stack of crap
    work_needed = {node: task_time(node) for node in NODES}
    current_tasks = set()
    completed = set()
    time_taken = 0
    while len(completed) < len(NODES):
        while len(current_tasks) < 5 and len(zero_list) > 0:
            t = min(zero_list)
            zero_list.remove(t)
            current_tasks.add(t)

        # we can assume that current_tasks is nonempty
        work_step = min(work_needed[task] for task in current_tasks)
        time_taken += work_step
        for task in current_tasks:
            work_needed[task] -= work_step
            if work_needed[task] == 0:
                completed.add(task)
                for w in DAG[task]:
                    degree[w] -= 1
                    if degree[w] == 0:
                        zero_list.add(w)
        current_tasks.difference_update({task for task in current_tasks if work_needed[task] == 0})
    return time_taken


if __name__ == '__main__':
    print(part_a())
    print(part_b())
