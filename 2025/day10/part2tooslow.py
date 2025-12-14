from collections import deque

puzzles: list[tuple[list[int], list[list[int]], list[int]]] = []

while (cur_line := input()) != "end":
    cur_tokens = cur_line.split()
    cur_goal_str = cur_tokens[0]
    cur_buttons_str = cur_tokens[1:-1]
    cur_joltage_str = cur_tokens[-1]

    # Parse the goal
    cur_goal: list[int] = []
    for c in cur_goal_str[1:-1]:
        cur_goal.append(int(c == '#'))
    
    # Parse the buttons
    cur_buttons: list[list[int]] = []
    for b in cur_buttons_str:
        cur_button: list[int] = []
        for i in b[1:-1].split(','):
            cur_button.append(int(i))
        cur_buttons.append(cur_button)
    
    # Parse the joltage
    cur_joltage: list[int] = []
    for j in cur_joltage_str[1:-1].split(','):
        cur_joltage.append(int(j))
    
    puzzles.append((cur_goal, cur_buttons, cur_joltage))


def press_button(state: list[int], button: list[int], neg: bool = False) -> list[int]:
    after_state = state.copy()
    for b in button:
        if not neg:
            after_state[b] += 1
        else:
            after_state[b] -= 1
    return after_state

total = 0

# Unlike part 1 of this problem, I think this may be a dynamic programming problem? Rather than a BFS
# I'm still not 100% sure. It might also involve working backwards
# As soon as I can wrap my head around a solution I'll think about how to implement it.

# Alright, I think I have one.
# We do, pretty much, the exact same thing as before. EXCEPT, our "solution space" is a dictionary!
# Once we know that the optimal way to get 0 0 0 1 is one press, why not add 3 5 4 6 to the solution space?
# I believe it should pretty much cut down the depth we need to search by HALF, which in this exponential growth
# problem may be critical.
# I also have a theory about sums of results, but I'm not sure of a good way to implement that for now, so I hope
# this other approach is sufficient.

# We need to store the seen states as a dictionary
# We need to store the solution space as a dictionary
# Every time we update the solution space, we need to check if it exists in the seen space
# This, kinda, pretty much handles the sums of results case? Almost? Not 100% sure on that

# It does not! And we are, in fact, not efficient enough here.
# I do think we need to try doing sums within our space. We know that any sum is a valid solution, however we do not
# know for sure that it is optimal...
# Actually. We MIGHT know for sure that it's optimal if we start with the depth 1 and work our way up. I'm not 100% sure of this

total = 0

for _, buttons, joltage in puzzles:
    # pattern, depth
    seen: dict[tuple[int, ...], int] = {}
    # pattern, depth (how much to add to get to end goal)
    solution_space: dict[tuple[int, ...], int] = {}
    next: deque[tuple[tuple[int, ...], int]] = deque()
    found = False
    next.append((tuple([0] * len(joltage)), 0))
    seen[next[0][0]] = 0
    solution_space[tuple(joltage)] = 0
    while not found:
        cur_state, depth = next.popleft()
        print(cur_state, depth)
        for button in buttons:
            after_press = tuple(press_button(list(cur_state), button))
            if after_press in solution_space:
                total += solution_space[after_press] + depth + 1
                found = True
                break
            if not after_press in seen:
                seen[after_press] = depth + 1
                new_solution = tuple(press_button(list(joltage), button, True))
                if not new_solution in solution_space:
                    solution_space[new_solution] = depth + 1
                next.append((after_press, depth + 1))

print(total)


