# abacaba
# abacabadabacaba
# abacabadabacabaeabacabadabacaba

# look at the output and find the pattern. Hint - add next letter in the alphabet in each row


let = input("Enter the starting letter you need : ")    # asking user to type what character should begins

let = ord(let)  # converting it into number

front_back=total_str=""   # initializing two string varriable

rows = int(input("Enter the number of rows you need : "))   # asking number of rows

for row in range(1,rows+1): # to traverse the rows
    total_str = front_back+chr(let)+front_back  # adding front_back + input letter + front_back
    print(total_str)    # printing the total string after adding the string
    front_back=""   # after printing clearing the string
    front_back=total_str
    if let==122:
        let=96
    let+=1  # incrementing the number +1 so i can print next next characters
    
    
# OUTPUT

# Enter the starting letter you need : a
# Enter the number of rows you need : 5
# a
# aba
# abacaba
# abacabadabacaba
# abacabadabacabaeabacabadabacaba