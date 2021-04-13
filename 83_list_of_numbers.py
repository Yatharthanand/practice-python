import sys
numbers = [2,24,43,42,445]

sum = 0
product = 1
max = -1
min = -1
max = -sys.maxsize
min = -sys.maxsize

for item in numbers:
    sum = item + sum
    product*= item
    if item >max:
        max = item
    if item < max:
        min = item

print(f"Sum of {numbers} = {sum}")


avg = sum/len(numbers)
print(f"Average = {avg}")
print(f"max = {max}")
print(f"min = {min}")