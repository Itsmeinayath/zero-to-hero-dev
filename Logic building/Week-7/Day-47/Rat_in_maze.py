#  Rat in maze problem using backtracking

from typing import List

class Solution:
    def findPath(self,m: List[List[int]], n: int) -> List[str]:
        result = []
        visited = [[False for _ in range(n)] for _ in range(n) ]
        def is_safe(r,c):
            return 0 <= r < n and  0 <= c and m[r][c] == 1 and not visited[r][c]
        
        def backtrack(r, c, path):
            if r == n-1 and c == n-1:
                result.append(path)
                return
            # Mark as visited
            visited[r][c] = True 
            # Explore all 4 directions

            if is_safe(r+1, c): backtrack(r+1,c, path + 'D')
            if is_safe(r, c-1): backtrack(r, c-1, path + 'L')
            if is_safe(r, c+1): backtrack(r, c+1, path + 'R')
            if is_safe(r-1, c): backtrack(r-1, c, path + 'U')

            visited[r][c] = False  # Backtrack
        if m[0][0] == 1:
            backtrack(0,0,"")
        return result
    
# Example usage
if __name__ == "__main__":
    maze = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 1]
    ]
    n = len(maze)
    sol = Solution()
    paths = sol.findPath(maze, n)
    print("Possible paths from start to end:")
    for p in paths:
        print(p)    
if not paths:
    print("No path found.")
    

