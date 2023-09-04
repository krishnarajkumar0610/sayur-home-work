'''Input is a sentence. Find the number of times each word appears.'''
def check_letter(word,letter):
    for i in range(0,len(word)):
        if letter == word[i]:
            return True
    return False
name=input("Enter a word :") 
name=name.lower()
word=""    # this varable for storing the characters
for i in range(0,len(name)):    
    count=0    # this count defaultly changed to zero when i value is incremented
    if not check_letter(word,name[i]):   # sending the word and particular charater
        # when if is true it comes inside
        word=word+name[i]
        for j in range(i,len(name)): 
            # this for loop is for count the letter. it won't count the same character again if it already checked
            if name[i]==name[j]:
                count=count+1
        print(f"{name[i]} has present in the word is {count} times") # print the character and number of times 
    else:
        continue