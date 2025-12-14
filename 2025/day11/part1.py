# Sounds a lot like a directed graph.
# The number of paths to the final node is the sum of the number of paths to all the nodes immediately preceding it.
# The numbers of paths to each node immediately preceding it is the same.
# If there were a loop anywhere within the directed graph, the number would be infinite. So we assume this isn't the case.

# We can create a recursive function (top-down dp) to solve the problem I think
# We'll of course also need to memoize but we can simply do that using dictionary entries I think.

adj_list: dict[str, set[str]] = {}

while (cur_line := input()) != "end":
    line_split = cur_line.split()
    key = line_split[0][:-1]
    values = line_split[1:]
    adj_list[key] = set(values)

# For the sake of recursion, we're going to want to reverse the directionality of our graph.

adj_list_rev: dict[str, set[str]] = {}

for key in adj_list.keys():
    values = adj_list[key]
    for value in values:
        if value in adj_list_rev:
            adj_list_rev[value].add(key)
        else:
            adj_list_rev[value] = set([key])

calculated: dict[str, int] = {}

def get_num_paths(key: str, rev_adj: dict[str, set[str]]) -> int:
    if key in calculated:
        return calculated[key]
    if not key in rev_adj:
        calculated[key] = 0
        return 0
    if key == "you":
        calculated[key] = 1
        return 1
    sum = 0
    for prev_key in rev_adj[key]:
        sum += get_num_paths(prev_key, rev_adj)
    calculated[key] = sum
    return sum

num_end_paths = get_num_paths("out", adj_list_rev)
print(num_end_paths)
