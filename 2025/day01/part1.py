dial = 50

rotations = []
while True:
    rotation = input()
    if rotation == 'end':
        break
    else:
        rotations.append(rotation)

password = 0

for rotation in rotations:
    direction, distance = rotation[0], int(rotation[1:]) % 100
    if direction == 'L':
        dial -= distance
    else:
        dial += distance
    dial %= 100
    if dial == 0:
        password += 1

print(password)
