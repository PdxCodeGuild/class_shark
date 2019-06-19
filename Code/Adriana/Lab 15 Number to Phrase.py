#Lab 15: NUMBER TO PHRASE


ones = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
teens = {10: 'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15: 'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}
hundee = {00:'zeroty', 10: 'onety', 20: 'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60: 'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}
#listing a dictionaries conversion from number to phrase

def get_words(num):
    if num < 10:
        return ones[num]
    elif num < 20:
        return teens[num]
    elif num < 100:
        tens_digit = num // 10
        ones_digit = num % 10
        ten_digit_new = tens_digit * 10
        return hundee[ten_digit_new]+'-'+ones[ones_digit]

