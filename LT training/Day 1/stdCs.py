# Problem #2
# you have a list of student names and another list with their marks in CS. 
# hard code the values. no need to get it as input
# Pass mark is 50.
# Print a new list with all the students with pass marks along with their mark in the format name:mark.
# Also print the number of students who failed.

students = ['krishna','raj','kumar','ramu','somu']  # students name list

cs_marks = [98,87,50,49,25] # students mark list

pass_count,fail_count=0,0   #assigning 0 to pass and fail count

pass_std,fail_std=[],[] # assigning empty list to pass and fail student list

pass_mark=50    # assigning pass mark 50 to pass mark variable

for index,student in enumerate(students):   # using for loop to traverse in the list and enumerate to get index and value
    if(cs_marks[index]>=pass_mark): # if cs mark of 1 student is >=50 he is pass
        pass_std.append(f"{student} : {str(cs_marks[index])}")  # adding his name in pass student list
        pass_count+=1   # counting him
        
    else:   # else he is fail in cs
        fail_std.append(f"{student} : {str(cs_marks[index])}")      # adding his name in fail student list
        fail_count+=1   # couting him
        
print(f"Pass students list : {pass_std} and their total count is = {pass_count}\n") # displaying the passed students in cs subject
print(f"fail students list : {fail_std} and their total count is = {fail_count}")   # displaying the failed students in cs subject

# output

# Pass students list : ['krishna : 98', 'raj : 87', 'kumar : 50'] and their total count is = 3

# fail students list : ['ramu : 49', 'somu : 25'] and their total count is = 2