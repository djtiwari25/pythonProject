lst = [10,20,30,40,50]

i=0
leng = (len(lst))-1

while i < leng:
    lst[i],lst[leng] = lst[leng],lst[i]
    i+=1
    leng-=1
print(lst)
