import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Adivina un numero entre 1 y {x}: '))
        if guess < random_number:
            print('Lo siento, prueba otra vez. Muy bajo.')
        elif guess > random_number:
            print('Lo siento, prueba otra vez. Muy alto.')

    print(f'Bien, enhorabuena. Has adivinado el numero {random_number} correctamente!!')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'Es {guess} muy alto (A), muy bajo (B), o correcto (C)?? ').lower()
        if feedback == 'a':
            high = guess - 1
        elif feedback == 'b':
            low = guess + 1

    print(f'Bien! El ordenador adivinó tu numero, {guess}, correctamente!')


guess(100)
input()