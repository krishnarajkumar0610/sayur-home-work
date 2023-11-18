# Problem #2
# you have a list of student names and another list with their marks in CS. 
# hard code the values. no need to get it as input
# Pass mark is 50.
# Print a new list with all the students with pass marks along with their mark in the format name:mark.
# Also print the number of students who failed.

students = ['krishna','raj','kumar','ramu','somu']

cs_marks = [98,87,50,49,25]

pass_count,fail_count=0,0

pass_std,fail_std=[],[]


pass_mark=50

for index,student in enumerate(students):
    if(cs_marks[index]>=pass_mark):
        pass_std.append(f"{student} : {str(cs_marks[index])}")
        pass_count+=1
    else:
        fail_std.append(f"{student} : {str(cs_marks[index])}")
        fail_count+=1
        
print(f"Pass students list : {pass_std} and their total count is = {pass_count}\n")
print(f"fail students list : {fail_std} and their total count is = {fail_count}")