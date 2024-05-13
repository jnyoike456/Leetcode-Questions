'''
equations[i] = [Ai, Bi] and values[i] -> Ai / Bi = values[i]
queries[j] = [Cj, Dj] 

equations = [["a","b"],["b","c"]], 
values = [2.0,3.0], queries = 

[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

a/b = 2.0
b/c = 3.0


equations = [["a","b"],["b","c"],["bc","cd"]], 
values = [1.5,2.5,5.0], 
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"], [c,a], [bc,a]]

a/b = 1.5
b/c = 2.5
bc/cd = 5.0

a/c -> a/b*b/c -> 
c/b -> 1/(b/c) -> 
bc/cd -> 
cd/bc -> 1/(bc/cd)
c/a -> 1/(a/c)




a -> (b, 1.5)
b -> (a, 1/1.5), (c, 2.5)
c -> (b, 1/2.5)
bc -> (cd, 5)
cd -> (bc, 1/5)




a, bc

a,b,c <- keep track of the path and if the destination is not in the path generated then it's -1
1*1.5*2.5


equations = [["a","b"]], 
values = [0.5], 
queries = [["a","b"],["b","a"],["a","c"],["x","y"]]

a -> b, 0.5
b -> a, 1/0.5

a -> b

(a, 1), (b, 0.5)

(b, 1), (a, 1/0.5)

a,1), b()


Time - O(V + E) -> O(2n + 2n)

Observations:
- What if we could represent the equations and values and a weighted directed graph. 
- query -> what is the weight of the path between the two values. 

1. can evaluate the path weight between the query 
    - if source is destination, return 1
2. we can't
    - one or both of the query items is not in the graph
    - both are in the graph but are part of different connected components

'''
from collections import defaultdict, deque
from typing import List
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        result = []
        for i, equation in enumerate(equations):
            source, target = equation
            weight = values[i]
            graph[source].append((target, weight))
            graph[target].append((source, 1/weight))
        
        def bfs(source: str, target: str) -> float:
            queue = deque()
            queue.append((source, 1))

            visited = set()
            visited.add(source)
            while queue:
                node, weight = queue.popleft()
                if node == target:
                    return weight
                
                for neighbor in graph[node]:
                    if neighbor[0] not in visited:
                        new_weight = neighbor[1] * weight
                        visited.add(neighbor[0])
                        queue.append((neighbor[0], new_weight))
            return -1
        
        for query in queries:
            source, target = query
            if source not in graph or target not in graph:
                result.append(-1)
                continue
            weight = bfs(source, target)
            result.append(weight)
        return result

            

                    
                
            
        