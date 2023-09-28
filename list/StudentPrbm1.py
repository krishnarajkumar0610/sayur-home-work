stud_name = ["krishna","raj","kumar","vicky","vignesh"] # students names
stud_marks = [54,56,40,98,86]   # students marks
names_mark=[]   # empty list for passed students
fail_count=0    # to count failed students
if len(stud_name) != len(stud_marks):   # if both length are not same 1 student mark is not entered
    print("One of the student has not entered mark")    

else:   # if equal
    for i in range(len(stud_name)):  # to traverse the list
        if stud_marks[i]>=50:        # if mark is >=50 
            names_mark.append(stud_name[i]+":"+str(stud_marks[i]))  # adding the student name and mark in the String list
        else:   # if mark is < 50
            fail_count+=1   # failed student count is increased by +1
          
print(f"Passed students : {names_mark}")    # printing the passed students

print(f"Failed students : {fail_count}")    # printing the failed students