raw_input = input()

ranges_raw = raw_input.split(',')
ranges = []
for r in ranges_raw:
    x, y = r.split('-')
    ranges.append((int(x), int(y)))

def is_repeating(x):
    x_str = str(x)
    lenx = len(x_str)
    if lenx % 2 == 0:
        return x_str[:lenx // 2] == x_str[lenx // 2:]

invalid_id_sum = 0

for low, high in ranges:
    for i in range(low, high + 1):
        if is_repeating(i):
            invalid_id_sum += i

print(invalid_id_sum)
