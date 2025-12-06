# While part 1 was very straightforward, part 2 seems to be a challenge of input parsing.
# Nothing too crazy
# Question: will the operator always be on the bottom-leftmost position?
# That seems to be the case but it's very hard to tell from the input data

in_data: list[str] = []

while True:
    cur_line = input()
    if cur_line == 'end':
        break
    in_data.append(cur_line)

num_rows = len(in_data)
num_cols = len(in_data[0])

# We can go from right to left - each problem is delineated by the fact that we've seen an operator (plus a column of empty space)

total = 0
nums_buffer = []
skip_next = False
for i in range(num_cols - 1, -1, -1):
    if skip_next:
        skip_next = False
        continue
    nums = [int(r[i]) for r in in_data[:-1] if r[i].isnumeric()]
    resolved = 0
    p = 0
    for n in reversed(nums):
        resolved += n * 10 ** p
        p += 1
    
    nums_buffer.append(resolved)

    op = in_data[-1][i]
    if op in {'*', '+'}:
        result = nums_buffer[0]
        if op == '*':
            for n in nums_buffer[1:]:
                result *= n
        elif op == '+':
            for n in nums_buffer[1:]:
                result += n
        nums_buffer.clear()
        total += result
        skip_next = True

print(total)