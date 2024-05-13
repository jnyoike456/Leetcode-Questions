'''
Solution:
- Starting from gates, run BFS while populating the distance of empty rooms


[
    [3,y,0,1],
    [2,2,1,y],
    [1,y,2,y],
    [0,y,3,4]
]

'''
from typing import List
from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWS = len(rooms)
        COLS = len(rooms[0])
        EMPTY_ROOM = 2147483647
        GATE = 0
        def get_neighbors(row: int, col: int) -> List[tuple]:
            directions = [(0,1), (0, -1), (1,0), (-1,0)]
            neighbors = []
            for dr, dc in directions:
                new_r = row + dr
                new_c = col + dc
                if new_r >= 0 and new_r < ROWS and new_c >= 0 and new_c < COLS:
                        neighbors.append((new_r, new_c))
            return neighbors
        
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == GATE:
                    queue.append((r,c))
        
        while queue:
            row, col = queue.popleft()
            dist = rooms[row][col]
            for nei_r, nei_c in get_neighbors(row, col):
                if rooms[nei_r][nei_c] == EMPTY_ROOM:
                    rooms[nei_r][nei_c] = dist + 1
                    queue.append((nei_r, nei_c))
        


        