from random import randrange

def swap(a, b):
    temp = a
    a = b
    b = temp

def gcd(a, b):
    if a < b:
        swap(a,b)
    
    # a >= b
    r = a % b
    if r == 0:
        return b
    else :
        return gcd(b, r)

def extended_gcd(a,b):
    """
    Returns the extended gcd of a and b

    Parameters 
    ----------
    a : Input data.
    b : Input data.
    Returns
    -------
    (d, x, y): d = gcd(a,b) = a*x + b*y
    """

    big = max(a,b)
    small = min(a,b)

    r = big % small
    q = big // small

    if (r==0):
        return small,0,0

    son_gcd, x, y = extended_gcd(small,r)
    
    if (x==0 and y==0):
        return son_gcd,1,-q

    return son_gcd,y,int(x-q*y)


# a = e, n = (p-1)(q-1)
def modular_inverse(a,n):
    """
    Returns the inverse of a modulo n if one exists

    Parameters
    ----------
    a : Input data.
    n : Input data.

    Returns
    -------
    x: such that (a*x % n) == 1 and 0 <= x < n if one exists, else None
    """
    (gcd, x, y) = extended_gcd(n,a) # y*a + x*n = 1
    print(gcd, x, y)
    return y % n


# bin(10)[2:] = 1010
# bin(10) = 0b1010

def modular_exponent(a, d, n):
    # bin_a = bin(a)
    
    """
    Returns a to the power of d modulo n

    Parameters
    ----------
    a : The exponential's base.
    d : The exponential's exponent.
    n : The exponential's modulus.

    Returns
    -------
    b: such that b == (a**d) % n
    """
    
    a = a % n

    i = 0
    tmp = 1
    for i in range(len(bin(d)) - 2):
        
        tmp *= a ** (d & (2**i))
        tmp %= n

    return tmp

def miller_rabin(n):
    """
    Checks the primality of n using the Miller-Rabin test

    Parameters
    ----------
    n : The number to check

    Returns
    -------
    b: If n is prime, b is guaranteed to be True.
    If n is not a prime, b has a 3/4 chance at least to be False
    """
    a = randrange(1,n)
    k = 0
    d = n-1
    while d % 2 == 0:
        k = k + 1
        d = d // 2
    x = modular_exponent(a, d, n)
    if x == 1 or x == n-1:
        return True
    for _ in range(k):
        x = (x * x) % n
        if x == 1:
            return False
        if x == n-1:
            return True
    return False

def is_prime(n):
    """
    Checks the primality of n

    Parameters
    ----------
    n : The number to check

    Returns
    -------
    b: If n is prime, b is guaranteed to be True.
    If n is not a prime, b has a chance of less than 1e-10 to be True
    """
    for _ in range(10):
        if not miller_rabin(n):
            return False
    return True

def generate_prime(digits):
    for i in range(digits * 10):
        n = randrange(10**(digits-1), 10**digits)
        if is_prime(n):
            return n
    return None