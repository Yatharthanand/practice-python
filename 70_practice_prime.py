def is_prime(n):
    start = 2
    stop = n-1

    i= start
    while(i<= stop):
        if (n%i==0):
            return False
        i=i+1
        return True
def is_prime_status(n):
    if is_prime(n):
        print(f"{n} is a prime")
    else:
        print(f"{n} not a prime")
def main():
    n=int(input("Enter value of n: "))
    
    is_prime_status(n)

main()

