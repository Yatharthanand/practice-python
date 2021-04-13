"""

Declare list of names,
Declare a list of wishes,

wish every person with all eishes

eg:
names: yatharth,ankush and aaditya
wishes:good morning, good evening and good night

output
good morning yatharth
goodnight ankush

"""

names = ["Messi", "Yatharth", "Virat", "Jas"]
wishes= ["Good morning","Good morning","Good night","Good afternoon"]
for name in names:
    print(name)
for wish in wishes:
    print(wish)

print("----------")
for i in range(4):
    print(f"{i}. {wishes[i]}.{names[i]}")