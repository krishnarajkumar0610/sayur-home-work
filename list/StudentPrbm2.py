




stud_name = ["krishna","raj","kumar","vicky","vignesh"] # students names
cs_mark = [90,34,56,78,23]   # students cs mark
math_mark = [90,54,36,50,73] # students cs mark
eng_mark = [56,100,76,68,83]
names_grade=[]   # empty list for passed students
fail_count=0    # to count failed students
grade_A,grade_B=0,0
index=0
for i in range(len(stud_name)):  # to traverse the list
    if cs_mark[index]>=90:
         grade_A+=1
    if math_mark[index]>=80:
        grade_B+=1
    if eng_mark[index]==50:
        names_grade.append(stud_name[index]+" ")