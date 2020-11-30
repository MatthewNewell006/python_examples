def central_tendencies(num_list):

    num_list.sort()
    length = len(num_list)
    mean = sum(num_list) / length

    if (length % 2 == 0):
        median = (num_list[(length) // 2]) + (num_list[(length) // 2 - 1] / 2)
    else:
        median = num_list[(length - 1) // 2]

    mode = max(set(num_list), key = num_list.count)
    central_vals = (mean, median, mode) # return tuple

    return central_vals

print(central_tendencies([1,1,3,5,6,8,4,4,4,7]))

print('\n') # ========================================================================================================================

# Permutations: (Order Matters)

import math

n = 4
r = 2

print(math.factorial(n)) # n!
print((math.factorial(n) / math.factorial(n - r))) # with out repetition

# n! / n1! * n2! * n3! ........ nk! (Different Objects)

# (n - 1)! (Ways to arrange distinct objects in circle)

print('\n') # ========================================================================================================================

# Combinations: (Order Doesn't Matter)

# Cnr = n! / r! * (n - r)!