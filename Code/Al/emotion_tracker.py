# emotion_tracker.py
emotion_dict = {}
while True: # This REPL will run until the user types 'done'
    user_input = input("How are you feeling? (type 'done' to leave) >")
    if user_input == 'done':
        break 
    if user_input in emotion_dict.keys(): # If we've seen the emotion before
        emotion_dict[user_input] += 1 # make the counter go up by one
    else: # If this is the first time we're seeing the emotion
        emotion_dict[user_input] = 1 # set a new counter and start it at one
    print(emotion_dict)

# Example data: emotion_dict = {'sad': 1, 'happy': 3, 'hungry': 1}

biggest_num = 0
for emotion in emotion_dict: # Iterate over the keys of the dictionary
    if emotion_dict[emotion] > biggest_num: # If the integer value is the biggest seen yet
        biggest_num = emotion_dict[emotion] # Set the 'biggest num' to that value
    print(f"You felt {emotion} {emotion_dict[emotion]} times.")
print(f"You mostly feel {emotion_dict[biggest_num]}")
print(emotion_dict)
