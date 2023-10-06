def fun1(num):
    length1= len(str(num))    
    res = 0
    if length1 == 1:
       return False
    else:    
        n = num
        while n >0 :
            digit = n%10
            res = res + digit**2            
            n= n//10
            if res== 1:
                return True
            else :
                return fun1(res)    




print(fun1(1))
