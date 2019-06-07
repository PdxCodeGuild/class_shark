"""
Name:           Scott Tran
Date            6/5/2019
Assignment:     Make program that prompts the user for several inputs then prints a Mad Lib as the result.
"""
# inpsired by https://www.posttypography.com/project-archive/mad-lib-posters-double-dagger

Play = True

while Play:
    City = input("What city do you live in?  ") 
    Day = input("What is a day in the week are you free?  ")
    Venue = input("What is a really cool place?  ")

    Band = input("What are three of your favorite bands?  Please seperate each band using a space.  ")
    BandList = Band.split(" ")

    Adjective = input("Give me three adjective? Please seperate each band using a space.  ")
    AdjList = Adjective.split(" ")

    print(f"\nCandy Cigarettes is playing in {City} on {Day} at a really cool spot called {Venue}. They're playing with {BandList[0]} and {BandList[1]} but not {BandList[2]}.  I think that this show will be really {AdjList[0]}! I hear that there will be {AdjList[1]} girls and {AdjList[2]} boys there.")

    again = input("\nWould you like to play Mad Lib again? please type 'yes' or 'no':  ")
    if again == "no":
        Play = False
