from data import DATA, logo
import random

print(logo)
game_on = True
score = 0
while game_on:
    option_1 = random.randint(0,4)
    option_2 = random.randint(0,4)
    print("Does "+DATA[option_1]['name']+" has more followers than")
    print(DATA[option_2]['name']+"?")
    answer = input().lower()
    correct_ans = max(DATA[option_1]['follower count'], DATA[option_2]['follower count'])
    if answer == 'yes' and correct_ans == DATA[option_1]['follower count']:
        score += 1
        print("correct answer")
    elif answer == 'no' and correct_ans == DATA[option_2]['follower count']:
        score += 1
        print("correct answer")
    else:
        score -= 1
        print("wrong answer")
    next = input("Next Question(n) or Quit(q): ").lower()
    if next == 'q':
        game_on = False
        print(score)
    else:
        print(score)
