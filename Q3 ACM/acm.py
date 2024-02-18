# Nom, Matricule
# Nom, Matricule

import math
import sys
from collections import namedtuple

INFINITY = math.inf

Point = namedtuple("Point", ["x", "y"])


def quick_dist(point1, point2):
    return (point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2


def dist(point1, point2):
    return math.sqrt(quick_dist(point1, point2))


def read_section_input():
    section = []
    m = int(input())
    for _ in range(m):
        a, b = list(map(float, input().split(" ")))
        section.append(Point(a, b))
    return section


def make_quick_adjacency_matrix(points):
    # because sqrt is very costly, we will use the un-square-rooted distance
    mat = []
    for p1 in points:
        row = []
        for p2 in points:
            row.append(quick_dist(p1, p2))
        mat.append(row)
    return mat


def min_label(label, visited):
    min_label = INFINITY
    min_index = -1
    for i in range(len(label)):
        if not visited[i] and label[i] < min_label:
            min_label = label[i]
            min_index = i
    return min_index


def prim(adj_mat):
    n = len(adj_mat)
    visited = [False] * n
    label = [INFINITY] * n
    parent = [-1] * n
    label[0] = 0
    mst_weight = 0
    for _ in range(n):
        u = min_label(label, visited)
        visited[u] = True
        for v in range(n):
            uv = (adj_mat[u][v])
            if uv < label[v] and not visited[v]:
                label[v] = uv
                parent[v] = u

    for i in range(1, n):
        mst_weight += math.sqrt(adj_mat[i][parent[i]])

    return mst_weight


# Fonction main/Main function
def main(args):
    # input_file = args[0]
    # output_file = args[1]
    for i in range(3, 8, 1):
        input_file = f"input{i}.txt"
        output_file = f"output{i}.txt"

        with open(input_file, 'r') as sys.stdin:
            with open(output_file, 'w') as sys.stdout:
                n = int(input())
                for _ in range(n):
                    point_list = read_section_input()
                    unsqrt_mat = make_quick_adjacency_matrix(point_list)
                    mst = prim(unsqrt_mat)
                    print("{:.3f}".format(mst))


# NE PAS TOUCHER
# DO NOT TOUCH
if __name__ == '__main__':
    main(sys.argv[1:])
