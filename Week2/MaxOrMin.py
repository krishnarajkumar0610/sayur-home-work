'''
Ask the user to input 3 numbers. Ask the user if they want to find the max of these numbers or minimum.
'''

def maximum(a,b,c):
    if(a==0 and b==0 and c==0) or a==b==c:         # if a,b,c are zero then we can't find max value 
        return "All are equal"          # returned enter valid number
    
    if a>b and a > c:                   # if a is greaterthan b and c
        return  f"Ais max"           # return a is max
    
    elif b>a and b>c:                   # if a is greaterthan b and c
        return f"B is max"            # return b is max
    
    return f"C is max"                # if both conditions are false so i returned c is max

def minimum(a,b,c):
    if(a==0 and b==0 and c==0) or a==b==c:         # if a,b,c are zero then we can't find max value 
        return "All are equal"          # returned enter valid number
    
    elif a < b and a < c:               # if a is lessthan b and c
        return f"A is min"            # return a is min
    
    elif b < a and b < c:               # if b is lessthan a and c
        return f"B is min"            # return b is min

    return f"C is min"                # if both conditions are false so i returned c is min

#asking 3 values for finding max or min of 3 numbers

a=int(input("Enter A value :"))
b=int(input("Enter B value :"))
c=int(input("Enter C value :"))
operation=input("what to find maximum(>) or minimum(<) :")
if operation=='>':
    print(maximum(a,b,c) )
elif operation=='<':
    print(minimum(a,b,c))
else :
    print("invalid operation")