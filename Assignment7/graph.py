# A Python3 program to count the number
# of rectangular islands where every
# island is separated by a line

# Size of given matrix is M X N
M = 4
N = 5

# This function takes a matrix of 'X' and 'O'
# and returns the number of rectangular
# islands of 'X' where no two islands are
# row-wise or column-wise adjacent, the islands
# may be diagonaly adjacent
def countIslands(mat):

    count = 0; # Initialize result

    # Traverse the input matrix
    for i in range (0, M):

        for j in range(0, N):

            # If current cell is 'X', then check
            # whether this is top-leftmost of a
            # rectangle. If yes, then increment count
            if (mat[i][j] == '1'):

                if ((i == 0 or mat[i - 1][j] == '0') and
                    (j == 0 or mat[i][j - 1] == '0')):
                    count = count + 1

    return count

# Driver Code
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print("Number of rectangular islands is",
                       countIslands(grid))
mat = [['1', '1', '0', '0', '0'],
       ['1', '1', '0', '0', '0'],
       ['0', '0', '1', '0', '0'],
       ['0', '0', '0', '1', '1']]

print("Number of rectangular islands is",
                       countIslands(mat))

# This code is contributed by iAyushRaj
