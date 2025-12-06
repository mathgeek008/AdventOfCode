# We want to know the NUMBER of IDs which are included in these ranges.
# We definitely need to be smart about this one
# I think it might make sense to consolidate the ranges until there's no overlap
# Then we can simply add the differences for each range

ranges: list[tuple[int, int]] = []

while True:
    cur_line = input()
    if len(cur_line) == 0:
        break
    start, end = cur_line.split('-')
    ranges.append((int(start), int(end)))

# Throw out the rest of the input
while True:
    if input() == "end":
        break

ranges.sort(key=lambda x: x[0])
idx = 1
while idx < len(ranges):
    # If the beginning of this range is within the bounds of the range before it,
    if ranges[idx][0] >= ranges[idx - 1][0] and ranges[idx][0] <= ranges[idx - 1][1]:
        # amend the first range, and remove the current range
        ranges[idx - 1] = (ranges[idx - 1][0], max(ranges[idx - 1][1], ranges[idx][1]))
        ranges.pop(idx)
    else:
        idx += 1

num_ids = 0

for range in ranges:
    num_ids += range[1] - range[0] + 1

print(num_ids)
