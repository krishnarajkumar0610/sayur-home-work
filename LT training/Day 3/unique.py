# Problem #3
# From the same file as above, read from the file, count the number of unique 4 letter words and it no of occurrences
# for each word. Write this information at the end of file under the heading "Summary of 4 letter words"


def check(words,word):
    if word in words:   # if the word in unique word
        return True # then returning true
    return False    # not having returning false

words=[]    # to store the words from the file
unique_words=[] # to store unique words
unique_words_count={}   # to store unique words and its count


try:    # using exception Handling to check my file is available or not
    with open('F:\Sayur learning\sayur-home-work\LT Training\Day 3\passage_two.txt','r') as file:   # reading my file
        for word_row in file:   
            for word in word_row.strip().lower().split(' '):
                words.append(word)                           
    for index,index_word in enumerate(words): # taking the index and its word     
        if len(index_word) == 4 and not check(unique_words,index_word): # if my word length is 4 and it is not in unique list
            unique_words.append(index_word) # adding it in unique list
            count=0 # setting counter as 0
            for j in range(index,len(words)):   # this loop is to traverse the words list
                if words[j] == index_word:  # if my word is equals to other word
                    count+=1    # counting it
            unique_words_count[index_word]=count    # storing it in the dict with its count from the words
         
    print(unique_words_count)  # printing the unique words with its count
    
except Exception:   # if my file is not available then exception will be thrown
    print("File is not found")
    
    
# output

# {'road': 1, 'path': 1, 'ices': 1}