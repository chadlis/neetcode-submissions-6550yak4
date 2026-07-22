class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set((str(i) for i in range(1, 10)) ) for _ in range(9)]
        cols = [set((str(i) for i in range(1, 10)) ) for _ in range(9)]
        squares = {(i,j): set((str(k) for k in range(1, 10))) for i in range(3) for j in range(3)}
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in rows[i]:
                    return False
                rows[i].remove(board[i][j])
                if board[i][j] not in cols[j]:
                    return False
                cols[j].remove(board[i][j])
                r, c = (i//3, j//3)
                if board[i][j] not in squares[(r,c)]:
                    return False
                squares[(r, c)].remove(board[i][j])
        return True
                