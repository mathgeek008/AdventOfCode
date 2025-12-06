grid: list[str] = []

# We basically have a big rectangle of . around the whole thing.
# Instead of handling the literal edge cases, let's just add these ourselves

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

num_accessible_rolls = 0

# We need to use a pair of indexes so that we have finer control of where we are in the grid
for i in range(1, grid_height - 1):
    for j in range(1, line_width - 1):
        if grid[i][j] == '@':
            if check_adjacents(i, j) < 4:
                num_accessible_rolls += 1

print(num_accessible_rolls)
