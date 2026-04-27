class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ROWS = COLS = n
        res = []
        col = set()
        posDiag = set() # r + c
        negDiag = set() # r - c
        board = [["."] * n for i in range(n)]
        
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for i in range(n):
                invalid = (i in col or (r + i) in posDiag or (r - i) in negDiag)
                if invalid:
                    continue
                
                col.add(i)
                posDiag.add(r + i)
                negDiag.add(r - i)
                board[r][i] = 'Q'
                backtrack(r + 1)
                col.remove(i)
                posDiag.remove(r + i)
                negDiag.remove(r - i)
                board[r][i] = '.'

        backtrack(0)
        return res