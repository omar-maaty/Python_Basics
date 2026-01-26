import random
import os
rnd=random.randint(1,100)
att=0
file_path='score.txt'
score=100
if os.path.exists(file_path):
    with open(file_path,'r') as f:
        cont=f.read()
        if cont:
            score=int(cont)
print(f'Current High Score to beat: {score}')

while True:
    try:
        x = int(input('guess a number: '))
        att+=1
        if x > rnd:
            print('Too High')
        elif x < rnd:
            print('Too Low')
        elif x == rnd:
            print(f'Good job, you did it in {att} attempts')
            if att<score:
                print('New High score')
                with open(file_path,'w') as f:
                    f.write(str(att))
            else:
                print(f'Hard luck, High score is still {score}')
            break
    except ValueError:
        print('enter a valid number')
