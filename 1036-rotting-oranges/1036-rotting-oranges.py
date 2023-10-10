class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q = []
        time, fresh = 0, 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    q.append((r,c))
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh:
            length = len(q)
            for _ in range(length):
                r,c = q.pop(0) 
                
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (
                        row in range(rows) and 
                        col in range(cols)
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time+=1

        return time if fresh == 0 else -1



                    




        