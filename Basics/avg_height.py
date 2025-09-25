students_heights = [180, 124, 165, 173, 189, 169, 146]
total = 0

for height in students_heights:
    total += height

avg = total / len(students_heights)
print(f"Avg of height is: {avg}")