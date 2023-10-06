# def fibo(n):
#     if n <= 1 :
#         return n
#     else :
#         return fibo(n-1)+fibo(n-2)

# n = 10 
# if n<=0:
#     print('please provide a positive number')

# else:
#     print('fibonacci upto {0} is {1}'.format(n,fibo(n))) 
   
    #efficient way to find fibonacci 

def fibo(n, memo={}):
    if n <= 1:
        return n
    elif n not in memo:
        memo[n] = fibo(n-1, memo) + fibo(n-2, memo)
    return memo[n]

n = 10
if n <= 0:
    print('Please provide a positive number')
else:
    for i in range(n):
        print(fibo(i))


