# String sorting.

str_new = sorted(input('Enter the string: ', ))

str_int = [0] * len(str_new)
str_lower = [0] * len(str_new)
str_title = [0] * len(str_new)
str_else = [0] * len(str_new)

i_int = 0
i_lower = 0
i_title = 0
i_else = 0

for i in range(len(str_new)):
    if str_new[i].isnumeric():
        str_int[i_int] = str_new[i]
        i_int += 1
    elif str_new[i].islower():
        str_lower[i_lower] = str_new[i]
        i_lower += 1
    elif str_new[i].istitle():
        str_title[i_title] = str_new[i]
        i_title += 1
    else:
        str_else[i_else] = str_new[i]
        i_else += 1

print(str_int[:i_int] + str_lower[:i_lower] + str_title[:i_title] + str_else[:i_else])
