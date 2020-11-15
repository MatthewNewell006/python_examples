# LIST STRING METHODS

def get_all_letters(string):
    return list(string)

print(get_all_letters('Radagast'))

print('\n')
#======================================================================================================================

def get_all_words(string):
    return string.split()

print(get_all_words('Radagast the Brown'))

print('\n')
#======================================================================================================================

# ADVANCED 1

from collections import Counter, defaultdict

def count_words(string):
    d = {}
    count = 1
    for i in sorted(string.split()):
        if i not in d:
            d[i] = count
        else:
            d[i] = count + 1
    return d

string = 'ask a bunch, get a bunch'
print(count_words(string))

print('\n')
#======================================================================================================================

def count_words(string):
    d = Counter(sorted(string.split()))
    return d

string = 'ask a bunch, get a bunch'
print(count_words(string))

print('\n')
#======================================================================================================================

def count_words(string):
    if not string:
        return {}

    word_dict = {}
    words = string.split(" ")
    for word in words:
        if word_dict.get(word):
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    return word_dict

string = 'ask a bunch, get a bunch'
print(count_words(string))

print('\n')
#======================================================================================================================

def invert_dictionary(d):
    '''
    Given a dictionary d, return a new dictionary with d's values
    as keys and the value for a given key being
    the set of d's keys which shared the same value.

    Parameters
    ----------
    d: dict

    Returns
    -------
    dict
        A dictionary of sets of input keys indexing the same input values
        indexed by the input values.


    >>>invert_dictionary({'a': 2, 'b': 4, 'c': 2})
    {2: {'a', 'c'}, 4: {'b'}}
    '''
    dict_ = {}
    for key, value in d.items():
        dict_.setdefault(value, set()).add(key)
    return dict_

print(invert_dictionary({'a': 2, 'b': 4, 'c': 2}))

print('\n')
#======================================================================================================================

# LIST METHODS 6

def remove_from_back(lst):
    if lst:
        lst.pop()
    return lst

lst = []
print(remove_from_back(lst))

print('\n')
#======================================================================================================================

# CONDITIONALS 6

def is_either_even_or_are_both_7(num1, num2):
    return num1 % 2 == 0 or num2 % 2 == 0 or (num1 == 7 and num2 == 7)

print(is_either_even_or_are_both_7(3,7))
print(is_either_even_or_are_both_7(2,3))
print(is_either_even_or_are_both_7(7,7))

print('\n')
#======================================================================================================================

def is_either_even_and_both_less_than_9(num1, num2):
    return (num1 < 9 and num2 < 9) and (num1 % 2 == 0 or num2 % 2 == 0)

print(is_either_even_and_both_less_than_9(2,4))
print(is_either_even_and_both_less_than_9(72,2))

print('\n')
#======================================================================================================================

# ADVANCED 2

def extend(dict1,dict2):
    for k,v in dict2.items():
        if k not in dict1:
            dict1[k] = v
    return dict1

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 4, 'c': 3}
print(extend(dict1, dict2))

print('\n')
#======================================================================================================================

# DICTIONARY 4

def remove_numbers_larger_than(num, dict1):
    res = {}
    for key in dict1:
        if not (isinstance(dict1[key], int) and dict1[key] > num):
            res[key] = dict1[key]
    return res

dictionary = {'a': 8, 'b': 2, 'c': 'montana'}
result = remove_numbers_larger_than(5, dictionary)
print(result)

print('\n')
#======================================================================================================================

# DICTIONARY 4: SECOND METHOD

def remove_numbers_larger_than(target, dictionary):
    removal_list = []
    for key in dictionary:
        if isinstance(dictionary[key], int):
            if dictionary[key] > target: removal_list.append(key)

    for key in removal_list:
        dictionary.pop(key)
    return dictionary

dictionary = {'a': 8, 'b': 2, 'c': 'montana'}
result = remove_numbers_larger_than(5, dictionary)
print(result)

print('\n')
#======================================================================================================================

# DICTIONARY 4: SINGLE LINE METHOD

res = {key : val for key, val in dictionary.items() if not (isinstance(val, int) and (val > 5))}
print(res)

print('\n')
#======================================================================================================================

