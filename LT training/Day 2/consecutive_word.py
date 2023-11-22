def count_consecutive_words(text):
    words = text.split()
    consecutive_word_count = {}
    prev_word = ''

    for word in words:
        if word == prev_word:
            if word in consecutive_word_count:
                consecutive_word_count[word] += 1
            else:
                consecutive_word_count[word] = 1
        prev_word = word

    return consecutive_word_count

passage = input("Enter Your Passage: ")
result = count_consecutive_words(passage)
for word, count in result.items():
    print(f"{word} {word} : {count} times")