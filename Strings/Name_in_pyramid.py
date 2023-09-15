########## Program 2
#Print your name in a pyramid
#eg RAM
#R
#RA
#RAM

myName = input("Enter your name :") # asking user name
for i in range(len(myName)):    # stoing index values of myname in 'i'
    
    for j in range(0,i+1):      # j is always st with 0 and ends with i value
        
        print(myName[j],end='') # printing the characters up to ith index value
        
    print() # goes to next line after printing one line


#OUTPUT

# Enter your name :krishna

# s
# sa
# say
# sayu
# sayur
# sayur 
# sayur l
# sayur le
# sayur lea
# sayur lear
# sayur learn
# sayur learni
# sayur learnin
# sayur learning