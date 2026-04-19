print("=== Student Grade Calculator ===")

name = input("Enter student name: ")

sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))
sub4 = float(input("Enter marks for Subject 4: "))
sub5 = float(input("Enter marks for Subject 5: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
average = total / 5

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

if average >= 50:
    status = "PASS"
else:
    status = "FAIL"

print(f"\nStudent Name: {name}")
print(f"Total Marks: {total} / 500")
print(f"Average: {average}")
print(f"Grade: {grade}")
print(f"Result: {status}")
