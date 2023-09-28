def check(word,words):  # this method is to check the list
    if word in words:   # if word in words list
        return True # return True
    return False    # if not, return False

sentence = input("Enter your sentence : ")  # asking input

sentence = sentence.split(" ")  # spliting it into list by spacing

unique_words=[]

for i in range(len(sentence)):  # to traverse the list
    if not check(sentence[i],unique_words):   
        unique_words.append(sentence[i])  # appending word in final list
    else:
        continue
print(f"Unique list : {unique_words}")