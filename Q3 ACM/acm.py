# Hoang Quan Tran, 20249088
# Richard Gu, 20211389

# Reference for Prim's algorithm: chatGPT

import math
import sys
from collections import namedtuple

INFINITY = math.inf

Point = namedtuple("Point", ["x", "y"])


def squared_dist(point1, point2):
    """
    This function calculates the square of the distance between two points.
    :param point1:
    :param point2:
    :return:
    """
    return (point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2


def dist(point1, point2):
    """
    This function calculates the distance between two points.
    :param point1:
    :param point2:
    :return:
    """
    return math.sqrt(squared_dist(point1, point2))


def read_section_input():
    """
    This function reads the input for points of one MST section
    :return:
    """
    section = []
    m = int(input())
    for _ in range(m):
        a, b = list(map(float, input().split(" ")))
        section.append(Point(a, b))
    return section


def make_quick_adjacency_matrix(points):
    """
    This function makes a quick adjacency matrix for the points
    because sqrt is very costly, we will use the squared distance
    :param points:
    :return:
    """
    mat = []
    for p1 in points:
        row = []
        for p2 in points:
            row.append(squared_dist(p1, p2))
        mat.append(row)
    return mat


def min_label(label, visited):
    """
    This function finds the minimum label among the unvisited nodes
    :param label:
    :param visited:
    :return:
    """
    min_label = INFINITY
    min_index = -1
    for i in range(len(label)):
        if not visited[i] and label[i] < min_label:
            min_label = label[i]
            min_index = i
    return min_index


def prim(squared_dist_mat):
    """
    This function calculates the minimum spanning tree using Prim's algorithm
    :param squared_dist_mat: squared distance matrix
    :return: weight of the MST
    """
    n = len(squared_dist_mat)
    visited = [False] * n
    label = [INFINITY] * n
    parent = [-1] * n
    label[0] = 0
    mst_weight = 0
    for _ in range(n):
        u = min_label(label, visited)
        visited[u] = True
        for v in range(n):
            uv = (squared_dist_mat[u][v])
            if uv < label[v] and not visited[v]:
                label[v] = uv
                parent[v] = u

    for i in range(1, n):
        mst_weight += math.sqrt(squared_dist_mat[i][parent[i]])

    return mst_weight


def main(args):
    """
    The main function takes in the input from input file and runs the program, outputting the result to the output file
    :param args:
    :return:
    """
    input_file = args[0]
    output_file = args[1]

    with open(input_file, 'r') as sys.stdin:
        with open(output_file, 'w') as f:
            n = int(input())
            for _ in range(n):
                point_list = read_section_input()
                squared_dist_mat = make_quick_adjacency_matrix(point_list)
                mst = prim(squared_dist_mat)
                f.write("{:.3f}\n".format(mst))


if __name__ == '__main__':
    main(sys.argv[1:])
