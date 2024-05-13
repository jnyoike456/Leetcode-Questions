'''
1. For all O's at the borders, we want to find the paths from them, so we know that we cannot flip those
    For each O on the border that is not visited, run BFS on it
2. Go over the matrix and flip those that can be flipped

'''
from collections import deque
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        def get_neighbors(x: int, y: int, visited: set) -> list:
            neighbors = []
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy
                if new_x >= 0 and new_x < rows and new_y >= 0 and new_y < cols:
                    if (new_x, new_y) not in visited:
                        neighbors.append((new_x, new_y))
                        visited.add((new_x, new_y))
            return neighbors
        
        def bfs(x: int, y: int, visited: set) -> None:
            queue = deque()
            visited.add((x,y))
            queue.append((x,y))

            while len(queue) > 0:
                x, y = queue.popleft()
                for new_x, new_y in get_neighbors(x, y, visited):
                    if board[new_x][new_y] == "O":
                        queue.append((new_x, new_y))
        
        visited = set()
        for c in range(cols):
            if (0,c) not in visited and board[0][c] == "O":
                bfs(0, c, visited)
            if (rows - 1,c) not in visited and board[rows - 1][c] == "O":
                bfs(rows - 1, c, visited)
        
        for r in range(rows):
            if (r,0) not in visited and board[r][0] == "O":
                bfs(r, 0, visited)
            if (r, cols - 1) not in visited and board[r][cols - 1] == "O":
                bfs(r, cols - 1, visited)
        
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if board[r][c] == "O" and (r,c) not in visited:
                    board[r][c] = "X"


        



        