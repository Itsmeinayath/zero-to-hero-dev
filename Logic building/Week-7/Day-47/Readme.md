# Day 47 — Backtracking on Grids 🎯

**Topic**: N-Queens & Rat in a Maze

---

## 📚 Overview

Today we tackled the **most famous applications** of Backtracking:

1. **N-Queens** - Constraint satisfaction (no attacking queens)
2. **Rat in a Maze** - Pathfinding with obstacles

**The Pattern**: Choose (Mark) → Explore (Recurse) → Unchoose (Unmark)

---

## 🎯 TL;DR - Key Techniques

| Problem | Challenge | Solution | Tracking |
|---------|-----------|----------|----------|
| **N-Queens** | Place N queens without attacks | 3 Sets for O(1) checks | `cols`, `pos_diag`, `neg_diag` |
| **Rat in a Maze** | Navigate grid avoiding cycles | Visited matrix | `visited[r][c]` boolean |

---

## 💡 Core Concepts

### Grid Backtracking Pattern

```
1. Check if current position is valid/safe
2. CHOOSE: Mark position as used
3. EXPLORE: Recursively try next positions
4. UNCHOOSE: Unmark position (backtrack!)
```

### Why Grids Are Special

```
Linear problems:    [1, 2, 3, 4]
                    ↓ One direction

Grid problems:      . . . .
                    . X . .  ← Multiple directions!
                    . . . .  (Up, Down, Left, Right)
                    . . . .
```


---

## 🎨 Pattern 1: N-Queens (LeetCode 51)

**The Challenge**: Place N queens on an N×N chessboard so no two queens attack each other.

### Problem Statement

> A queen can attack any piece in the same row, column, or diagonal.

**Example for N=4**:
```
Solution 1:        Solution 2:
. Q . .            . . Q .
Q . . .            Q . . .
. . . Q            . . . Q
. . Q .            . Q . .
```

---

### 💡 The Attack Lines Math

**Key Insight**: Use math formulas instead of scanning the board!

```
For any cell (r, c):

Column:            c (same for entire column)
Positive Diagonal: r + c (constant along ↗ diagonal)
Negative Diagonal: r - c (constant along ↘ diagonal)

Example 4x4 board:

Columns (c):
  0 1 2 3
0 . . . .
1 . . . .
2 . . . .
3 . . . .

Positive Diagonals (r+c):
  0 1 2 3
0 0 1 2 3
1 1 2 3 4
2 2 3 4 5
3 3 4 5 6

Negative Diagonals (r-c):
   0  1  2  3
0  0 -1 -2 -3
1  1  0 -1 -2
2  2  1  0 -1
3  3  2  1  0
```

**If any of these are already in our sets → Attack detected!**

---

### 🌳 Visual: Decision Tree for N=4 (Partial)

```
Row 0: Try each column
         []
    /    |    |    \
   c0   c1   c2   c3
   
Row 1: Try safe columns
   c0
   |
   ❌c0 ❌c1 ✅c2 ❌c3
              |
Row 2:       c2
         /   |   \
       ❌c0 ❌c1 ❌c2 ❌c3 (no safe position!)
       (All attacked by Q at (0,0) and (1,2))
       Backtrack! ⬅️

Try next position at Row 1...
   c0
   |
   ❌c0 ❌c1 ❌c2 ✅c3
              |
Row 2:       c3
         /   |   \
       ✅c1 ...
       
Continue until valid solution found...

✅ Solution: [(0,1), (1,3), (2,0), (3,2)]

Board:
. Q . .
. . . Q
Q . . .
. . Q .
```

---

### 🔍 Step-by-Step Trace: N=4 (First Solution)

