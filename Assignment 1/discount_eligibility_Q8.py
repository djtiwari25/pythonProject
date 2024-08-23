age = int(input("Enter a number:" ))

if(age>=60):
    print(age, "is eligible for senior citizen discount")
elif(age<25 and age > 5):
    print(age, "is eligible for student discount")
else:
    print("not eligible for senior citizen or student discount")