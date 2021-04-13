
i=1
n=int(input("Enter value of n: "))

for num in range(i,n+1):
    y=0
    z=num
    while(z>0):
       x=z%10
       y=x*x*x + y
       z=z//10
       if num==y:
        print(num) 

