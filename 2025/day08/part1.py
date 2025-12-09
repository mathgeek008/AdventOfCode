import math

type Coordinate = tuple[int, int, int]
coords: list[Coordinate] = []

while (cur_line := input()) != 'end':
    cur_coords = cur_line.split(',')
    coords.append((int(cur_coords[0]), int(cur_coords[1]), int(cur_coords[2])))

def get_dist(a: Coordinate, b: Coordinate) -> float:
    delta_x = a[0] - b[0]
    delta_y = a[1] - b[1]
    delta_z = a[2] - b[2]
    sum_of_squares = delta_x * delta_x + delta_y * delta_y + delta_z * delta_z
    return math.sqrt(sum_of_squares)

# I think we can afford to just find the distances between each pair of junction boxes.
# How should we store this data? We can find all the pairings, store as tuples, then sort

dists_pairs: list[tuple[float, tuple[Coordinate, Coordinate]]] = []

for i, c1 in enumerate(coords[:-1]):
    for j, c2 in enumerate(coords[i + 1:]):
        dists_pairs.append((get_dist(c1, c2), (c1, c2)))

# Sort by the distance ascending
dists_pairs.sort(key=lambda x: x[0])

# Now, we need to have these coordinates go into an adjacency list
# Tuples are hashable, so we should be able to use a dictionary for this

# This adjacency list is going to be a bit special. Instead of only maintaining immediate neighbours,
# each coordinate maintains a list of ALL the connected nodes.

# We can simple combine the lists when we're putting them together.

adj_list: dict[Coordinate, set[Coordinate]] = {}
for c in coords:
    adj_list[c] = {c}

for i in range(1000):
    a, b = dists_pairs[i][1]
    # If a isn't in b, then b isn't in a.
    if not a in adj_list[b]:
        combined = adj_list[a].union(adj_list[b])
        for c in combined:
            adj_list[c] = combined

# Now, we want to have a set of all the unique sets lol
circuits = set(frozenset(x) for x in adj_list.values())
circuit_lengths = sorted([len(c) for c in circuits], reverse=True)
result = circuit_lengths[0] * circuit_lengths[1] * circuit_lengths[2]

print(result)
