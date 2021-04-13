def get_armstrong(n):
   i=n
   y=0
   while(i>0):
       x=i%10
       y=x*x*x + y
       i=i//10

   return n==y 

def main():
    print("----Is Armstrong----")
    print(f"371 ------> {get_armstrong(371)}")
    print(f"1634 ------> {get_armstrong(1634)}")
    print(f"153 ------> {get_armstrong(153)}")

main()