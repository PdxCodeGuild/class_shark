import random

def show_Recent_Score_Grade(score, grade):
    names = ['Jackie', 'Bobby','Sue', 'Tyler']
    op_Score = random.randint(65, 101)
    print(f'Your score was ' + str(score) + ' which is ' + grade)
    if op_Score > score:
        print(f'\n Just to let you know, ' + random.choice(names) +
        ' got a better score of ' + str(op_Score) + ' try harder next time')
    else:
        print(f'\n Just to let you know, ' + random.choice(names) +
        ' got a worse score of ' + str(op_Score) + ' great job I guess.')

def grader(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def adv_VTwo(sc):
    t_score = sc
    p_or_m = t_score % 10
    if t_score < 60:
        return ''
    elif p_or_m >= 7:
        return '+'
    elif p_or_m <= 3:
        return '-'
    else:
        return ''

def again():
    choice = input('Would you like to grade another score? y/n ')
    if choice == 'y':
        grade_Me()
    elif choice == 'n':
        print('Goodbye')
    else:
        print('incorrect input')
        again()

def grade_Me():
    score = input('Please enter your score: ')
    score = int(score)
    grade = grader(score)
    grade += adv_VTwo(score)
    show_Recent_Score_Grade(score, grade)
    again()

grade_Me()
