#Multi conditional statements 
#If 
#If else
#If elif else

#Enter day no and show the day
day_no = input("Enter day number.")
if day_no == "1" :
    print("The day is Monday")
elif day_no == "2" :
    print("The day is Tuesday")
elif day_no == "3" :
    print("The day is Wednesday")
elif day_no == "4" :
    print("The day is Thursday")
elif day_no == "5" :
    print("The day is Friday")
elif day_no == "6" :
    print("The day is Saturday")
elif day_no == "7" :
    print("Weekend or Sunday")
else : 
    print("Please enter correct day number between 1-7.")



#Using conditional statements to know temperature 
#If temperature is less than -5 very cold, lower than 5 cold,
#lower than 15 cool, lower than 30 normal, above 30 warm, above 40 very hot.

temperature = int(input("Enter temperature."))
if temperature > 40 : #Above 40 
    print("Temperature is very hot")
elif temperature > 30 : #31 - 40
    print("Temperature is warm")
elif temperature > 15 : #16 - 30
    print("Temperature is normal")
elif temperature > 5 : #6 - 15
    print("Temperature is cool")
elif temperature > -4: #-3 - 5
    print("Temperature is cold")
else:
    print("Temperature is freezing") #Lower than -4
    