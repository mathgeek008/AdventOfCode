grid: list[str] = []

# For part 2, we can do the same process as pat 1, but record the number of adjacent @ in some kind of grid.
# Then, we can simply do several passes of these until we can't anymore.
# There may be a more clever solution to the problem but I like this one.

while True:
    cur_line = input()
    if cur_line == "end":
        break
    grid.append('.' + cur_line + '.')

line_width = len(grid[0])
grid.insert(0, '.' * line_width)
grid.append('.' * line_width)

grid_height = len(grid)

def check_adjacents(r, c) -> int:
    sum = 0
    if grid[r - 1][c - 1] == '@':
        sum += 1
    if grid[r - 1][c] == '@':
        sum += 1
    if grid[r - 1][c + 1] == '@':
        sum += 1
    if grid[r][c + 1] == '@':
        sum += 1
    if grid[r][c - 1] == '@':
        sum += 1
    if grid[r + 1][c - 1] == '@':
        sum += 1
    if grid[r + 1][c] == '@':
        sum += 1
    if grid[r + 1][c + 1] == '@':
        sum += 1
    return sum

# -1 indicates that there is no @ in that particular position

adj_grid: list[list[int]] = []
for i in range(grid_height):
    adj_grid.append([])
    for j in range(line_width):
        adj_grid[i].append(-1)

# We need to use a pair of indexes so that we have finer control of where we are in the grid
for i in range(1, grid_height - 1):
    for j in range(1, line_width - 1):
        if grid[i][j] == '@':
            adj_grid[i][j] = check_adjacents(i, j)

# Now we need to go through this grid until we can't anymore. We'll keep track of whether or not the removed total changed.

def decrement_adjacents(r, c) -> None:
    adj_grid[r - 1][c - 1] -= 1
    adj_grid[r - 1][c] -= 1
    adj_grid[r - 1][c + 1] -= 1
    adj_grid[r][c - 1] -= 1
    adj_grid[r][c + 1] -= 1
    adj_grid[r + 1][c - 1] -= 1
    adj_grid[r + 1][c] -= 1
    adj_grid[r + 1][c + 1] -= 1

total_removed = 0
previous_total_removed = -1

while previous_total_removed != total_removed:
    previous_total_removed = total_removed
    for i in range(1, grid_height - 1):
        for j in range(1, line_width - 1):
            if adj_grid[i][j] >= 0 and adj_grid[i][j] < 4:
                adj_grid[i][j] = -1
                total_removed += 1
                decrement_adjacents(i, j)

print(total_removed)