words = ['apple', 'banana', 'cherry', 'date', 'elderberry']
skip_words = ['banana', 'date']

for word in words:
    if word in skip_words:
        continue
    print(word, end=' ')