```
Initial: cols={}, pos_diag={}, neg_diag={}

Row 0: Try columns 0,1,2,3
       ├─ c=0: SKIP (leads to no solution)
       └─ c=1: SAFE ✅
          CHOOSE: cols={1}, pos_diag={1}, neg_diag={-1}
          Board[0][1] = 'Q'
          
          Row 1: Try columns 0,1,2,3
                 ├─ c=0: SKIP (col 0 conflicts)
                 ├─ c=1: SKIP (col 1 used)
                 ├─ c=2: SKIP (pos_diag conflicts)
                 └─ c=3: SAFE ✅
                    CHOOSE: cols={1,3}, pos_diag={1,4}, neg_diag={-1,-2}
                    Board[1][3] = 'Q'
                    
                    Row 2: Try columns 0,1,2,3
                           ├─ c=0: SAFE ✅
                              CHOOSE: cols={1,3,0}, pos_diag={1,4,2}...
                              Board[2][0] = 'Q'
                              
                              Row 3: Try columns 0,1,2,3
                                     ├─ c=0: SKIP (col 0 used)
                                     ├─ c=1: SKIP (col 1 used)
                                     ├─ c=2: SAFE ✅
                                        CHOOSE: All sets updated
                                        Board[3][2] = 'Q'
                                        
                                        Row 4: r==n → SOLUTION FOUND! ✅
                                        Save: [".Q..", "...Q", "Q...", "..Q."]
                                        
                                        UNCHOOSE (3,2)
                                     UNCHOOSE (2,0)
                           ...backtrack and try other positions...

First solution found: [".Q..", "...Q", "Q...", "..Q."]
```

---

### 📝 Implementation

```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()        # Tracks occupied columns
        pos_diag = set()    # Tracks occupied positive diagonals (r+c)
        neg_diag = set()    # Tracks occupied negative diagonals (r-c)
        result = []
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            # Base Case: Placed queens in all rows
            if r == n:
                # Convert board to required format
                result.append(["".join(row) for row in board])
                return

            # Try placing queen in each column of current row
            for c in range(n):
                # Check if position is under attack
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue  # Skip unsafe position

                # --- Golden Rule ---
                # 1. CHOOSE
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"

                # 2. EXPLORE
                backtrack(r + 1)  # Move to next row

                # 3. UNCHOOSE
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."

        backtrack(0)  # Start from row 0
        return result
```

**Key Points**:
- ✅ Process row by row (only one queen per row)
- ✅ Use 3 sets for O(1) attack detection
- ✅ Math formulas: `r+c` and `r-c` identify diagonals
- ✅ Backtrack removes queen and clears sets

---

### ⏱️ Complexity Analysis

- **Time**: **O(N!)**
  - Row 0: N choices
  - Row 1: ~N-1 choices (avoid column)
  - Row 2: ~N-2 choices (avoid columns and diagonals)
  - Total: N × (N-1) × (N-2) × ... ≈ O(N!)

- **Space**: **O(N²)**
  - Board: O(N²)
  - Sets: O(N) each × 3 = O(N)
  - Call stack: O(N)
  - Total: O(N²)

---

## 🎨 Pattern 2: Rat in a Maze (GeeksforGeeks)

**The Challenge**: Find all paths from (0,0) to (n-1,n-1) in a maze with obstacles.

### Problem Statement

> Given a maze where 1 = open cell, 0 = blocked cell. Find all paths using moves: Down (D), Left (L), Right (R), Up (U).

**Example**:
```
Input maze (4x4):
1 1 0 0
1 1 1 0
1 0 1 1
0 0 1 1

Output: ["DDRDRR", "DRDDRR"]
```

---

### 🌳 Visual: Path Exploration

```
Maze:           Path 1:         Path 2:
1 1 0 0         S→→. .         S . . .
1 1 1 0         ↓ →→. .         ↓ . . .
1 0 1 1         ↓ . →→E         →→→→. .
0 0 1 1         . . . .         . . →→E

S = Start (0,0)
E = End (3,3)
```

---

### 🔍 Decision Tree for Simple 3x3 Maze

```
Maze:
1 1 0
1 1 1
0 1 1

                    (0,0) ""
                    /    \
            Down(1,0)    Right(0,1)
              "D"           "R"
             /   \         /    \
          D(2,0) R(1,1) D(1,1) R(0,2)❌
           ❌     "DR"    "RD"   (blocked)
                 /  \     /  \
            D(2,1) R(1,2) D(2,1) R(1,2)
            "DRD"  "DRR"  "RDD"  "RDR"
              |      |      |      |
           R(2,2) D(2,2) R(2,2) D(2,2)
           "DRDR" "DRRD" "RDDR" "RDRD"
             ✅     ❌     ❌     ✅

Valid paths: ["DRDR", "RDRD"]

Note: ❌ means blocked cell or out of bounds
```

---

### 🗺️ Visual: Visited Matrix in Action

