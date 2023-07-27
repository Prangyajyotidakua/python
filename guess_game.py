secret_number = 9 
guess_count = 0

while guess_count < 3 :
    guess_count +=1 
    val = int(input("enter the secret number")) 
    if val == secret_number :
        print(f"yes you guess {val} it correct")
        break
    else:
        print(f"No your guess is not correct {3 - guess_count}  guess left")    
print ("end of code")
