def fact(num):
    f = 1
    for p in (num, 0, -1):
        f *= p
        print(p)

    return f



print(fact(5))
