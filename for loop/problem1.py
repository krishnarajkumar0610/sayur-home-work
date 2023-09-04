# Get and print the 2 marks each for 3 students. 
# Also, get each studen't name
# output should be
# Mark 1 for Student 1 is 55
# Mark 2 for Student 1 is 67
# Mark 1 for Student 2 is 56 
#etc
number_of_students=int(input("Enter number of students :"))
marks_count=int(input("Enter number of subjects :"))
students=[]
marks=[]
for student in range (number_of_students):
    name=input(f"Enter name of student {student+1} :")
    students.append(name)
    for mark in range(marks_count):
        inputMark = float (input(f"Enter mark{mark+1} of Student {name} :")) #use formatted string   
        marks.append(inputMark)                 
    print()  
mark_ind=0
for student_index in range(len(students)):
    num=0
    for mark in range(marks_count):        
        print(f"Mark {num+1} for Student {students[student_index]} is {marks[mark_ind]}")
        num+=1
        
        