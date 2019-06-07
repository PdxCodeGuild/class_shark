import math
import decimal
import again


decimal.getcontext().prec = 5


class Converter(object):
    """docstring for Converter."""
    ft = {'ft':1, 'mi':1/5280, 'm':1/3.28084, 'km':1/3280.84}
    mi = {'ft':5280, 'mi':1, 'm':1609.34, 'km':1.60934}
    m = {'ft':3.28084, 'mi':1/1609.34, 'm':1, 'km':1/1000}
    km = {'ft':3280.84, 'mi':1/1.60934, 'm':1000, 'km':1}
    conv = {'ft':ft, 'mi':mi, 'm':m, 'km':km}

    def __init__(self, f_Dist_In, s_Unit_In, s_Unit_Out):
        super(Converter, self).__init__()
        self.dist = f_Dist_In
        self.UI = s_Unit_In
        self.UO = s_Unit_Out

    def getConv(self):
        #Finds corresponding values within nested dicts
        uo = decimal.Decimal(self.conv[self.UI][self.UO])
        new_Dist = decimal.Decimal(self.dist * uo)
        return new_Dist



s_Units_Allowed = 'ft, mi, m, or km '
while True:
    f_Usr_Dist_In = decimal.Decimal(input('What is the distance you wish to convert? '))
    s_Usr_Unit_In = input('What are the units measured? ' + s_Units_Allowed)
    s_Usr_Unit_Out = input('What are the desired units? (ft, mi, m, or km) ')
    usr_Conv = Converter(f_Usr_Dist_In, s_Usr_Unit_In, s_Usr_Unit_Out)
    dc_Usr_Conv_Dist_Out = usr_Conv.getConv()
    print(f'\nYour converted distance is : {dc_Usr_Conv_Dist_Out}{usr_Conv.UO}')
    if again.again('\nWould you like to convert another distance?'):
        break



################################################################################
##################### USE THIS IF 'again.py' NOT CLONED ########################
################################################################################
# def again(question):
#     choice = input(f'{question} y/n\n')
#     if choice == 'n':
#         return True
#     elif choice == 'y':
#         return False
#     else:
#         print('Incorrect input')
#         return False
