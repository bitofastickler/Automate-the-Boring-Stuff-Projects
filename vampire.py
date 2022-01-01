name = input('Greetings human, what is your name?') #asks and sets value for name
if name == 'Amanda':
    print('Hey good looking')
if name != 'Amanda':
    print('How old are you?') #should only ask name if not Amanda
    age = input()
    if int(str(age)) == 12:
        print('Thats right, your birthday is in August...')
    elif int(str(age)) < 35:
        print('You are not Amanda, kiddo')
    elif int(str(age)) > 100:
        print('Unlike you, Amanda is not an undead immortal vampire.')
    elif age > 40:
        print('You are not Amanda, granny.')
