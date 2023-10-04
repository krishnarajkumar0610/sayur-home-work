std_names = ["krishna","raj","kumar","vicky","Vignesh"] # students names
std_marks = [80,75,60,49,33]    # students marks
pass_students=[]    # passed students list 
fail_students=[]    # failed students list
if len(std_names) != len(std_marks):    # if any of one length is low, then some data is missing
    print("Some data is missing check the lists of student name and student mark")
    
else:    # no data is missed
    for i in range(len(std_marks)):  # checking the marks of students
        if std_marks[i]>=50:    # if mark is >=50 is pass
            pass_students.append(str(std_names[i])+" : "+str(std_marks[i])) # adding to pass students list by adding their name with marks
        else:   # not passed
            fail_students.append(str(std_names[i])+" : "+str(std_marks[i])) # adding to fail students list by adding their name with marks
print(f"Pass students : {pass_students}")
print(f"Fail students : {fail_students}")