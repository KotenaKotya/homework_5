import random
L = ["самовар", "весна", "лето"]
randword = random.choice(L)
randletter = random.choice(randword)
ranind=randword.index(randletter)
lst=list(randword)
lst[ranind] = "?"
randword2 ="".join(lst)
print(randword2)
user = input("Write the missing letter:")
if randletter == user:
    print("You win!")
else:
    print("You lose :с Try again!")
print(randword)
