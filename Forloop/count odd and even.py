a=int(input())
b=int(input())
evencount=0
oddcount=0
for i in range(a+1,b):
    if(i%2==0):
       evencount= evencount+1
    else:
       oddcount=oddcount+1
print(evencount,oddcount)
