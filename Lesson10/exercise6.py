'''
@author: cristianlepore
'''

def isPrime(num, primes):
    '''
    input: an int num and a list of primes called primes
    output: a boolean

    returns True if num is prime, False otherwise
    '''
    count = 0
    if num == 0 or num == 1:
        return False
    for p in primes:
        if (num % p) != 0:
            count += 1
    if count == len(primes):
        return True
    return False


def genPrimes():
    '''
    generator
    '''
    primes = []
    num = 0
    while True:
        if isPrime(num, primes):
            primes.append(num)
            yield num
        num += 1


prime = genPrimes()
while True:
    print(prime.__next__())
