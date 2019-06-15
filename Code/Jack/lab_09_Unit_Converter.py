import math
import again


# Defines user choices
s_Units_Allowed = ['ft', 'mi', 'm', 'km', 'yd', 'inch']

class Converter(object):

    ''' To add more units, create a new line with as such

        U = U per m

        and then append to the end of m = {...'U':U}

        don't forget to add the choice to s_Units_Allowed
    '''

    ft = 0.3048
    mi = 1609.34
    km = 1000
    yd = 0.9144
    inch = 0.0254
    m = {'ft':ft, 'mi':mi, 'm':1, 'km':km, 'yd':yd, 'inch':inch}


    def __init__(self, dc_Dist_In, s_Unit_In, s_Unit_Out):
        super(Converter, self).__init__()
        self.UI = s_Unit_In
        self.UO = s_Unit_Out

        # Converts dist to meters
        self.dist = dc_Dist_In

    def getConv(self):

        return (self.dist * self.m[self.UI]) * (1/self.m[self.UO])




while True:
    sep = ', '
    units = sep.join(s_Units_Allowed)
    dc_Usr_Dist_In = float(input('What is the distance you wish to convert? '))
    s_Usr_Unit_In = input(f'What are the units measured? {units}: ')
    s_Usr_Unit_Out = input(f'What are the desired units? {units}: ')
    usr_Conv = Converter(dc_Usr_Dist_In, s_Usr_Unit_In, s_Usr_Unit_Out)
    print(f'\nYour converted distance is : {usr_Conv.getConv():.2f}{usr_Conv.UO}')
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
