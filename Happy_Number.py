class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def fun1(num):
            res = 0
            n = num  
            while n>0:
                print(res)
                digit = n % 10
                res = res + digit ** 2
                print(res)
                n = n // 10
                print(res)         
            if res == 1:
                return True
            elif res == num or res == 4 :
                return False
            else:
              
                return fun1(res)    
            

        return fun1(n)


# For input n = 3
result = Solution().isHappy(3)
print(result)
