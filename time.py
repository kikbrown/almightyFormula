def time(day):
    Day=day*24*3600, 'Seconds'
    return Day

def hours(hrs):
    hours=hrs*3600, 'Seconds'
    return hours

def minutes(min):
    minutes=min*60, 'Seconds'
    return minutes



while True:
    print("THIS IS YOUR TIME CONVERTOR, WHAT WOULD YOU LIKE TO CONVERT SECONDS")
    print("PRESS 1 TO CONVERT DAYS TO SECONDS.")
    print("PRESS 2 TO CONVERT HOURS TO SECONDS.")
    print("PRESS 3 TO CONVERT MINUTES TO SECONDS.")
    print("PRESS 4 TO CANCEL")
    option=int(input("WHAT WOULD YOU LIKE TO CONVERT:"))
    if option==1:
        dy=int(input('ENTER VALUES IN DAYS:'))
        print(time(dy))
    elif option==2:
        hrs=int(input('ENTER VALUSE IN HOURS:'))  
        print(hours(hrs))  
    elif option==3:
        min=int(input('ENTER VALUES IN MINUTES:'))  
        print(minutes(min))
    elif option != 1 and option != 2 and option !=3 and option != 4:
        print("TRY AGAIN!!!")
        break
    elif option==4:
         print("Bye and thank you.")
         break      