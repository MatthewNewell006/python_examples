import numpy as np


'''

Numpy Array vs. Python List
At first glance, NumPy arrays are similar to Python lists.
They both serve as containers with fast item getting and setting and somewhat slower inserts and removals of elements.

The hands-down simplest example when NumPy arrays beat lists is arithmetic:

'''

# normal python list with iteration
a = [1,2,3]

print([i * 2 for i in a])


# numpy array
a = np.array([1,2,3])

print(a * 2)


a = [1,2,3]
b = [4,5,6]

print([i+j for i, j in zip(a,b)])


a = np.array([1,2,3])
b = np.array([4,5,6])

print(a + b)

print('\n') # ===================================================================================================

'''

Other than that, NumPy arrays are:

more compact, especially when there’s more than one dimension
faster than lists when the operation can be vectorized
slower than lists when you append elements to the end
usually homogeneous: can only work fast with elements of one type

'''

a = np.array([1,2,3])
print(a.shape, a.dtype)


b = np.zeros(3, int)
print(b, b.dtype)


c = np.zeros_like(a)
print(c, c.shape, c.dtype)


# Actually, all the functions that create an array filled with a constant value have a _like counterpart:

a = np.array([1,2,3])

print(np.zeros(3), np.zeros_like(a))

print(np.ones(3), np.ones_like(a))

print(np.empty(3), np.empty_like(a))

print(np.full(3, 7), np.full_like(a, 7))

print('\n') # ===================================================================================================


# np.arange(start, stop, step)
# np.linspace(start, stop, num)

print(np.arange(1, 6, 2), np.linspace(0, 0.5, 6))

print('\n') # ===================================================================================================


a = np.arange(3)
print(a, a.astype(float))


print(np.random.randint(0,10,3))

# uniform
print(np.random.rand(3))

# normal
print(np.random.randn(3))

# uniform
print(np.random.uniform(1, 10, 3))

# normal
print(np.random.normal(5, 2, 3))

print('\n') # ===================================================================================================
