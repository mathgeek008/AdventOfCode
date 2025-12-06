in_data: list[list[str]] = []

while True:
    cur_line = input()
    if cur_line == 'end':
        break
    in_data.append(cur_line.split())

num_rows = len(in_data)
num_cols = len(in_data[0])

total = 0
for i in range(num_cols):
    op = in_data[-1][i]
    nums = [r[i] for r in in_data[:-1]]
    result = int(nums[0])
    if op == '+':
        for n in nums[1:]:
            result += int(n)
    elif op == '*':
        for n in nums[1:]:
            result *= int(n)
    total += result

print(total)