```
Step 1: Start at (0,0)
Visited:        Maze:
T F F          1 1 0
F F F          1 1 1
F F F          0 1 1

Step 2: Move Down to (1,0)
Visited:        Current Path: "D"
T F F
T F F
F F F

Step 3: Move Right to (1,1)
Visited:        Current Path: "DR"
T F F
T T F
F F F

Step 4: Dead end, Backtrack to (1,0)
Visited:        Current Path: "D"
T F F          ↑ Unmark (1,1)
T F F          (backtrack!)
F F F

Step 5: Try Down from (1,0) to (2,0)
Visited:        Current Path: "DD"
T F F          ❌ Blocked! (maze[2][0] = 0)
T F F
F F F

Backtrack and try other paths...
```

---

### 📝 Implementation

```python
class Solution:
    def findPath(self, m: List[List[int]], n: int) -> List[str]:
        result = []
        visited = [[False] * n for _ in range(n)]
        
        def is_safe(r, c):
            """Check if cell is valid and not visited"""
            return (0 <= r < n and 
                    0 <= c < n and 
                    m[r][c] == 1 and 
                    not visited[r][c])

        def backtrack(r, c, path):
            # Base Case: Reached destination
            if r == n-1 and c == n-1:
                result.append(path)
                return

            # --- Golden Rule ---
            # 1. CHOOSE
            visited[r][c] = True
            
            # 2. EXPLORE (try all 4 directions in lexicographical order)
            # Down
            if is_safe(r+1, c):
                backtrack(r+1, c, path + "D")
            # Left
            if is_safe(r, c-1):
                backtrack(r, c-1, path + "L")
            # Right
            if is_safe(r, c+1):
                backtrack(r, c+1, path + "R")
            # Up
            if is_safe(r-1, c):
                backtrack(r-1, c, path + "U")
            
            # 3. UNCHOOSE
            visited[r][c] = False  # Allow this cell in other paths!

        # Start exploring if starting cell is open
        if m[0][0] == 1:
            backtrack(0, 0, "")
        
        return result
```

**Key Points**:
- ✅ `visited` matrix prevents cycles in current path
- ✅ Try directions in order: D, L, R, U (lexicographical)
- ✅ Unmark `visited[r][c]` when backtracking
- ✅ `is_safe()` checks bounds, obstacles, and visited

---

### ⏱️ Complexity Analysis

- **Time**: **O(4^(N²))**
  - Each cell can branch to 4 directions
  - Maximum N² cells in path
  - Worst case: 4 × 4 × 4 × ... (N² times)
  - Exponential: O(4^(N²))

- **Space**: **O(N²)**
  - `visited` matrix: O(N²)
  - Call stack (path length): O(N²) worst case
  - Total: O(N²)

---

## 📊 Pattern Comparison

| Aspect | N-Queens | Rat in a Maze |
|--------|----------|---------------|
| **Grid Type** | N×N chessboard | N×N maze with obstacles |
| **Goal** | Place all queens safely | Find all paths to destination |
| **Constraint** | No attacks (row/col/diag) | No obstacles, no cycles |
| **Tracking** | 3 Sets (cols, diagonals) | `visited` matrix |
| **Direction** | Row by row (top to bottom) | 4 directions (D, L, R, U) |
| **Validation** | Check 3 sets | Check bounds + obstacles + visited |
| **Base Case** | Placed N queens | Reached (n-1, n-1) |
| **Unchoose** | Remove from sets + clear board | Mark `visited[r][c] = False` |

---

## 🎓 The Grid Backtracking Template

```python
def grid_backtrack(position, state):
    # 1. Base Case (goal reached or invalid)
    if at_goal(position):
        save_solution()
        return
    
    # 2. Try all valid moves
    for next_position in get_valid_moves(position):
        
        # 3. Check if safe/valid
        if not is_safe(next_position):
            continue
        
        # 4. CHOOSE (mark as used)
        mark_used(next_position)
        
        # 5. EXPLORE (recurse)
        grid_backtrack(next_position, updated_state)
        
        # 6. UNCHOOSE (unmark for other paths)
        mark_unused(next_position)
```

---

## 🔑 Key Takeaways

1. **N-Queens uses math**: `r+c` and `r-c` for O(1) diagonal checks
2. **Rat in Maze uses visited matrix**: Prevents infinite loops
3. **Always unchoose**: Critical for exploring alternative paths
4. **Grid = Multiple directions**: Unlike linear problems
5. **Order matters**: D, L, R, U for lexicographical output
6. **Both are exponential**: N-Queens O(N!), Maze O(4^(N²))
7. **Sets vs Matrix**: Choose based on what you're tracking

---

**Made with ❤️ for mastering Grid Backtracking**
