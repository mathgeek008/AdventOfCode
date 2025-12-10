import bisect

type pos = tuple[int, int]

coords: list[pos] = []

while (cur_line := input()) != 'end':
    coords_str = cur_line.split(',')
    coords.append((int(coords_str[0]), int(coords_str[1])))

perimeter: list[pos] = []

for i, c in enumerate(coords):
    next_coord = coords[(i + 1) % len(coords)]
    # Let's add a coordinate for each one of these points, except for the end one (it will get added in the next loop)
    x_diff = c[0] - next_coord[0]
    y_diff = c[1] - next_coord[1]
    if x_diff != 0:
        xds = x_diff // abs(x_diff)
        for j in range(c[0], next_coord[0], -1 * xds):
            perimeter.append((j, c[1]))
    elif y_diff != 0:
        yds = y_diff // abs(y_diff)
        for j in range(c[1], next_coord[1], -1 * yds):
            perimeter.append((c[0], j))

perimeter.sort(key=lambda x: x[0])
perim_x = [x[0] for x in perimeter]

# Let's precompute a list of ALL the squares, then work in reverse order of size until we find one containing no perimeter.
all_square_sizes: list[tuple[int, tuple[pos, pos]]] = []
for i, a in enumerate(coords[:-1]):
    for j, b in enumerate(coords[i + 1:]):
        area = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
        all_square_sizes.append((area, (a, b)))

all_square_sizes.sort(key=lambda x: x[0], reverse=True)

for size, cs in all_square_sizes:
    a, b = cs
    valid = True
    left_point = bisect.bisect_left(perim_x, min(a[0], b[0]) + 1)
    right_point = bisect.bisect_right(perim_x, max(a[0], b[0]) - 1)
    for p in perimeter[left_point:right_point]:
        if p[1] > min(a[1], b[1]) and p[1] < max(a[1], b[1]):
            valid = False
            break
    if valid:
        print(size)
        break

