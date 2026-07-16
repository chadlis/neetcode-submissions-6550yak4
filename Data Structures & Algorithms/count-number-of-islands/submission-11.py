class Solution:
    def dfs(self, grid, visited, rows, cols, r, c):
        if (
            r < 0 or r >= rows or c < 0 or c >= cols
            or grid[r][c] == "0" or ((r, c) in visited)):
            return
        visited.add((r, c))
        for (i, j) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            self.dfs(grid, visited, rows, cols, r + i, c + j)

    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands_count = 0
        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == "1") and ((r, c) not in visited):
                    islands_count += 1
                    self.dfs(grid, visited, rows, cols, r, c)
        return islands_count

