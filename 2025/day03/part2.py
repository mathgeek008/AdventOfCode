joltages = []

while True:
    joltage = input()
    if joltage == 'end':
        break
    else:
        joltages.append(joltage)

def find_leftmost_largest(j: str) -> tuple[str, int]:
    largest = sorted(j, reverse=True)[0]
    idx = j.find(largest)
    return (largest, idx)

result = 0

for joltage in joltages:
    overall_index = -1
    for i in range(11, 0, -1):
        val, idx = find_leftmost_largest(joltage[overall_index + 1:(-1 * i)])
        overall_index += idx + 1
        result += int(val) * 10 ** i
    val, _ = find_leftmost_largest(joltage[overall_index + 1:])
    result += int(val)

print(result)
    