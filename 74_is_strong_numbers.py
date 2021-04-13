"""
Strong number is a special number whose sum of factorial of digits is equal to the original number.
"""

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
    return n == sum

def main():
    print("Is strong number:")
    print(f"1 --> {is_Strong(1)}")
    print(f"145 --> {is_Strong(1)}")
    print(f"2 --> {is_Strong(1)}")
    print(f"1 --> {is_Strong(1)}")


main()

