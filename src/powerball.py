from collections import Counter

import random
from random import randint, choice

print('\n')
# numbers = [2,57,58,60,65,51,54,57,60,69,4,5,17,43,52,7,15,18,32,45,13,15,17,45,
#           63,14,16,37,48,58,23,32,33,45,49,2,6,40,42,55,11,28,37,40,53,18,20,27,
#           45,65,10,24,27,35,53]

# power_ball = [26,11,5,20,13,18,14,24,13,6,18]


numbers = [4,23,37,61,67,27,32,34,43,52,6,13,38,39,53,10,24,27,35,53,3,43,45,61,65]

n1 = [4,27,6,10,3]
n2 = [23,32,13,24,43]
n3 = [37,34,38,27,45]
n4 = [61,43,39,35,61]
n5 = [67,52,53,53,65]

power_ball = [7,13,6,18,14]



print('NUMBERS: \n', Counter(numbers), '\n', '\nTOP_5: \n', Counter(numbers).most_common(5))
print('\n')

print('POWERBALL: \n', Counter(power_ball),  '\n', '\nMOST_COMMON: \n', Counter(power_ball).most_common(3))
print('\n')

print('\n')

quick_pick = [randint(1, 69) for _ in range(5)]
quick_powerball = [randint(1, 26)]

print('QUICK_PICK: \n', quick_pick)
print('QUICK_POWERBALL: \n', quick_powerball)

print('\n')

y = range(1, 69)
choice_numbers = [choice(y) for i in range(5)]

z = range(1, 26)
choice_powerball = [choice(z)]

print('CHOICE_NUMBERS: \n', choice_numbers)
print('CHOICE_POWERBALL: \n', choice_powerball)


print('\n') # ================================================================================================================================