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


def press_button(state: list[int], button: list[int]) -> list[int]:
    after_state = state.copy()
    for b in button:
        after_state[b] = int(not after_state[b])
    return after_state

total = 0

# This is where the solution really starts.
# We should just be able to use a brute force approach with caching.
# A breadth-first-search approach would work here, I think.

total = 0

for goal, buttons, _ in puzzles:
    # We need to use tuple instead of list since it's hashable
    seen_states: set[tuple[int, ...]] = set()
    next_states = deque()
    found = False
    next_states.append((tuple([0] * len(goal)), 0))
    seen_states.add(next_states[0][0])
    while not found:
        cur_state, depth = next_states.popleft()
        for button in buttons:
            after_press = tuple(press_button(list(cur_state), button))
            if after_press == tuple(goal):
                total += depth + 1
                found = True
                break
            if not after_press in seen_states:
                seen_states.add(after_press)
                next_states.append((after_press, depth + 1))

print(total)


