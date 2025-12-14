shapes: list[list[str]] = []
puzzles: list[tuple[tuple[int, ...], tuple[int, ...]]] = []

line_buffer: list[str] = []
while (cur_line := input()) != "end":
    if len(shapes) < 6:
        if len(cur_line) == 0:
            shapes.append(line_buffer[1:])
            line_buffer.clear()
        else:
            line_buffer.append(cur_line)
    else:
        tokens = cur_line.split()
        dims = tuple([int(x) for x in tokens[0][:-1].split("x")])
        req_shapes = tuple([int(x) for x in tokens[1:]])
        puzzles.append((dims, req_shapes))

def get_shape_hash_count(shape: list[str]) -> int:
    sum = 0
    for line in shape:
        sum += line.count('#')
    return sum

nontrivial_puzzles = []

total = 0

for puzzle in puzzles:
    required_space = 0
    for i, shape in enumerate(puzzle[1]):
        required_space += get_shape_hash_count(shapes[i]) * shape
    trivially_impossible = required_space > puzzle[0][0] * puzzle[0][1]
    trivially_possible = puzzle[0][0] * puzzle[0][1] > sum(puzzle[1]) * 9
    kindatrivially_possible = puzzle[0][0] * puzzle[0][1] > (puzzle[1][0] + puzzle[1][1] + puzzle[1][2] + puzzle[1][3] + puzzle[1][5]) * 9 + puzzle[1][4] * 6

    if not trivially_impossible:
        total += 1

    if not trivially_impossible and not trivially_possible and not kindatrivially_possible:
        nontrivial_puzzles.append(puzzle)

print(total)

