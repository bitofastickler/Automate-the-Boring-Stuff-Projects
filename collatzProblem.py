def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print(number)
        elif number % 2 == 1:
            number = 3 * number + 1
            print(number)

while True:
    try:
        n = int(input('enter a number'))
        if n <= 0:
            print('enter positive whole numbers only')
            continue
        collatz(n)
    except ValueError:
        print('Please use whole numbers only.')
        continue
