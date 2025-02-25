fruits = ['apple', 'banana', 'orange']

for fruit in fruits:
    print(fruit)

student_scores = [150,142,185,171,183,320,21,64,75,34,100]

total_score = sum(student_scores)
print(total_score)

sum = 0
for score in student_scores:
    sum += score

print(sum)
print(max(student_scores))

max = student_scores[0]
for score in student_scores:
    if max < score:
        max = score

print(max)

for i in range(0,11,2):
    print(i)

sum_of_100 =  0
for i in range(1,101):
    sum_of_100 += i

print(sum_of_100)