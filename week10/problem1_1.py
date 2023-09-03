######### Problem 1.1
#same problem as above, but output should have the student name and 
# all the marks in the same line.
# Eg - Input - Student Name - Chitra, Mark1 1 55, Mark 2 67
#output -  Chitra's marks 55, 67

number_of_students=int(input("Enter number of students :"))
marks_count=int(input("Enter number of marks :"))
for student in range (number_of_students):
    name=input(f"Enter name of student {student+1} :")
    mark_1,mark_2=0,0
    marks=[]
    for mark in range(marks_count):
        inputMark = float (input(f"Enter mark{mark+1} of Student {name} :")) #use formatted string 
        marks.append(inputMark)
    marks_str = ', '.join(str(mark) for mark in(marks)) # join is used for join into a String not in list
    print(f"{name}'s marks {marks_str}")
    print()  