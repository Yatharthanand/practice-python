def get_perfect(n):
    i=1
    y = 0
    while (i<n):
        if n%i == 0:
            y = y + i
        i = i + 1
      
        if( n == y):
            return n

def main():
    n=int(input("Enter number of values n: "))
    perfect = get_perfect(n)
    print(f"{perfect} is a perfect number")
        

main()
