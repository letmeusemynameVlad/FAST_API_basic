def add_2(*args):
    for i in args:
        print(i + 2)

    print("-"*100)


def add_3(a=0, b=0, c=0):
    print(a + 1)
    print(b + 2)
    print(c + 3)


def add_4(n, p, **kwargs):
    print(n + 4)
    print(p + 4)
    for i, j in kwargs.items():
        print(i, j + 4)


add_2(1, 2, 3)  #  positional arguments
add_2(45, 234)
add_2(3)
add_2()


add_3(1, 2, 3)  # positional arguments
add_3(a=2, c=10, b=4)  # naming arguments
add_3(c=10)  # naming arguments


add_4(10, 2, s=10, k=13)
add_4(1, 2, arg1=3, arg2=4, arg3=5)

print("="*100)
d = {"b": 10, "a": 11, "c": 50}
add_3(**d)  # a=11, b=10, c=12
print("="*100)
add_3(a=10, b=11, c=12)
print("="*100)
t = (15, 13, 12)
add_3(*t)  # 10, 11, 12
