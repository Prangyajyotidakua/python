a = int(input("enter A number"))
 
# if (a % 4 == 0 ) :
#     if(a % 100 == 0):
#          if(a  % 400== 0):
#               print(a,"is a leap year")
#          else:
#              print(a,"is not a leap year")  
#     else:
#          print(a,"is a leap year")    
# else:
#          print(a,"is not a leap year")            

# or 
result = "Leap Year" if a%400 ==0 else "leap year " if a%4==0 and a%100!=0 else"not leap year"
print(result) 