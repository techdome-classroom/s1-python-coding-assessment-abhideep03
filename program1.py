class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 'W' or visited[i][j]:
                return
            visited[i][j] = True
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    islands = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'L' and not visited[i][j]:
                dfs(i, j)
                islands += 1

    return islands