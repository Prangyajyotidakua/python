start_com = "Car started ... Ready too go "
stop_com = "Car stopped ."
Other = "I don't understand that "
started = False
stopped = False
command =""
while command != "quit" :
    command = input("enter command").lower()
    if command == "start" :
        if started :
            print("car is already started")
        else :
            started = True    
            print(start_com)
    elif command == "stop" :
        if not started :
            print("car is already stopped")
        else :  
            stopped = True 
            started = False
            print(stop_com)
    elif command == "quit" :
        break
    elif command == "help" :
        print(
            """
               start - to start the car
               stop - to stop the car
               quit  - to quit """
        )   
    else :
        print(Other)       