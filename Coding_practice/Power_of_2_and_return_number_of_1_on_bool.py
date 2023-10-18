def ispowerof2(n):
    x = n
    y= not(n & (n-1))
    return x and y    
def count_1(n):
    c = 0
    while n:
        c += 1
        n = n & (n - 1)
    return c

res= ispowerof2(12)
res2 = count_1(12)
print(res, res2)

        
