import math


def P(n, r):

    f = math.factorial
    permutasi = f(n)//f(n-r)//1
    print("P :", permutasi)


P(10, 7)


def C(n, r):

    f = math.factorial
    kombinasi = f(n)//f(r)//f(n-r)
    print("C :", kombinasi)


C(5, 3)
