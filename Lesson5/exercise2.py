'''
@author: cristianlepore
'''

def quotient_and_reminder(x, y):
    '''
    input: two numbers
    output: a tuple with the quotient and the reminder
    '''
    q = x // y
    r = x % y
    return  (q, r)

(quot, rem) = quotient_and_reminder(4, 5)
print("Quotient:", end=' ')
print(quot)
print("Reminder:", end=' ')
print(rem)
