n=int(input("enter no of elements"))
a=[]
b=[]
print("enter element")
for i in range(n):
    temp=int(input())
    a.append(temp)
print("list :,a")
for i in range(n):
        if(a[i]%2==0):
            b.append(a[i])
print("even list :",b)
            

