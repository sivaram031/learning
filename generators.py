# using while loop

def gen(n):
    number = 0
    while number < n:
        yield number
        number += 1

seq = gen(5)

print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))


# using for loop

def get_seq(x):
    for i in range(x):
        yield i
ord = get_seq(5)
print(next(ord))
print(next(ord))
next(ord)