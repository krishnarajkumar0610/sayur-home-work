'''We have 3 colleges - each college has a different cut off mark for engineering college admission.
Get the 5 marks from the student. Calculate the average. Find out which colleges the student is eligible to get admission.
For eg, College 1 cut off - 93%, College 2 - 89% and college 3 - 97%. If the student's avg is, 94%, the student is eligible
 for admission in College 1 and College 2.'''
mark1=int(input("Enter the mark 1 :"))
mark2=int(input("Enter the mark 2 :"))
mark3=int(input("Enter the mark 3 :"))
mark4=int(input("Enter the mark 4 :"))
mark5=int(input("Enter the mark 5 :"))
average=int(mark1+mark2+mark3+mark4+mark5)/5
print(f"Average : {average}")
if average>=97 and average<=100:
    print("you can apply to college 3")
elif average>=94 and average<=100:
    print("You are eligible for college 1 and college 2")
elif average>=93 and average<=100:
    print ("you can apply to college 1")
elif average>=89 and average<=100:
    print("you can apply to college 2")
else:
    print("You can't go college")