import os
from astral_projection import host


x = 23
os.system("hostname")

with host("l3vi.de"):
    os.system("hostname")
    x += 1

print(x)
