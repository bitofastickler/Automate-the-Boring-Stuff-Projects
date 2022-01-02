import time
name = 0
while not name:
    print('Enter your name.')
    name = input()
time.sleep(1)
numOfGuests = False
print('How many guests will you have?')
while True:
    numOfGuests = int(input())
    if numOfGuests < 0:
        print('Please enter a positive number')
    if numOfGuests > -1:
        break
time.sleep(1)
print('Make sure to have enough room for all your guests.')
time.sleep(1)
print('All done!')



