num = int(input("Enter a number:" ))
flag = False
if num == 0 or num == 1:
    print("not a prime number")
elif num > 1 and num%2!=0:

    for i in range(2, num):
        if(num%i == 0):
            flag = True
            break
    if flag:
        print("not a prime number")
    else:
        print("odd prime number")

else:
    if num> 1 and num%2==0:
        for i in range(2, num):
            if(num%i == 0):
                flag = True
                break
        if flag:
            print("not a prime number")
        else:
            print("even prime number")
