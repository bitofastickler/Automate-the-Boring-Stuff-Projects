import random
import time
import sys

messages = ['It is decidedly so', 'Yes definitely',
            'Reply hazy try again',
            'Ask again later', 'Concentrate and ask again',
            'My reply is no', 'Outlook not so good', 'Very doubtful']

while True:
    print('What would you like to know?')
    userQuestion = input()
    if userQuestion == '':
        sys.exit()
    else:
        time.sleep(1)
        print(messages[random.randint(0, len(messages) - 1)])

