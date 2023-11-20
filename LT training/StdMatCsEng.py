# Problem #3
# you have a list of student names. you have one list each for their marks in CS, Math and English. 
# hard code the values. no need to get it as input
# Pass mark is 50.
# Grade A is, mark 90 or above
# Grade B , 80 or above
# Fail is < 50
# Print the name of the students who got A in all subjects or atleast one A and the rest B.
# Try to use only one if statement.

students = ["john", "smith", "david",]  # students list

marks=[
    [95, 90, 95],   # john marks
    [90, 85, 82],   # smith marks
    [95, 49, 82]    # david marks
]

marks_dict = {} # creating the empty dict

for index in range(len(students)):  # this for loop is to assigning key and value to mark dict
    marks_dict[students[index]] = marks[index]


for name, marks in marks_dict.items():  # this for loop is for getting keys and values from the dict
    grade_A_list = [mark >= 90 for mark in marks]   # collecting numbers of true which is >=90
    grade_B_list = [mark >= 80 and mark < 90 for mark in marks]  # collecting numbers of true which is >=80
    a_count = grade_A_list.count(True)  # count number of True in A grade
    b_count = grade_B_list.count(True)  # count number of True in B grade
    
    if (a_count >= 3) or (a_count >= 1 and b_count == len(grade_B_list) - a_count): 
        # if my 'A' grade count is 3 or 1 'A' and and 2 'B' grade i can assign them as passed students 
        print(f"{name} is passed")
        
    else:   
        # if any one is fail in any one subject they considered as fail students
        print(f"{name} is failed")  
        
        
# output

# john is passed
# smith is passed
# david is failed