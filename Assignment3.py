#Write a program that defines Conditional Expressions
a =int(input("Enter your obtained marks: "))
b = 65
if a >= b:
  print("Congrats Bud, You've Passed.")
else:
  print("Sorry, Better Luck next time.")


  #Write another program that shows Conditional statement
a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
if a>b:
    print("First value is greater than second one")
elif a<b:
    print("First value is smaller than second one")
else:
    print("Both vlaues are equal")



#Practicing with another example
Kiwi = 1 
Mango = 2 
Grapes = 3
a = int(input("Enter a number from 1 to 3: "))
if a == Kiwi:
   print("I ate Kiwi.")
elif a == Mango:
   print("Mangoes are tasty.")
elif a == Grapes:
   print("Grapes are sour.")
else:
   print("Invalid entry, Please choose a number from 1 to 3 as mentioned.")