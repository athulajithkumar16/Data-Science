def non_repeating(string):
    for i in string:
        if string.count(i) == 1:
            print(string.index(i))
            break

non_repeating('leetcode')
non_repeating('loveleetcode')