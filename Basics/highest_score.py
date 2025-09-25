students_scores = input("Input a list of students scores\n").split()
for n in range(0, len(students_scores)):
    students_scores[n] = int(students_scores[n])

print(students_scores)

max = 0 
for score in students_scores:
    if(score > max):
        max = score

print(f"The highest score in the class is: {max}")
