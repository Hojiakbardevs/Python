from collections import deque

def find_giant_loop(sketch):
    # Convert the sketch to a 2D grid
    grid = [list(row) for row in sketch.split('\n') if row]

    # Find the starting position
    start_row = next(i for i, row in enumerate(grid) for 'S' in row)
    start_col = grid[start_row].index('S')

    # Define the directions: north, south, west, east
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def is_valid(row, col):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != '.'

    # Calculate distances using BFS
    distances = [[float('inf')] * len(grid[0]) for _ in range(len(grid))]
    distances[start_row][start_col] = 0
    queue = deque([(start_row, start_col)])

    while queue:
        current_row, current_col = queue.popleft()

        for dr, dc in directions:
            new_row, new_col = current_row + dr, current_col + dc

            if is_valid(new_row, new_col) and distances[new_row][new_col] == float('inf'):
                distances[new_row][new_col] = distances[current_row][current_col] + 1
                queue.append((new_row, new_col))

    # Find the maximum distance in the loop
    max_distance = max(max(row) for row in distances)

    return max_distance

# Your example sketch
sketch = """
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
"""

result = find_giant_loop(sketch)
print(result)
