type pos = tuple[int, int]

coords : list[pos] = []

while (cur_line := input()) != 'end':
    coords_str = cur_line.split(',')
    coords.append((int(coords_str[0]), int(coords_str[1])))

# We can simply try every pair of coordinates to find the largest rectangle

largest = 0
for i, a in enumerate(coords[:-1]):
    for j, b in enumerate(coords[i + 1:]):
        area = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
        largest = max(largest, area)

print(largest)