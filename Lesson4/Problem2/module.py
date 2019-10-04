def newMonthlyBalance(balance, annualInterestRate, monthlyPayment):
    '''
    input: three numbers. Balance, annual interest rate and monthly payment rate.
    output: one number. The new balance at the end the year
    '''

    def monthlyInterestRate(annualInterestRate):
        '''
        input: one number. The annual interest rate.
        output: one number. The monthly interest rate.
        '''
        return annualInterestRate / 12.00

    def monthlyUnpaidBalance(balance, monthlyPayment):
        '''
        input: two number. The previous balance and the minimum monthly payment.
        output: one number. The monthly unpaid balance
        '''
        return balance - monthlyPayment

    def unpaidBalanceEachMonth(monthlyUnpaidBalance, annualInterestRate):
        '''
        input: two numbers. The monthly unpaid balance, the annual interest rate.
        output: one number. The unpaid balance of each month.
        '''
        return monthlyInterestRate(annualInterestRate) * monthlyUnpaidBalance + monthlyUnpaidBalance

    monthlyUnpaidBalance = monthlyUnpaidBalance(balance, monthlyPayment)
    monthlyBalance = round(unpaidBalanceEachMonth(monthlyUnpaidBalance, annualInterestRate), 2)

    return monthlyBalance
