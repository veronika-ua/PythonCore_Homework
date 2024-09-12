# Find out if a string can be a palindrome: return True and False. Example: Mr. Owl ate my metal worm

string_palindrome = input('Enter the string: ', )
string_palindrome = string_palindrome.lower()  # converts a string into lower case
string_palindrome = string_palindrome.replace(" ", "", string_palindrome.count(" "))  # delete spaces
string_palindrome = string_palindrome.replace(".", "", string_palindrome.count("."))  # delete dots

true_palindrome = False
if string_palindrome == string_palindrome[::-1]:
    true_palindrome = True
    print('This string is a palindrome - TRUE')

if not true_palindrome:
    count = 0
    list_unique = list(set(string_palindrome))
    for i in range(len(list_unique) - 1):
        if string_palindrome.count(list_unique[i]) % 2 == 1:
            count += 1  # counting odd symbols
    if count > 1:
        print('This string is not a palindrome, and it cannot be - FALSE')
    else:
        print('This string is not a palindrome, but it could be - TRUE')
