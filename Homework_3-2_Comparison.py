# Create your own algorithm for comparing two strings.

list_1 = list(input('Enter the 1th string: ', ))
list_2 = list(input('Enter the 2th string: ', ))

if len(list_1) == len(list_2):
    check = True
    for i in range(len(list_1)):
        if list_1[i] != list_2[i]:
            check = False
            print('Different element №', i + 1, ':', list_1[i], '-', list_2[i])
    if check:
        print('True: the strings match.')
    else:
        print('False: the strings do not match.')
else:
    print('False: the strings do not match, they have different lengths.')
