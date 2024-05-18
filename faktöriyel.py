def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n-1)

print("5 faktöriyel:", faktoriyel(5))
