def string_reverse(strin):

    rstr = ' '
    index = len(strin)
    while index > 0:
        rstr += strin[ index - 1 ]
        index = index - 1
    return rstr
print(string_reverse('1234abcd'))
