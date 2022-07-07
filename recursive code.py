import sys  # the sys function is called to give access to the system's

# parameters and functions

NO_PATH = sys.maxsize  # this is the algorithm's infinity. It is returned
# if there is no edge from one vertex to another
graph = [[0, 5, NO_PATH, 10],
         [NO_PATH, 0, 3, NO_PATH],
         [NO_PATH, NO_PATH, 0, 1],
         [NO_PATH, NO_PATH, NO_PATH, 0]]  # this is the input graph
# provided on the VLE
# from geekstogeeks website

MAX_LIMIT = len(graph[0])
""" the MAX_LIMIT is the maximum number of vertices in the above mentioned 4x4 matrix"""


def floyd_recursive(distance, k=0, i=0, j=0):
    """
    This function runs a recursive version of the Floyd's algorithm. distance refers to the matrix.
    type distance: 2D array
    param k: start node
    param i: intermediate node
    param j: end node
    The parameters k,i,j should not exceed the MAX_LIMIT mentioned above(MAX_LIMIT = len(graph[0])).
    Parameters i and j need to be 1 less than the MAX_LIMIT while k$$$$$$
    """

    if k < MAX_LIMIT:
        distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
        if j < MAX_LIMIT - 1:
            j += 1
        elif i < MAX_LIMIT - 1:
            j = 0
            i += 1
        elif k < MAX_LIMIT:
            j = 0
            i = 0
            k += 1
        floyd_recursive(distance, k, i, j)
    return distance


"""The below function is to show the result in a specifically formatted graph
"""


def print_graph(distance):
    for start_point in range(MAX_LIMIT):
        for end_point in range(MAX_LIMIT):
            if distance[start_point][end_point] == NO_PATH:
                print("%7s" % " NO_PATH ", end=" ")
            else:
                print("%7d\t" % (distance[start_point][end_point]), end="  ")
            if end_point == MAX_LIMIT - 1:
                print()


print_graph(floyd_recursive(graph))
