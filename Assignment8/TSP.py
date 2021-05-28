from sys import maxsize
from itertools import permutations
V = 4

# implementation of traveling Salesman Problem
def approx_tsp_algo(G):
    s = 0
    # store all vertex apart from source vertex
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    # store minimum weight Hamiltonian Cycle
    min_path = maxsize
    next_permutation=permutations(vertex)
    for i in next_permutation:

        # store current Path weight(cost)
        current_pathweight = 0

        # compute current path weight
        k = s
        for j in i:
            current_pathweight += G[k][j]
            k = j
        current_pathweight += G[k][s]

        # update minimum
        min_path = min(min_path, current_pathweight)

    return min_path


# Driver Code
if __name__ == "__main__":

    # matrix representation of G
    G = [[0, 4, 3, 1], [4, 0, 1, 2],
            [3, 1, 0, 5], [1, 2, 5, 0]]
    print(approx_tsp_algo(G))
