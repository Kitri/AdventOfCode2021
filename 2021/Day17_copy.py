# xmin, xmax, ymin, ymax = 14,50,-267, -225
xmin, xmax, ymin, ymax = 20,30,-10,-5

assert ymax < 0

# Find yvel (as described above).
yvel = -ymin - 1

# Find apex elevation. Actually, this is the yvel'th triangular number :)
y = 0
while yvel:
    print('yvel' + str(yvel))
    y += yvel
    yvel -= 1
    print(y)
