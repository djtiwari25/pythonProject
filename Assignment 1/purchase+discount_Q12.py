purchase = int(input("Enter a number:" ))

if(purchase>=150):
    print(purchase, "is eligible for discount & free shipping")
elif(purchase>=100 and purchase<150):
    print(purchase, "is eligible for free shipping")
else:
    print("not eligible for free shipping and discount")