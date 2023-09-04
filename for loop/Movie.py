############## Problem 2 ################
#Use For loop, break and continue as needed.
# You need Rs 1000 to go to movie. you are asking your parents for money. your parents give you a
# some money. Ask your parents for money until you get Rs1000 or a maximum of 5 times.
# Each time they give you some money, you need to print how much money you got so far and print "Thank you.".
# Print "Thank you " only if the money is > Rs 10. If money is less than or = Rs 10, don't add it
# towards the Rs1000 that you need. Use Continue stmt as needed.
# Print how many times you had to ask your parents to get this money.
target_amount=int(input("Enter the target amount you are asking your parents for money :"))
number_of_times=int(input("Enter the number of times we can ask our money to our parents :"))
total_amount=0
count_times=0
for limit in range(number_of_times):
    amount=int(input("Give money to your child :"))      
    if amount<=target_amount:
        if amount>10:
            print("Thank you")
            total_amount+=amount
            print(f"Current amount : {total_amount}")
            count_times+=1
        elif amount<=10:
            print("Insufficient amount please give me more money !")
            continue
        
    elif amount>=target_amount:
        total_amount=amount    
        print(f"Thank you. You got extra amount from your parents {amount}")
        count_times+=1
        break
    
    if total_amount==target_amount:
        break
    
if total_amount<target_amount:
    print(f" You having only Rs.{total_amount} amount. You can't able to go movie")
else:
    print(f"After asking amount to parents and total amount is Rs.{total_amount}. You can watch movie")
print(f"Number of times you asked money to your parents is {count_times}")