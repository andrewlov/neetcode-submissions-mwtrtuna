class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        time = 0
        numOranges = 0



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    numOranges += 1

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and numOranges > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row < 0 or row == ROWS or col < 0 or col == COLS or grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    q.append([row, col])
                    numOranges -= 1

            time += 1
        if numOranges == 0:
            return time
        else:
            return -1