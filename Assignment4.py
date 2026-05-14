#Write a program that checks if a number is positive/negative or Zero

num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive")
elif num == 0:
    print("The number is Zero")
else: 
    print("The number is negative") 


# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number

num = int(input("Enter a number: "))
if (num % 2) == 0:
    print("{0} is Even".format(num))
else:
    print("{0} is Odd".format(num))

    #Write a program to generate random number
    #Importing the random module
    import random
    print(random.randint(0,99999))