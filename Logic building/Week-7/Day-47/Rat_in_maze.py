#  Rat in maze problem using backtracking

from typing import List

class Solution:
    def findPath(self,m: List[List[int]], n: int) -> List[str]:
        result = []
        visited = [[False for _ in range(n)] for _ in range(n) ]
        def is_safe(r,c):
            return 0 <= r < n and  0 <= c and m[r][c] == 1 and not visited[r][c]
        
        def backtrack(r, c, path):

