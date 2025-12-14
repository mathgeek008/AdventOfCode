from pulp import LpVariable, LpProblem, lpSum, PULP_CBC_CMD

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

total = 0

for puzzle in puzzles:
    _, buttons, joltage = puzzle

    joltage_vars: list[LpVariable] = []
    for i, t in enumerate(joltage):
        joltage_vars.append(LpVariable("t" + str(i), 0, cat="Integer"))

    button_vars: list[LpVariable] = []
    for i, b in enumerate(buttons):
        button_vars.append(LpVariable("b" + str(i), 0, cat="Integer"))

    prob: LpProblem = LpProblem()

    for i, t in enumerate(joltage_vars):
        prob += t == joltage[i]
        affecting_buttons = []
        for j, b in enumerate(buttons):
            if i in b:
                affecting_buttons.append(button_vars[j])
        prob += t == lpSum(affecting_buttons)

    prob += lpSum(button_vars)
    prob.solve(PULP_CBC_CMD(msg=False))
    total += sum([round(x.value()) for x in button_vars]) # type: ignore

print(total)