# DICTIONARY 4: CON'T

def remove_integers_less_than(target, dictionary):
    return {key:value for key, value in dictionary.items() if not (isinstance(value, int) and (value < target))}

dictionary = {'a': 8, 'b': 2, 'c':'montana'}
result = remove_integers_less_than(5, dictionary)
print(result)

print('\n')
#======================================================================================================================

def remove_integers_less_than(target, dictionary):
    res = {}
    for key in dictionary:
        if not (isinstance(dictionary[key], int) and dictionary[key] < target):
            res[key] = dictionary[key]
    return res

dictionary = {'a': 8, 'b': 2, 'c':'montana'}
result = remove_integers_less_than(5, dictionary)
print(result)

print('\n')
#======================================================================================================================

def remove_integers_less_than(target, dictionary):
    removal_list = []
    for key in dictionary:
        if isinstance(dictionary[key], int):
            if dictionary[key] < target: removal_list.append(key)

    for key in removal_list:
        dictionary.pop(key)

    return dictionary

dictionary = {'a': 8, 'b': 2, 'c':'montana'}
result = remove_integers_less_than(5, dictionary)
print(result)

print('\n')
#======================================================================================================================

# DICITONARY 4: CON'T

def remove_string_values_longer_than(target, dictionary):
    return {key:value for key,value in dictionary.items() if not (isinstance(dictionary[key], str) and len(dictionary[key]) > target)}

dictionary = {'name': 'Montana', 'age': 20, 'location': 'Texas'}
result = remove_string_values_longer_than(6, dictionary)
print(result)

print('\n')
#======================================================================================================================

def remove_string_values_longer_than(target, dictionary):
    removal_list = []
    for key in dictionary:
        if isinstance(dictionary[key], str):
            if len(dictionary[key]) > target: removal_list.append(key)

    for key in removal_list:
        dictionary.pop(key)

    return dictionary

dictionary = {'name': 'Montana', 'age': 20, 'location': 'Texas'}
result = remove_string_values_longer_than(6, dictionary)
print(result)

print('\n')
#======================================================================================================================

# DICTIONARY 5

def remove_even_values(dictionary):
    return {key : value for key, value in dictionary.items() if not isinstance(dictionary[key], int) or (value % 2 !=0)}

dictionary = {'a': 2, 'b': 3, 'c': 4, 'd':'Texas'}
output = remove_even_values(dictionary)
print(output)

print('\n')
#======================================================================================================================

def remove_even_values(dictionary):
    removal_list = []
    for key in dictionary:
        if isinstance(dictionary[key], int):
            if dictionary[key] % 2 == 0: 
                removal_list.append(key)

    for key in removal_list:
        dictionary.pop(key)

    return dictionary

dictionary = {'a': 2, 'b': 3, 'c': 4, 'd':'Texas'}
output = remove_even_values(dictionary)
print(output)

print('\n')
#======================================================================================================================

def count_number_of_keys(dictionary):
    return len(dictionary)

dictionary = {'a': 1, 'b': 2, 'c': 3}
output = count_number_of_keys(dictionary)
print(output)

print('\n')
#======================================================================================================================

def count_number_of_keys(dictionary):
    return len(dictionary.keys())

dictionary = {'a': 1, 'b': 2, 'c': 3}
output = count_number_of_keys(dictionary)
print(output)

print('\n')
#======================================================================================================================
def remove_odd_values(dictionary):
    return {key:value for key,value in dictionary.items() if not isinstance(dictionary[key], int) or (value % 2 == 0)}

dictionary = {'a': 1, 'b': 2, 'c': 3, 'd':'montana'}
output = remove_odd_values(dictionary)
print(output)

print('\n')
#======================================================================================================================

def remove_odd_values(dictionary):
    removal_list = []
    for key in dictionary:
        if isinstance(dictionary[key], int):
            if dictionary[key] % 2 == 1: 
                removal_list.append(key)

    for key in removal_list:
        dictionary.pop(key)

    return dictionary

dictionary = {'a': 1, 'b': 2, 'c': 3, 'd':'montana'}
output = remove_odd_values(dictionary)
print(output)

print('\n')
#======================================================================================================================

x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

z = {**x, **y}

print(z)