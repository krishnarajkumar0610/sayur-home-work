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
    return topMarks # returning the top marks

def findCombinedMark(mark_details): # this method is to find the top 3 marks in combined class
    marks=[]    # creating a empty list
    for mark in mark_details:   # this for loops is to traverse the mark detail list
        if mark.isdigit():  # checking each element is digit or not from the list
            marks.append(int(mark))     # if it id digit then adding the element in the marks list as integer
    marks=sorted(marks,reverse=True)    # sorting the marks in decending order
    topMarks=marks[0:3] # slicing the 1st 3 as top 3 marks in combined class
    return topMarks # returning the top 3 marks from the combined class

def fingAvgEc(mark_details,b=True): # this method is to find the avg mark from each class
    sum=0   # assigning sum = 0 to add  the marks
    count=0 # count is to count the failed student when we need count of the failed students it will work
    mark_details=[int(x) for x in mark_details]  #changing all marks as integer and stored in same list
    for mark in mark_details:   # this loop is to traverse the mark details list
        if mark>=50:    # if any element from the list is >=50 then it is pass  mark
            sum+=mark   # then adding the marks to get the total pass mark 
        else:   # if any one of the mark is fail then counting it
            count+=1
    if(not b):  # if i pass False in the parameters then not operator change it as True 
        return count   # then return the failed count when i need the failed count it won't return the average mark from each class
    return sum//len(mark_details)

def fingAvgCom(mark_details):       #  this method is to find the avg mark from the combined class
    sum=0   # assigning sum = 0 to add  the marks
    marks=[]    #creating the empty list to store marks
    for mark in mark_details:   # this loop is to traverse the mark details list
        if mark.isdigit():  # checking each element is digit or not 
            marks.append(int(mark)) # if it is digit then adding it in the list
    for mark in marks:  # this for is to traverse the marks list
        if mark>=50:    # if any mark is >=50 then it is pass
            sum+=mark   # then adding it to get total marks
    return sum//len(mark_details)  # returning the average mark from the combined class   
            

    
def bestAvg_leastFail(average,fails):    
    max=average[0]
    min=fails[0]
    for index in range(1,len(average)):
        if max<average[index]:
            max=index
    for index in range(1,len(fails)):
        if min>fails[index]:
            min=fails[index]
            
    return f"The best average mark is {max} and least fail is {min}"

        
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
failed={}
avg=[]
fail=[]
limit=6

for index in range(0,len(mark_details),6):   
    val=fingAvgEc(mark_details[index+1:limit])
    avg.append(val)
    ec_avg[mark_details[index]]=val
    val=fingAvgEc(mark_details[index+1:limit],False)
    fail.append(val)
    failed[mark_details[index]]=val
    limit = limit+6  
    
avg_combined=fingAvgCom(mark_details)
    
best_avg_fails=bestAvg_leastFail(avg,fail) 
    
      

print(f"\nTop 3 marks in each class =  {topMarks_eachCls}\n")

print(f"Top 3 marks in combained class = {topThree_comClass}\n")

print(f"The average marks in each class = {ec_avg}\n")

print(f"The average mark in combined class = {avg_combined}\n")

print(f"Fail counts in each class = {failed}\n")

print(best_avg_fails)