# filename: "scantron.py"
from random import choice
options = ['a', 'b', 'c', 'd', 'e']
answer_sheet = ['a', 'c', 'e', 'e', 'd', 'b', 'e']
lewis_answers = []
for num in range(len(answer_sheet)):
    lewis_answers.append(choice(options))
correct_answers = 0
for num in range(len(answer_sheet)):
    if lewis_answers[num] == answer_sheet[num]:
        correct_answers += 1
print(f"{correct_answers} correct answers!")
