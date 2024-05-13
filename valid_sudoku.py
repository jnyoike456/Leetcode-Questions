'''
Solution:
1. go over the board, and for each non-empty cell, validate the row, the column and the 3x3 grid

rows and columns map to 0 - 8
map the 3x3 grids to the numbers 0 - 8
    - (r//3)*3 + c//3

7,7 -> 2*3 + 2 -> 8



Time -> O(N^2)
Space -> O(N^2)

'''
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        rows_sets = [set() for _ in range(N)]
        cols_sets = [set() for _ in range(N)]
        grids_sets = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                if board[r][c] == ".":
                    continue
                
                if board[r][c] in rows_sets[r]:
                    return False
                rows_sets[r].add(board[r][c])

                if board[r][c] in cols_sets[c]:
                    return False
                cols_sets[c].add(board[r][c])

                grid_idx = (r//3)*3 + c//3
                if board[r][c] in grids_sets[grid_idx]:
                    return False
                grids_sets[grid_idx].add(board[r][c])
                
        return True