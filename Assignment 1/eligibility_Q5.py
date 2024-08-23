age = int(input("Enter a number:" ))

if(age>=18):
    print(age, "is eligible for voting and driving")
elif(age>=16 and age<18):
    print(age, "is eligible for driving and not voting")
else:
    print("not eligible for voting and driving")