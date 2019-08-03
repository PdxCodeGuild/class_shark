# magic 8 ball
import random
magic_ball = ["yes", "no", "perhaps", "not today, but maybe tomorrow", "never in your wildest dreams", "don't count on it", "ask again", "Without a doubt", "Most likely"]

greeting = ("Welcome! Come discover your forturne.")

while True:
    print(greeting)
    print("Ask me a question about your future!")
    user_answer = input()
    print(random.choice(magic_ball))

    play_again = input('Would you like to play again?: yes/no')
    if play_again == ('no'):
            break
