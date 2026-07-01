# 2812. Find the Safest Path in a Grid

## Problem

You are given a 0-indexed 2D matrix `grid` of size `n x n`, where
`grid[r][c] = 1` marks a cell containing a thief and `grid[r][c] = 0` marks an
empty cell.

Starting at cell `(0, 0)`, in one move you can move to any adjacent cell
(up, down, left, right), including cells containing thieves.

The **safeness factor** of a path is the minimum Manhattan distance from any
cell on the path to any thief in the grid. Return the **maximum** safeness
factor over all paths from `(0, 0)` to `(n - 1, n - 1)`.

Constraints:
- `1 <= grid.length == n <= 400`
- `grid[i].length == n`
- `grid[i][j]` is either `0` or `1`.
- There is at least one thief in the grid.

---

## Examples

### Example 1
**Input:**
```
grid = [[1,0,0],[0,0,0],[0,0,1]]
```
**Output:** `0`

All paths from `(0, 0)` to `(n - 1, n - 1)` pass through the thieves at
`(0, 0)` and `(n - 1, n - 1)`.

### Example 2
**Input:**
```
grid = [[0,0,1],[0,0,0],[0,0,0]]
```
**Output:** `2`

### Example 3
**Input:**
```
grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
```
**Output:** `2`

---

## Approach

1. **Multi-source BFS** from every thief simultaneously fills each cell with
   its Manhattan distance to the nearest thief (BFS layers on a 4-directional
   grid correspond exactly to Manhattan distance).
2. **Maximize the bottleneck path** with a max-heap Dijkstra variant. The
   safeness of a path is the minimum cell distance along it, so we always
   expand the reachable cell whose best-so-far safeness is largest. A
   neighbour's safeness is `min(current safeness, dist[neighbour])`. When the
   target `(n - 1, n - 1)` is popped, its recorded safeness is the answer.

---

## Complexity

- Time Complexity: `O(n^2 log n)` — heap operations over `n^2` cells
- Space Complexity: `O(n^2)` — distance grid, heap and visited set

---

## Solution

[solution.py](./solution.py)
