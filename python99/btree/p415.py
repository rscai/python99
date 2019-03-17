from math import ceil


def layout_binary_tree(t):
    tree, _ = markX(countour(t), 0)
    return markY(tree, 1)


def markX(t, p):
    if t is None:
        return None, p
    if t[1] is None and p == 0:
        # found the mostleft node
        e = (t[0][0], 1)
        p = 1
        left = None
    else:
        left, p = markX(t[1], p)
    firstLeftShift = 0
    firstRightShift = 0
    if len(t[0][1]) > 0:
        firstLeftShift = t[0][1][0][0]
        firstRightShift = t[0][1][0][1]
    selfX = p-firstLeftShift
    e = (t[0][0], selfX)
    if t[2] is not None:
        rightX = selfX+firstRightShift
        right, p = markX(t[2], rightX)
    else:
        right = None
    return [e, left, right], selfX


def markY(t, h):
    if t is None:
        return None
    return [(t[0][0], t[0][1], h), markY(t[1], h+1), markY(t[2], h+1)]


def countour(t):
    if t[1] is None and t[2] is None:
        return [(t[0], []), None, None]
    if t[1] is None:
        left = None
        leftCountours = []
    else:
        left = countour(t[1])
        leftCountours = left[0][1]
    if t[2] is None:
        right = None
        rightCountours = []
    else:
        right = countour(t[2])
        rightCountours = right[0][1]
    distance = maxDistance(leftCountours, rightCountours)
    print(t[0], distance)
    leftShift = 0-ceil(distance/2)
    if left is None:
        leftShift = 0
    rightShift = ceil(distance/2)
    if right is None:
        rightShift = 0
    selfCountours = [(leftShift, rightShift)]+remainCountours(leftShift,
                                                              rightShift, leftCountours, rightCountours)
    return [(t[0], selfCountours), left, right]


def maxDistance(leftCountours, rightCountours):
    maxDist = 1
    for i in range(0, max(len(leftCountours), len(rightCountours))):
        left = 0
        right = 0
        if i < len(leftCountours):
            left = leftCountours[i][1]
        if i < len(rightCountours):
            right = rightCountours[i][0]
        distance = left + 1-right
        if distance > maxDist:
            maxDist = distance
    return maxDist


def remainCountours(leftShift, rightShift, leftCountours, rightCountours):
    countours = []
    for i in range(0, max(len(leftCountours), len(rightCountours))):
        left = 0
        right = 0
        if i < len(leftCountours):
            left = leftCountours[i][0]
        if i < len(rightCountours):
            right = rightCountours[i][1]
        countours.append((left+leftShift, right+rightShift))
    return countours
