def max4(n1, n2, n3, n4):
    if n1 > (n2 or n3 or n4):
        return n1
    if n2 > (n1 or n3 or n4):
        return n2
    if n3 > (n1 or n2 or n4):
        return n3
    return n4


print(max4(5, 6, 12, 7))
print(max4(-10, -12, -4, -9))
print(max4(2.5, 2.6, 2.6, 2.4))
print(max4(-2.5, 0, -1.2, -0.4))
print(max4(-2, -2, -2, -2))
