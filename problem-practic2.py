# Harry Potter has got the “n” number of apples. Harry has some students among whom he
# wants to distribute the apples. These “n” number of apples is provided to harry by his friends,
# and he can request for few more or few less apples.
#
# You need to print whether a number is in range mn to mx, is a divisor of “n” or not.


while(True):
    apples = input("Enter the number of apple you have\n")
    if apples.isnumeric():
        apples1=int(apples)
    else:
        print("Invalid input try again!")
        continue

    mn = input("Enter the min no of student\n")
    if mn.isnumeric():
        min=int(mn)

    else:
        print("Invalid input try again!")
        continue

    mx = input("Enter the max no of student\n")
    if mx.isnumeric():
        max=int(mx)

    else:
        print("Invalid input try again!")
        continue


    for i in range(min, max+1):
        if apples1 % i == 0:
            print(f"{i} is divisor of {apples1}")
        else:
            print(f"{i} is not divisor of {apples1}")
    break
