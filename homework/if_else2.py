# Write a code which gives grade to students according to theirs scores:
# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F

score = int(input('Enter your score : '))
if score <= 100 and score >= 90:
    print('A')
elif score <= 89 and score >= 70:
    print('B')
elif score <= 69 and score >= 60:
    print('C')
elif score <= 59 and score >= 50:
    print('D')
elif score <= 49 and score >= 0:
    print('F')
else:
    print('Invalid Score')