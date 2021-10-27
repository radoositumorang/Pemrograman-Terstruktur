import math


def starFormation1(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("*", end=' ')
        print("\r")


starFormation1(4)


def starFormation2(n):
    for i in range(n + 1, 0, -1):
        for j in range(0, i - 1):
            print("*", end=' ')
        print("\r")


starFormation2(4)


def starFormation2(x):
    n = math.ceil(x / 2)
    for i in range(0, n):
        for j in range(0, i + 1):
            print("*", end=' ')
        print("\r")
    for i in range(n, 0, -1):
        for j in range(0, i - 1):
            print("*", end=' ')
        print("\r")


starFormation2(7)
