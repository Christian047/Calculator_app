# define the functions needed
# print options to the user
# ask for values
# call the functions
# while loop to continue program

# define the functions needed
def add():
    # ask for values
    a = int(input('Enter your first number: '))
    b = int(input('Enter your first number: '))
    answer = a + b
    print(f'{a} + {b}= {answer}')


def multiplication():
    a = int(input('Enter your first number: '))
    b = int(input('Enter your first number: '))
    answer = a * b
    print(f'{a} * {b}= {answer}')


def Subtract():
    a = int(input('Enter your first number: '))
    b = int(input('Enter your first number: '))
    answer = a - b
    print(f'{a} - {b}= {answer}')


def Divide():
    a = int(input('Enter your first number: '))
    b = int(input('Enter your first number: '))
    answer = a / b
    print(f'{a} /{b}= {answer}')
    
    

# print options to the user
print('Welcome to the Calculator')
print('A. Addition')
print('B. Multiplication')
print('C. Subtraction')
print('D. Division')
print('E. Exit')

# while loop to continue program
while True:
   

    choice = input('Enter your choice: ').upper()

    if choice == 'A':
        add()
    if choice == 'B':
        multiplication()
    if choice == 'C':
        Subtract()
    if choice == 'D':
        Divide()
    elif choice == 'E':
            print('Exiting the Calculator. Goodbye!')
            break
    else:
        print('Invalid choice. Please enter A, B, C, D, or E.')






