import random


def shuffleString(x, n):
    l = []
    i = 0
    while i < n:
        d = ''.join(random.sample(x, len(x)))
        if (d not in l):
            l += [d]
            i += 1
    print(l)


shuffleString('aku', 2)
shuffleString('aku', 3)
shuffleString('aku', 4)
