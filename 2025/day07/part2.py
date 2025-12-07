grid: list[list[str]] = []

while True:
    cur_line = input()
    if cur_line == "end":
        break
    grid.append([c for c in cur_line])

start_pos = grid[0].index('S')

# Isn't this just the same problem but we remove dedupe check?
# Nope - that's way too time-expensive.
# This might be the first problem that requires some good algorithmic thinking!
# Let's work backwards. Looking at the last set of split points, if we know *how many ways* to get to each of them, the problem would be solved easily.
# All we need to know to determine that is, for the layer above, in how many timelines could we have gotten to those splits?

# Actually this is a graph theory problem!
# We go from the top-down. Each of the split point "affects" some number of other split points.
# We can determine this pretty cheaply.
# Then we can determine the total number of timelines by summing the number of timelines in each "leaf", times two??

# We start by constructing this relationship between splitting nodes

# I think I was overthinking it the whole time before. It *would* have worked, but would have had more complex overhead than this new strategy.
# Start by going to every caret and replacing it with a 0.
# Then, go layer-by-layer. For the very first layer caret, we simply set it to 1.
# Then, for each caret on each layer, we determine which carets in lower layers will be affected. We increment those numbers by our number
# If at any point a caret does NOT affect another caret, then it's an "end timeline" and should be added to the total.
# If this happens twice then we simply add our timeline number twice.
# This also account for carets with values of 0 - we don't even need to skip these!

for i, line in enumerate(grid):
    for j, char in enumerate(line):
        if char == '^':
            grid[i][j] = '0'

# Simulate the first ray
grid[2][start_pos] = '1'

total = 0

def draw_ray(row: int, col: int, to_add: int) -> None:
    global total
    cur_pos = grid[row][col]
    while (cur_pos == '.'):
        row += 1
        if row >= len(grid):
            total += to_add
            break
        cur_pos = grid[row][col]
    if cur_pos.isnumeric():
        grid[row][col] = str(int(grid[row][col]) + to_add)

def print_grid():
    for line in grid:
        print(''.join(line))
    print()

for i in range(2, len(grid), 2):
    row = grid[i]
    for j, char in enumerate(row):
        if char.isnumeric():
            draw_ray(i, j - 1, int(char))
            draw_ray(i, j + 1, int(char))

print(total)

