#Writing a program to understand the concept of looping (using "While")
count = 1 
while count < 11 :
    print(count,".Assignment")
    count = count + 1


#Using break function
var = 1 
while  var < 6 :
    print(var,".var")
    if var == 4 :
        break
    var += 1


#Using continue function
var = 0
while var < 8 :
    var += 1 
    if var == 2 :
        continue
    print(var,".Here we go again")