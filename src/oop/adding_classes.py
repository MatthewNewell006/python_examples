import operator

class Add_obj:
    def __init__(self, *num):
        self.num = num

    def __repr__(self):
        return 'Add_obj{}'.format(self.num)
    
    def __add__(self, other):
        return self.__class__(*[num1+num2 for num1, num2 in zip(self.num, other.num)])


obj1 = Add_obj(2, 5)
obj2 = Add_obj(4, 7)
print(obj1 + obj2)

print('\n')
#=======================================================================================================

class Add_obj:
    def __init__(self, *num):
        self.num = num

    def __repr__(self):
        return 'Add_obj{}'.format(self.num)
    
    def __add__(self, other):
        return self.__class__(*map(operator.add, self.num, other.num))


obj1 = Add_obj(2, 5)
obj2 = Add_obj(4, 7)
print(obj1 + obj2)

print('\n')
#=======================================================================================================

class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return (self.name + ' ('+str(self.capacity)+'L)')
    
    def __add__(self, other):
        return self.__class__(self.name + '&' + other.name, self.capacity + other.capacity)

a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)

result = a + b
print(result)