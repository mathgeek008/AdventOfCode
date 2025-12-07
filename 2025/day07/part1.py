grid: list[list[str]] = []

while True:
    cur_line = input()
    if cur_line == "end":
        break
    grid.append([c for c in cur_line])

start_pos = grid[0].index('S')

num_splits = 0

# We need to keep track of where rays have already been, so that we never double-count
# We can probably just change the . in the grid to a |, like in the example

def draw_ray(row: int, col: int) -> None:
    global num_splits
    cur_pos = grid[row][col]
    while (cur_pos == '.'):
        grid[row][col] = '|'
        row += 1
        if row >= len(grid):
            return
        cur_pos = grid[row][col]
    if cur_pos == '|':
        return
    elif cur_pos == '^':
        num_splits += 1
        draw_ray(row, col - 1)
        draw_ray(row, col + 1)

draw_ray(1, start_pos)

print(num_splits)