from typing import List
from self import self
import heapq

def minEffort(self, heights: List[List[int]]) -> int:
    #init vars, and possible directions
    m,n = len(heights), len(heights[0])
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    output = 0
    heap = [(0,0,0)]
    visited = set()

    while heap:
        k,x,y= heapq.heappop(heap)
        output = max(output,k)
        if (x,y) == (m-1, n-1):
            return output
        visited.add((x,y))
        for dx, dy, in dirs:
            new_x, new_y = x+dx,y
            if 0 <new_x<m and 0<=new_y<n and (new_x, new_y) not in visited:
                new_k = abs(heights[x][y]-heights[new_x][new_y])
                heapq.heappush(heap,(new_k, new_x, new_y))
    return -1



if __name__ ==  '__main__':
    input = [[1,3,5],[2,8,3],[3,4,5]]
    print(minEffort(input))
