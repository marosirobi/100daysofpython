import random

friends = ["Alice", "Bob", "Charlie","David", "Emanuel"]

randNum = random.randint(0, friends.__len__()-1)

print(friends[randNum])
print(random.choice(friends))

