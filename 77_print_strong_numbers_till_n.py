def get_factorial(n):
    fact = 1
    for i in range(n,0,-1):
        fact = fact *i
    return fact

def is_Strong(n):
    i=n
    sum = 0
    while i >0:
        rem =  i % 10
        sum += get_factorial(rem)
        i //=10
    if n == sum:
        return 1
    else:
        return 0 


def main():
    n=int(input("Enter value of n: "))
    for num in range(1,n+1,1):
        if is_Strong(num):
            print(num)



main()