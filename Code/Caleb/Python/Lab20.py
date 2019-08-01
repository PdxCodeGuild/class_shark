'''
Lab 20: Credit Card Validation
Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

Convert the input string into a list of ints
Slice off the last digit. That is the check digit.
Reverse the digits.
Double every other element in the reversed list.
Subtract nine from numbers over nine.
Sum all values.
Take the second digit of that sum.
If that matches the check digit, the whole card number is valid.
'''
class CreditCardValidation(object):
    '''
    This is the class for the main Credit Card Validation Logic
    
    Parameters: Credit Card Input

    The logic will then perform the stated above steps, and return whether or not that inputted credit card number is valid.
    '''

# def credit_card_validation(x):
    list_of_ints =[]
    check_digit = 0

    def __init__(self, credit_num_input):
        super(CreditCardValidation, self).__init__()
        self.list_of_ints = list(str(credit_num_input))
        for r in range(len(self.list_of_ints)):
            self.list_of_ints[r] = int(self.list_of_ints[r])
        check_digit = self.list_of_ints.pop(-1)
        self.list_of_ints.reverse()
        for q in range(len(self.list_of_ints)):
            if q % 2 == 0:
                self.list_of_ints[q] *= 2
        for y in range(len(self.list_of_ints)):
            if self.list_of_ints[y] > 9:
                self.list_of_ints[y] -= 9
        sum = 0
        for z in range(len(self.list_of_ints)):
            sum += self.list_of_ints[z]
        sum = str(sum)
        final_check_dig = int(sum[1])
        if int(sum[1]) == check_digit:
            print('Credit Card is Valid! Thanks for Checking.')
        else:
            print('Credit Card is not Valid!')


if __name__ == "__main__":
    CreditCardValidation(4556737586899855)
    CreditCardValidation(4556737586899854)
    CreditCardValidation(45567375868998445)