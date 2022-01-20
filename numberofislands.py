"""
https://leetcode.com/problems/number-of-islands/solution/
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""


def dfs(grid, i, j):
    # use DFS to check bounds and sink islands when found
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0":
        return
    
    grid[i][j] = "0"
    
    dfs(grid, i-1, j)
    dfs(grid, i+1, j)
    dfs(grid, i, j-1)
    dfs(grid, i, j+1)
    
def numIslands(grid):
    
    # use DFS to count each island
    islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "1":
                dfs(grid, i, j)
                islands += 1
                
    return islands

"""
Time: O(m * n)
Space: O(m * n)
"""

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

ans = numIslands(grid)
print(ans)

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

ans = numIslands(grid)
print(ans)