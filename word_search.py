'''
Test cases:
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED" -> True
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEe" -> False
board = [["A"]], word = "A" -> true
board = [["A"]], word = "B" -> False

Reduction -> is there a path from the first letter to the last letter of the string? -> graph

Solution
- Starting at the first letter of the word, can we traverse to the end of the word
- Starting at the first position in the matrix, can we traverse to the end of the word -> go with this is because, this is easier to do

[
    ["S","F","C","S"],
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
]

ABCCED
i

[
    ["A","B","E","E"],
    ["A","B","E","E"],
    ["A","D","E","E"]
]

ABEED

AB



Solution:
- need a helper dfs function
    - happy path, we get to the end of the word
    - unhappy paths:
        - we go out of bounds
        - it's a cell that we have already visited(be careful for the visited set)
        - the character in the matrix is not the same as the character in the string
- Starting at the first position in the matrix, can we traverse to the end of the word -> go with this is because, this is easier to do

- Time and Space -> O(m*n)

board = [["A"]], word = "A" -> true
board = [["A"]], word = "B" -> False

[
    ["A","B","C","E"],
    ["S","F","E","S"],
    ["A","D","E","E"]
]


A -> B -> C -> E -> S -> E
A -> B -> C -> E -> S -> 

"ABCESEEEFS"

Problem:
- Don't want to go over the cell more than once, -> visited set(?)
- But we need to be careful in case it's used elsewhere -> backtrack(?)

'''
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def find_path(row: int, col: int, idx: int, visited: set) -> bool:
            if idx >= len(word):
                return True
            
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or (row, col) in visited or board[row][col] != word[idx]:
                return False
            
            visited.add((row, col))
            for dr, dc in DIRECTIONS:
                new_row = row + dr
                new_col = col + dc
                if find_path(new_row, new_col, idx + 1, visited):
                    return True
            
            visited.remove((row, col))
            return False
        
        for r in range(ROWS):
            for c in range(COLS):
                if find_path(r, c, 0, set()): 
                    return True
        return False
            



        