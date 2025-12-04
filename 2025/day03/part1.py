joltages = []

while True:
    joltage = input()
    if joltage == 'end':
        break
    else:
        joltages.append(joltage)

# We can greedily take the largest number in the list, and find the largest number to its right
# In other words, this is kind of a recursive problem in a way.

def find_leftmost_largest(j: str) -> tuple[str, int]:
    largest = sorted(j, reverse=True)[0]
    idx = j.find(largest)
    return (largest, idx)

result = 0

for joltage in joltages:
    tens, idx = find_leftmost_largest(joltage[:-1])
    ones, _ = find_leftmost_largest(joltage[idx + 1:])
    result += int(tens) * 10 + int(ones)

print(result)
    