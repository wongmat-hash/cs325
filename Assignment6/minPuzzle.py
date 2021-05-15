from typing import List
import heapq

def minEffort(heights: List[List[int]]) -> int:
    #init vars, and possible directions
    m,n = len(heights), len(heights[0])
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    def dfs(k,x,y):
        visited.add((x,y))
        for dx,dy in dirs:
            new_x, new_y = x+dx, y+dy
            if 0 <= new_x<m and 0<=new_y<n and (new_x,new_y) not in visited:
                new_k = abs(heights[x][y]-heights[new_x][new_y])
                if new_k <= k:
                    dfs(k, new_x, new_y)

    mn, mx = -1, max([heights[row][col] for col in range(n) for row in range(m)])
    while mn+1 < mx:
        mid = (mn+mx)//2
        visited = set()
        dfs(mid, 0, 0)
        if (m-1, n-1) in visited:
            mx = mid
        else:
            mn = mid
    return mx



if __name__ ==  '__main__':
    input = [[1,3,5],[2,8,3],[3,4,5]]
    print(minEffort(input))
