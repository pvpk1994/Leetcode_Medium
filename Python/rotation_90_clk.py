# Rotate an NxN matrix by 90 degrees clockwise
# Constraint: Should be rotated in O(1) space complexity
# Author: Pavan Kumar Paluri
def rotateImage(a):
    for i in range(len(a)//2):
        for j in range(i, len(a)-1-i):
            prev = a[i][j]
            a[i][j] = a[len(a)-1-j][i]
            # a[len(a)-1-j][i] = prev
            a[len(a)-1-j][i] = a[len(a)-1-i][len(a)-1-j]
            a[len(a)-1-i][len(a)-1-j] = a[j][len(a)-1-i]
            a[j][len(a)-1-i] = prev
    return a
