def string_manipulation(string):
    vowel_count = 0

    for i in string:
        if i.lower() in 'aeiou':
            vowel_count += 1

    print(f'Number of vowels in {string} : {vowel_count}')
    print(string[::-1])