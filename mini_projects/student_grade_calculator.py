def calculate_grade(average):
    if average >= 80:
        return "A+"
    elif average >= 70:
        return "A"
    elif average >= 60:
        return "A-"
    elif average >= 50:
        return "B"
    elif average >= 40:
        return "C"
    else:
        return "Fail"


print("=== Student Grade Calculator ===")

# Input

student_name = input("Enter student name: ")

math = float(input("Enter Math marks: "))
english = float(input("Enter English marks: "))
science = float(input("Enter Science marks: "))

# Calculation 

total = math + english + science
average = total / 3

grade = calculate_grade(average)

# Output

print("\n===== Result =====")
print("Student:", student_name)
print("Total Marks:", total)
print("Average:", round(average, 2))
print("Grade:", grade)
# Grade will show based on avarage

# Loop Example

print("\nSubjects Processed:")

subjects = ["Math", "English", "Science"]

for subject in subjects:
    print("-", subject)
