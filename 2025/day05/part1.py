# So I'm not 100% sure where part 2 will go on this one, but I know that I can do the part 1 pretty naively.

ranges: list[tuple[int, int]] = []

while True:
    cur_line = input()
    if len(cur_line) == 0:
        break
    start, end = cur_line.split('-')
    ranges.append((int(start), int(end)))

available: list[int] = []

while True:
    cur_line = input()
    if cur_line == "end":
        break
    available.append(int(cur_line))

num_fresh = 0

for id in available:
    for range in ranges:
        if id >= range[0] and id <= range[1]:
            num_fresh += 1
            break

print(num_fresh)
