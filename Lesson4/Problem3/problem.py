from module import *

# The outstanding balance on the credit card
balance = 999999
# AnnualInterestRate
annualInterestRate = 0.18
# Minimum monthly payment rate as a decimal
monthlyPaymentLowerBound = balance / 12.0
# Upper bound of the monthly payment
monthlyPaymentUpperBound = (balance * (1 + monthlyInterestRate(annualInterestRate))**12) / 12
# Number of months in a year
monthsInAYear = 12

startingBalance = balance
while balance != 0:
    monthlyPayment = round((monthlyPaymentLowerBound + monthlyPaymentUpperBound) / 2.0, 2)
    balance = startingBalance
    for i in range(monthsInAYear):
        # Iterate over the months of the year
        monthlyBalance = newMonthlyBalance(balance, annualInterestRate, monthlyPayment)
        balance = int(monthlyBalance)
        i += 1

    if balance > 0:
        monthlyPaymentLowerBound = monthlyPayment
    else:
        monthlyPaymentUpperBound = monthlyPayment

print("Minimum monthly payment:", end=' ')
print(round(monthlyPayment, 2))