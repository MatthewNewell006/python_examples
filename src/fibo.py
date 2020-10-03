# Fibonacci number module

def fib(n):     # write a Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end = ' ')
        a, b = b, a+b
    print()

def fib2(n):    # return a Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

if __name__ == '__main__':
    ''' Run the funcitons'''
    
    fib(1000)

    print('\n')

    print(fib2(100))