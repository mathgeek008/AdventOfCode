dial = 50

rotations = []
while True:
    rotation = input()
    if rotation == 'end':
        break
    else:
        rotations.append(rotation)

password = 0

# Here's the strategy for this part.
# The first part is determining how many full rotations was done. We can just divide distance by 100 for this.
# The second part is figuring out if the remaining rotation put us on or over 0 at some point.
# If we're rotating right and we end up with a number equal or greater than 100, we know for sure we've clicked.
# If we're rotating left and we end up with a number equal or less than 0, we know for sure we've clicked.

# Here's an edge case: if we're rotating left FROM zero, we end up with a number less than 0, but we didn't click.
# This can't happen on the right side because instead of being at 100, we'd be at 0.

for rotation in rotations:
    direction, distance = rotation[0], int(rotation[1:])
    password += distance // 100
    distance %= 100
    if direction == 'L':
        dial -= distance
        # Check to make sure we didn't start at 0
        if dial <= 0 and dial + distance > 0:
            password += 1
    else:
        dial += distance
        if dial >= 100:
            password += 1
    dial %= 100

print(password)
