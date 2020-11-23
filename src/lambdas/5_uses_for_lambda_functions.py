def add_ten(x):
    return x + 10

print(add_ten(5))

lambda_add_ten = lambda x: x + 10
print(lambda_add_ten(5))

print('\n')
#==========================================================================================================================

numbers = [1, 12, 37, 43, 51, 62, 83, 43, 90, 2020]
odd_number = []

for n in numbers:
    if n % 2 == 1:
        odd_number.append(n)

print(odd_number)


print(list(filter(lambda x: x % 2 == 1, numbers)))

print('\n')
#==========================================================================================================================

leaders = ['Warren Buffett', 'Yang Zhou', 'Tim Cook', 'Elon Musk']
print(leaders)

leaders.sort(key = lambda x: len(x))
print(leaders)

print('\n')

leaders = {4: 'Yang Zhou', 2: 'Elon Musk', 3: 'Tim Cook', 1: 'Warren Buffett'}
print(leaders)

leaders = dict(sorted(leaders.items(), key = lambda x: x[0]))
print(leaders)

print('\n')
#==========================================================================================================================

print((lambda x, y: x * y) (2, 3))

print('\n')
#==========================================================================================================================

def outer_func():
    leader = 'Yang Zhou'
    def print_leader(location = ''):
        return leader + ' in the ' + location
    return print_leader

Lead = outer_func()('UK')
print(Lead)

def outer_funct():
    leader = 'Yang Zhou'
    return lambda location = '': leader + ' in the ' + location

Lead = outer_funct()('USA')
print(Lead)