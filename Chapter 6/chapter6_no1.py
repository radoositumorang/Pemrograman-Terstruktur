import math


def isPythagoras(a, b, c):

    a = math.sqrt(c ** 2 - b ** 2)/a
    b = math.sqrt(c ** 2 - a ** 2)/b
    c = math.sqrt(a ** 2 + b ** 2)/c

    if a == True or b == True or c == True:
        print("True")

    else:
        print("false")


isPythagoras(7, 8, 11)
isPythagoras(5, 9, 12)
isPythagoras(8, 6, 10)
isPythagoras(3, 4, 5)
