class Solution:
        def isValidSudoku(self, board: List[List[str]]) -> bool:
            nb = [0] * (27*9)
            for i in range(9):
                for j in range(9):
                    if board[j][i] != ".":
                        cell = int(board[j][i]) - 1
                        nb[i + cell*27] += 1
                        nb[(j+9) + cell*27] += 1
                        nb[j//3*3+i//3+18 + cell*27] += 1
                        
            s = set(nb) 
            if s == {0,1} or s == {0}:
                return True
            return False