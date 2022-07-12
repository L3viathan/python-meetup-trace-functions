import mypdb


def add(x, y):
    return x + y


mypdb.set_trace()
x = 23
y = 42
z = add(x, y)
print("sum is", z)
