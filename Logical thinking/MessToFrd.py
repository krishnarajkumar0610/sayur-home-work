def reverse(encoded_word):
    words=""
    for let in encoded_word:
        let=chr(let)
        words+=let
    # print(words)
    let=""
    if words[-1] in ['a','e','i','o','u']:
        let = words[-1]
        let+=words[0:len(words)-1]
        print(let)
    else:
        count = len(words)//2
        print(words[:count][::-1]+words[count:][::-1],end='')
        

word = list(input("Enter the word : ").lower())
encoded_word=[]
for let in word:
    let = ord(let)
    encoded_word.append(let)
print(encoded_word)
reverse(encoded_word)