import goto

x = 0
print("x =", x)
if x >= 10:
    goto +3
x += 1
goto -4
print("done")

y = False

def foo():
    global y
    if y:
        print("quitting")
        return
    y = True
    goto -99

foo()
