# Problem #2
# Read a passage from a file. 
# Count the number of times the word 'the' followed by another 'the' without 'a' in between.

# Eg The king went to the forest with the wife and a servernt. 
# The king shot a deer.
# The king went to the forest again the next day.

# answer is 4 (The king, the forest, The King the next).


def check(first_lasts,middle_letter):
    if middle_letter in first_lasts:
        return True
    
    return False


first_last="the"    # storeing 'the' in first first_last variablee
middle_letter="a"   # storing 'a' in middle first_last 
check_sentence=[]   # declaring the emply list 
count=0     # declaring the count varibale
words=[]
i=0 # initializing a 
try:
    with open('F:\Sayur learning\sayur-home-work\LT Training\Day 3\passage_one.txt','r') as file:
        for word_rows in file:
            word_rows=word_rows.strip().lower().split(' ')
            for word in word_rows:
                words.append(word) 
            
    for word in range(i,len(words)):   # to traverse the list
        if words[word] == first_last:
            check_sentence.append(words[word])
            for j in range(word+1,len(words)):
                check_sentence.append(words[j])
                if words[j] == first_last:
                    if not check(check_sentence,middle_letter):
                        count = count + 1
                        check_sentence.clear()  # []
                    else: 
                        check_sentence.clear()
                    break
                
                
    print(f"Count :{count}")
    
    
except FileNotFoundError:
    print("File is not fount")
             

# output 

# Count :4