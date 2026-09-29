import numpy as np

# Number of students
n = int(input("Enter the number of students: "))

# Student names
names = []

# Marks matrix (n students × 3 subjects)
marks = np.zeros((n, 3))

# Input data
for i in range(n):
    print(f"\nStudent {i+1}")

    name = input("Enter name: ")
    names.append(name)

    for j in range(3):
        marks[i][j] = float(input(f"Enter marks for Subject {j+1}: "))

# Convert names to NumPy array
names = np.array(names)

# Calculate average marks
avg = np.mean(marks, axis=1)

print("\n========== STUDENT REPORT ==========")

for i in range(n):

    # Grade calculation
    if avg[i] >= 90:
        grade = "A+"
    elif avg[i] >= 80:
        grade = "A"
    elif avg[i] >= 70:
        grade = "B"
    elif avg[i] >= 60:
        grade = "C"
    elif avg[i] >= 50:
        grade = "D"
    else:
        grade = "F"

    # Pass/Fail
    if np.all(marks[i] >= 40):
        result = "PASS"
    else:
        result = "FAIL"

    print("\nName:", names[i])
    print("Marks:", marks[i])
    print("Average:", round(avg[i], 2))
    print("Grade:", grade)
    print("Result:", result)

# Topper
topper_index = np.argmax(avg)

print("\n========== TOPPER ==========")
print("Name:", names[topper_index])
print("Average:", round(avg[topper_index], 2))

# Subject averages
subject_avg = np.mean(marks, axis=0)

print("\n========== SUBJECT AVERAGES ==========")
for i in range(3):
    print(f"Subject {i+1}: {round(subject_avg[i], 2)}")

# Ranking
rank = np.argsort(avg)[::-1]

print("\n========== RANK LIST ==========")

for pos, i in enumerate(rank, start=1):
    print(f"Rank {pos}: {names[i]} ({round(avg[i], 2)})")
