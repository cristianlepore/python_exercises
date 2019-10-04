# Import the required library
import math

def polySum(n, s):
    '''
    input: two arguments n and s
    output: one number with rounded to four decimal places that sums the area and the square of the perimeter of the regular polygon.
    '''

    def area(n, s):
        '''
        input: two arguments n and s
        output: one number that is the area of the regular polygon
        '''
        return (0.25 * n * s**2) / math.tan(math.pi / n )

    def perimeter(n, s):
        '''
        input: two arguments n and s
        output: return one number that is the perimeter of the polygon
        '''
        return n * s

    a = area(n, s)
    p = perimeter(n, s)

    # Value returned by the function polySum
    return round(a + p**2, 4)
