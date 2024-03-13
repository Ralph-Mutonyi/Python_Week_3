# if elif else statement

# if condition1:
# code block1


#elif condition2:
#   code block 2

#else:
#   code block 3
    

student_grade = input("Enter your grade: ")
student_grade1 = int(student_grade)


if student_grade1 >= 90:
    print("A")
elif student_grade1 >=80:
    print("B")
elif student_grade1 >= 70:
    print("C")
elif student_grade1 >= 60:
    print("D")
else:
    print("F")


