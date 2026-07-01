"""
2812. Find the Safest Path in a Grid
Difficulty: Medium

Approach:
- Multi-source BFS from every thief to compute, for each cell, the Manhattan
  distance to the nearest thief (BFS on a grid yields Manhattan distance).
- Then find the path from (0, 0) to (n - 1, n - 1) that maximizes the minimum
  cell distance along it. This is a "maximize the bottleneck" problem, solved
  with a max-heap (Dijkstra variant): always expand the reachable cell whose
  safeness (min distance seen so far on its best path) is largest.
- The safeness of a neighbour is min(current path safeness, dist[neighbour]).
  When we pop the target cell, its recorded safeness is the answer.

Time Complexity: O(n^2 log n) — heap operations over n^2 cells
Space Complexity: O(n^2) — distance grid, heap and visited set
"""

import heapq
from collections import deque
from typing import List


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dist = [[-1] * n for _ in range(n)]
        queue: deque[tuple[int, int]] = deque()

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    queue.append((r, c))

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        # Multi-source BFS: fill each cell with distance to nearest thief.
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))

        # Max-heap Dijkstra: maximize the minimum distance along the path.
        # Store negative safeness because heapq is a min-heap.
        heap = [(-dist[0][0], 0, 0)]
        safeness = [[-1] * n for _ in range(n)]
        safeness[0][0] = dist[0][0]

        while heap:
            neg_safe, r, c = heapq.heappop(heap)
            safe = -neg_safe

            if r == n - 1 and c == n - 1:
                return safe

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    new_safe = min(safe, dist[nr][nc])
                    if new_safe > safeness[nr][nc]:
                        safeness[nr][nc] = new_safe
                        heapq.heappush(heap, (-new_safe, nr, nc))

        return 0  # pragma: no cover — unreachable, grid is fully connected
