# Dictionary 6

def remove_list_values(dictionary):
    return {key:value for key, value in dictionary.items() if not isinstance(dictionary[key], list)}

dictionary = {'a': [1, 3, 4], 'b': 2, 'c': ['hi', 'there']}

output = remove_list_values(dictionary)
print(output)

print('\n') # =======================================================================================================================

# Dictionary 6 Alt

def remove_list_values(dictionary):
    removal_list = []
    for key in dictionary:
        if isinstance(dictionary[key], list):
                removal_list.append(key)

    for key in removal_list:
        dictionary.pop(key)

    return dictionary

dictionary = {'a': [1, 3, 4], 'b': 2, 'c': ['hi', 'there']}

output = remove_list_values(dictionary)
print(output)

print('\n') # =======================================================================================================================

def remove_number_values(dictionary):
    return {key:value for key, value in dictionary.items() if not isinstance(dictionary[key], (int, float))}

dictionary = {'a': 3.4, 'b': 2, 'c': ['hi', 'there'], 'd':'hi'}

output = remove_number_values(dictionary)
print(output)

print('\n') # =======================================================================================================================

def remove_number_values(dictionary):
    removal_list = []
    for key in dictionary:
        if isinstance(dictionary[key], (int,float)):
                removal_list.append(key)

    for key in removal_list:
        dictionary.pop(key)

    return dictionary

dictionary = {'a': 3.4, 'b': 2, 'c': ['hi', 'there'], 'd':'hi'}

output = remove_number_values(dictionary)
print(output)

print('\n') # =======================================================================================================================

def remove_string_values(dictionary):
    return {key:value for key, value in dictionary.items() if not isinstance(dictionary[key], str)}

dictionary = {'name': 'Sam', 'age': 20}

output = remove_string_values(dictionary)
print(output)

print('\n') # =======================================================================================================================

# List String Methods 2

def convert_double_space_to_single(string):
    return ' '.join(string.split('  '))

output = convert_double_space_to_single("string  with  double  spaces")
print(output)

print('\n') # =======================================================================================================================

# List Methods 7

def join_three_lists(list1, list2, list3):
    return list1 + list2 + list3

output = join_three_lists([1, 2], [3, 4], [5, 6])
print(output)

print('\n') # =======================================================================================================================

def add_to_front_of_new(list1, element):
    result = [element]
    return result + list1

list1 = [1, 2]

output = add_to_front_of_new(list1, 3)
print(output)

print('\n') # =======================================================================================================================

def add_to_front_of_new(new_list, element):
    new_list.insert(0,element)
    return new_list

new_list = [1, 2]
print(new_list)

output = add_to_front_of_new(new_list, 3)
print(output)
print(new_list)

print('\n') # =======================================================================================================================

def add_to_back_of_new(list1, element):
    result = [element]
    return list1 + result

list1 = [1, 2]

output = add_to_back_of_new(list1, 3)
print(output)

print('\n') # =======================================================================================================================

def get_all_elements_but_nth(list1, n):
    result = list1[:n] + list1[n + 1:]
    return result

list1 = ['a', 'b', 'c']

n = 1

output = get_all_elements_but_nth(list1, 1)
print(output)

print('\n') # =======================================================================================================================

# Iteration Methods 7

def get_index_of(char, string):
    return string.find(char)

output = get_index_of('a', 'I am a hacker')
print(output)

print('\n') # =======================================================================================================================

def get_index_of(char, string):
    for index, character in enumerate(string):
        if character == char: return index
    return -1

output = get_index_of('a', 'I am a hacker')
print(output)

print('\n')

output = get_index_of('z', 'I am a hacker')
print(output)

print('\n') # =======================================================================================================================

# Conditional 7

def are_valid_credentials(name, password):
    '''
    Given a name and a password, "are_valid_credentials",
    returns True if the name is longer than 3 characters AND
    the password is at least 8 characters long.
    Otherwise it returns False.
    '''
    return len(name) > 3 and len(password) >= 8

output = are_valid_credentials('Ritu', 'mylongpassword')
print(output)

print('\n') # =======================================================================================================================

def find_min_length_of_three_words(word1, word2, word3):
    lst = [word1, word2, word3]
    return len(min(lst, key = len))

output = find_min_length_of_three_words('a', 'be', 'see')
print(output)

print('\n') # =======================================================================================================================

def find_min_length_of_three_words(word1, word2, word3):
    return min(len(word1), len(word2), len(word3))

output = find_min_length_of_three_words('a', 'be', 'see')
print(output)

print('\n') # =======================================================================================================================

def find_max_length_of_three_words(word1, word2, word3):
    return max(len(word1), len(word2), len(word3))

output = find_max_length_of_three_words('a', 'be', 'see')
print(output)

print('\n') # =======================================================================================================================

# Advanced 3

def select(input_list, input_dict):
    return {key:value for key, value in input_dict.items() for i in input_list if i == key}

input_list = ['a', 'c', 'e']

input_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

output = select(input_list, input_dict)
print(output)

print('\n') # =======================================================================================================================