# calculates nth fibonacci number

def Fibonacci(n):
    '''
    Calculates nth Fibonacci term. 
    Term number must be greater than 0. 

    Inputs:
      n (int): term number
    Returns: nth Fibonacci number
    '''
    assert n > 0

    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return sum([Fibonacci(n-1), Fibonacci(n-2)])