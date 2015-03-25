def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    x = min(a,b)
    while a%x or b%x != 0:
        x-=1
    return x