##################################################################################################################################
# Kruskal's algorithm:It computes the minimum spanning tree of a network.Minimum spanning tree is optimization of graph          #
# and also ensure that all nodes have connection between them, and MST has weight lesser than main spanning tree.                #
# in terms of Networking, using this algorithm network do not form a loop, and broadcast strom can be eliminated                 #
# Input - it accepts a 2d array-  first Row and first Column represent vertices, between them weight of the edge                 #
# Output - the length of the minimum spanning tree                                                                               #
# ################################################################################################################################


def Kruskal(data):
    """
    Kruskal algorithm, it consists of two part. First Part: Sorting edges in ascending order by their weight.
    Second Part: Take a graph with total number(n) of vertices,keep adding the shortest(least weight) edge,
    while avoiding the creation of cycles, until (n-1) edges have been added.
    """

    edges = []
    total_weight = 0
    num_vertices = 0

    for i, line in enumerate(data):  # looping through raw and column of matrix
        num_vertices += 1

        for j, weight in enumerate(line.rstrip().decode('ascii').split(',')):

            if weight == '-' or i >= j:  # if weight is other than number
                continue

            total_weight += int(weight)
            edges.append([int(weight), i, j])  # Collecting edges and their weight
    edges = sorted(edges)

    graph = {}
    min_weight = 0

    for edge in edges:

        weight, node1, node2 = edge
        undis = set(range(num_vertices))

        s = [node1]

        while len(s):
            v = s.pop()

            if v in undis:  # checking one of the vertex of edge in the undiscovered node
                undis.remove(v)

                if v in graph:
                    try:
                        nodes = graph[v].iterkeys()

                    except AttributeError:
                        nodes = graph[v].keys()

                    s.extend(nodes)

        if node2 in undis:  # Checking the Second vertex of edge with minimum weight

            if node1 not in graph:
                graph[node1] = {}

            graph[node1][node2] = weight  # adding not forming loop edges in graph

            if node2 not in graph:
                graph[node2] = {}

            graph[node2][node1] = weight

            min_weight += weight  # calculating  minimum weight from edges added in graphs

    return total_weight - min_weight
