class Solution:
        def isValidSudoku(self, board: List[List[str]]) -> bool:
            nb = [0] * (27*9)
            for i in range(9):
                for j in range(9):
                    if board[j][i] != ".":
                        cell = int(board[j][i]) - 1
                        if 1 in (nb[i + cell*27] , nb[(j+9) + cell*27] , nb[j//3*3+i//3+18 + cell*27]):
                            return False
                        nb[i + cell*27] += 1
                        nb[(j+9) + cell*27] += 1
                        nb[j//3*3+i//3+18 + cell*27] += 1
                        
            return True