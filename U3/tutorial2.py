#question 1
flag = 1
while flag:
    # make sure that the number is integer
    try:
        number = int(input("please enter a number"))
    except:
        continue
    #check whether the number is greater than 0
    if number > 0:
        flag = 0
    else:
        print("please enter again")
        continue
    #check whether the number is the multiple of 2,3,4 collectively
    if (number % 2 + number % 3 + number % 4) == 0:
        print("The number {} is multiple of 2,3,4".format(number))
    else:
        print("The number {} is not a multiple of 2,3,4".format(number))

    print("End of Program")