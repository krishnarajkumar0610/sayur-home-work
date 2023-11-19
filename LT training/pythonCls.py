# problem 5
# In your college Python is taught in 3 different departments by the same professor. 
# For each dept, get the no of students stutying Python and their marks in the final exam 
# Get the input as comma seperated string

# Find the top 3 marks in each class
# Find the top 3 marks if all classes are combined.
# Find the avg mark of students with passing mark in each class and the classes combined.
# Find which class has the best average mark and least number of failed students.
def findTopthree(mark_details):  # This method is to find top 3 marks in each class
    mark_details=[int(x) for x in mark_details]
    mark_details=sorted(mark_details,reverse=True) # sorting the list in reverse order
    topMarks=mark_details[0:3]    # storing the top marks what limit we need
    return f"Top 3 marks in each class is {topMarks}"  # returning the top marks

def findCombinedMark(mark_details):
    marks=[]
    for mark in mark_details:
        if mark.isdigit():
            marks.append(int(mark)) 
    marks=sorted(marks,reverse=True)
    topMarks=marks[0:3]
    return f"Top 3 combained class marks is {topMarks}"

def fingAvgEc(mark_details,b=True):
    sum=0
    count=0
    mark_details=[int(x) for x in mark_details]  
    for mark in mark_details:
        if mark>=50:
            sum+=mark
        else:
            count+=1
    if(not b):
        return count
    return f"average mark is {sum//len(mark_details)}"

def fingAvgCom(mark_details):
    sum=0
    marks=[]
    for mark in mark_details:
        if mark.isdigit():
            marks.append(int(mark))
    for mark in marks:
        if mark>=50:
            sum+=mark
    return f"Average mark in combained class test is {sum}"        
            

    
def bestAvg_leastFail(ec_avg,fails=0,b=True):
    if(not b):
        for values in fails.values():
            element = values[0]
            for value in range(1,len(values)):
                if element>value:
                    element=value
        return element
    for values in ec_avg.values():
        element = values[0]
        for value in range(1,len(values)):
            if element<value:
                element=value
    return element


        
mark_details = input("Enter the dep and marks and seperate it by comma (,) : ")
topMarks_eachCls={}  # creating empty dict to store top 3 marks in each class
mark_details = mark_details.split(',')  # split each word by comma
number_of_subjects=5
limit = 6
for index in range(0,len(mark_details),6):   
    # storing top 1 mark from each class
    topMarks_eachCls[mark_details[index]]=findTopthree(mark_details[index+1:limit])       
    limit = limit+6    
#sending the combined class
topThree_comClass = findCombinedMark(mark_details)   # storing top 3 marks from combined class

ec_avg = {}
fails={}
limit=6

for index in range(0,len(mark_details),6):   
    ec_avg[mark_details[index]]=fingAvgEc(mark_details[index+1:limit])   
    fails[mark_details[index]]=fingAvgEc(mark_details[index+1:limit],False)
    limit = limit+6    

print(f"Top 3 marks in each class =  {topMarks_eachCls}\n")

print(f"Top 3 marks in combained class = {topThree_comClass}\n")

print(f"The average marks in each class = {ec_avg}\n")

print(f"Fail counts in each class = {fails}\n")