import sys

x = 23

def increment(variable):
    frame = sys._getframe()
    frame = frame.f_back
    frame.f_locals[variable] += 1

increment("x")

print(x)
