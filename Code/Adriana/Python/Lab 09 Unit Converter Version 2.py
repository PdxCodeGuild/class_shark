#version 2 inclusion:
#1 ft is 0.3048 m
#1 mi is 1609.34 m
#1 m is 1 m
#1 km is 1000 m

#need to come back to this

meters_conversion = {'feet': .3048, 'meters': 1, 'mile': 1609.34, 'kilometer': 1000}

distance = int(input("What is the distance you would like to convert?" ))
output_units = input("What output units would you like - feet, meters, mile or kilometer??")

print(f"{distance} meters is {distance*meters_conversion[output_units]}{output_units}")