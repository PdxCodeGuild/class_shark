#scantron.py
import random
options = ['a', 'b', 'c', 'd', 'e']
answer_sheet = ['a', 'b', 'c', 'e', 'd', 'b', 'e']
lewis_answers = ['a', 'b', 'c', 'e', 'e', 'r', 'a']
for num in range(len(answer_sheet)):
    lewis_answers.append(random.choice(options))

correct_answers = 0
for num in range(len(answer_sheet)):
    if lewis_answers[num] == answer_sheet[num]:
        correct_answers += 1

print(f"{correct_answers} correct answers!")
