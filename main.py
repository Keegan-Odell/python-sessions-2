# In this kata you should simply determine, whether a given year is a leap year or not.
# In case you don't know the rules, here they are:
# years divisible by 4 are leap years
# but years divisible by 100 are not leap years
# but years divisible by 400 are leap years
# Additional Notes:
# Only valid years (positive integers) will be tested, so you don't have to validate them
# Examples can be found in the test fixture.
# www.codewars.com/kata/526c7363236867513f0005ca/train/python
def is_leap_year(year):
    if year%400 == 0:
        return True
    elif year%100 == 0:
        return False
    elif year%4 == 0:
        return True
    else:
        return False


# testNum = int(input('What Year? '))
# print(is_leap_year(testNum))

# Trolls are attacking your comment section!
#
# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
#
# Your task is to write a function that takes a string and return a new string with all vowels removed.
#
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
#
# Note: for this kata y isn't considered a vowel.
def disemvowel(string_):
    vowels = 'aeiouAEIOU'
    finished_string = ''
    for char in string_:
        if char not in vowels:
            finished_string += char
    return finished_string


print(disemvowel("No offense but, Your writing is among the worst I've ever read"))





