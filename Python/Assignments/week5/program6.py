def func(list_):
    for i in list_:
        if i < 0:
            break
        else:
            print(i, end=' ')

list_ = list(map(int, input('Enter numbers(space seperated) : ').split()))

func(list_)