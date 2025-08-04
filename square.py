m=int(input("enter M: "))
n=int(input("enter N: "))
even_squares={x**2 for x in range(m,n+1) if x%2==0}
print(even_squares)