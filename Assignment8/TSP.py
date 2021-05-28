from sys import maxsize
from itertools import permutations
V = 4

#TSP with MST 
def approx_tsp_algo(G):
    s = 0
    vertex = []                                                 #store vertex from source
    for i in range(V):
        if i != s:
            vertex.append(i)

    min_path = maxsize                                          #hamiltonian cycle w
    next_permutation=permutations(vertex)
    for i in next_permutation:

        current_pathweight = 0                                  #store path

        k = s
        for j in i:                                             #calculate path W
            current_pathweight += G[k][j]
            k = j
        current_pathweight += G[k][s]

        min_path = min(min_path, current_pathweight)            #update min

    return min_path


if __name__ == "__main__":

    G = [[0, 4, 3, 1], [4, 0, 1, 2],
            [3, 1, 0, 5], [1, 2, 5, 0]]
    print(approx_tsp_algo(G))
