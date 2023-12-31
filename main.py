from functools import reduce

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
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
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


# print(disemvowel("No offense but, Your writing is among the worst I've ever read"))


# Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013).
# Jaden is also known for some of his philosophy that he delivers via Twitter.
# When writing on Twitter, he is known for almost always capitalizing every word.
# For simplicity, you'll have to capitalize each word, check out how contractions are expected to be in the example below.

# Your task is to convert strings to how they would be written by Jaden Smith.
# The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.
def to_jadan_case(string):
    string_list = list(string)
    jaden_string = ''
    prev_char = ' '
    for char in string_list:
        if prev_char == ' ':
            jaden_string += char.upper()
        else:
            jaden_string += char.lower()
        prev_char = char
    return jaden_string


# print(to_jadan_case("How can mirrors be real if our eyes aren't real"))


# There is a bus moving in the city which takes and drops some people at each bus stop.
#
# You are provided with a list (or array) of integer pairs. Elements of each pair represent the number of people that get on the bus (the first item) and the number of people that get off the bus (the second item) at a bus stop.
#
# Your task is to return the number of people who are still on the bus after the last bus stop (after the last array). Even though it is the last bus stop, the bus might not be empty and some people might still be inside the bus, they are probably sleeping there :D
#
# Take a look on the test cases.
#
# Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0. So the returned integer can't be negative.
#
# The second value in the first pair in the array is 0, since the bus is empty in the first bus stop.
def number(bus_stops):
    final_array = []
    for stops in bus_stops:
        holding_num = reduce(lambda x, y: x - y, stops)
        final_array.append(holding_num)
    return sum(final_array)


print(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]))
