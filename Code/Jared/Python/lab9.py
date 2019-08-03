# lab 9
# version 1
# def convert_distance(feet): #converts feet to meters
#     feet = 0.3048 # 1 ft to meters
#     ask_user = float(input("Enter the number of feet to convert to meters: "))
#     ft_to_meters = feet * ask_user
#     return ft_to_meters

# VERSION 2 and 3
# def convert_distance_to_meters(distance, units_from):
#     ft_to_meters = distance * 0.3048
#     miles_to_meters = distance * 1609.34
#     kilo_to_meters = distance * 1000
#     yds_to_meters = distance * 0.9144
#     inch_to_meters = distance * 0.0254
#
#     if units_from == 'feet':
#         meters = ft_to_meters
#     elif units_from == 'miles':
#         meters = miles_to_meters
#     elif units_from == 'kilometers':
#         meters = kilo_to_meters
#     elif units_from == "yards":
#         meters = yds_to_meters
#     elif units_from == 'inches':
#         meters = inch_to_meters
#     elif units_from == 'meters':
#         meters = distance
#     return meters


# version 4
def convert_distance_to_meters(distance, units):
    converter = {
        'feet': 0.3048,
        'miles': 1609.34,
        'kilometers': 1000,
        'yards': 0.9144,
        'inches': 0.0254,
        'meters': 1
    }
    return distance * converter[units]


def convert_distance_from_meters(distance, units):
    converter = {
        'feet': 0.3048,
        'miles': 1609.34,
        'kilometers': 1000,
        'yards': 0.9144,
        'inches': 0.0254,
        'meters': 1
    }

    return distance / converter[units]


distance = float(input("Enter a distance: (type a number)"))
from_unit = input("Choose the unit you wish to convert from:")
to_unit = input("Choose the unit you wish to convert to: ")
if to_unit == 'meters':
     print(convert_distance_to_meters(distance, from_unit))
else:
    print(convert_distance_from_meters(convert_distance_to_meters(distance, from_unit), to_unit))
