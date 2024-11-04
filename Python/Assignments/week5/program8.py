def skip(list_):
    for i in list_:
        if i < 5:
            continue
        print(i, end=' ')

demo_list = [6, 9, 13, 5, 2, 1, 22, 31, 69]

skip(demo_list)