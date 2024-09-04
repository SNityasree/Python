a=[10,9,8,7]
print(type(a))
a.append(5)
a.append(6)
b=len(a)
sum=[]
print(a)
for i in range(b):
    if(i==0):
        sum.append(a[b-1])
    sum.append(a[i])
sum.pop(b)
print(sum)
