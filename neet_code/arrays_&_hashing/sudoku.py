import math
from collections import *
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = defaultdict(set)
        row = defaultdict(set)
        box = defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[r])):
                cell = board[r][c]
                i = math.ceil((r + 1) / 3)
                j = math.ceil((c + 1) / 3)
                if cell.isnumeric():
                    if cell in col[c] or cell in row[r] or cell in box[ tuple([i,j]) ]:
                        return False
                    
                    col[c].add(cell)
                    row[r].add(cell)
                    box[tuple([i, j])].add(cell)

        return True