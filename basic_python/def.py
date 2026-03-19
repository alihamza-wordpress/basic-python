a = 16
b = 24
c = 31

def greatest(a, b, c):
    if (a>b and a>c):
        return a
    elif (b>a and b>c):
        return b
    elif (c>b and c>a):
        return c

a = 16
b = 24
c = 31
print(greatest(a, b, c))