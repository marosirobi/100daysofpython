programing_dictionary = {"Bug":"An error in a program that prevents program running",
                         "Function":"A piece of code that you can easily call and run",
                         "Loop": "The action of doing something over and over again"
                         }

#print(programing_dictionary)

empty_dictionary = {}

#for key in programing_dictionary:
    #print(key+ ': '+programing_dictionary[key])

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key in student_scores:
    if student_scores[key] >= 91:
        student_grades[key] = "Outstanding"
    elif 81 <= student_scores[key]:
        student_grades[key] = "Exceeds Expectations"
    elif 71 <= student_scores[key]:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

for key in student_grades:
    print(key+ ": "+student_grades[key])

