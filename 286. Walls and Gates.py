# 286. Walls and Gates
# You are given a m x n 2D grid initialized with these three possible values.

# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

# Example: 

# Given the 2D grid:

# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF
# After running your function, the 2D grid should be:

#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4
from collections import deque

def wallsAndGates(rooms):
    if not rooms or not rooms[0]:
        return

    m, n = len(rooms), len(rooms[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def bfs(start):
        queue = deque([(start[0], start[1], 0)])

        while queue:
            x, y, distance = queue.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and rooms[nx][ny] == 2147483647:
                    rooms[nx][ny] = distance + 1
                    queue.append((nx, ny, distance + 1))

    for i in range(m):
        for j in range(n):
            if rooms[i][j] == 0:
                bfs((i, j))


