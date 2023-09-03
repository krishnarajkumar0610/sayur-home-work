############## Problem 3 ##############
#Calculate the Grade for a student, using 3 marks.
'''The student has 100 marks in any one subject, Grade is A.
if the student has 90 or above in any one subject  Grade is B
if the student has 60 or above in any one subject  Grade is C
if the student has 50 or less  in all subjects  Grade is F, otherwise Grade is D.
#Code'''
# getting marks
mark1 = int(input("Enter mark 1 :"))
mark2 = int(input("Enter mark 2 :"))
mark3 = int(input("Enter mark 3 :"))
if mark1<0 or mark2<0 or mark3<0:
    print("Enter valid mark")
elif(mark1  or mark2  or mark3 == 100): #atleast one mark is 100
    print ("your Grade is A")
elif(mark1 or mark2  or mark3 >=90) :     #atleast one mark is 90
    print ("Your Grade is  B")
elif(mark1 or mark2 or mark3>=60):
    print("Your Garde is C")
elif(mark1<=50 and mark2<=50 and mark3<=50):    #all  marks lessthan 50 
    print("Your Grade is D")
else :
    print ("Grade F")   