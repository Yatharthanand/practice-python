def get_reverse(n):
    i=n
    rev = 0
    

    while i > 0:
        rem = i % 10
        rev = rev * 10 +rem
        i = i //10
    return rev

def main():
    print(f"1234<--> {get_reverse(1234)} ")
    print(f"7453<--> {get_reverse(7453)} ")

main()
