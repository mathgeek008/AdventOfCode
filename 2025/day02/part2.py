raw_input = input()

ranges_raw = raw_input.split(',')
ranges = []
for r in ranges_raw:
    x, y = r.split('-')
    ranges.append((int(x), int(y)))

def split_string_into_equal_parts_and_compare(s: str, p: int) -> bool:
    l = len(s)
    if l % p != 0:
        return False
    seg = l // p
    parts = set()
    for i in range(0, l, seg):
        parts.add(s[i:i + seg])
    
    return len(parts) == 1

def is_repeating(x):
    x_str = str(x)
    for i in range(2, 10):
        if split_string_into_equal_parts_and_compare(x_str, i):
            return True
    return False
            
invalid_id_sum = 0

for low, high in ranges:
    for i in range(low, high + 1):
        if is_repeating(i):
            invalid_id_sum += i

print(invalid_id_sum)
