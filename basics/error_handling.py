# learn about error handling

def get_input():
    print('What is your name?')
    name = input()
    print('What is your age?')
    age = int(input())
    return (name, age)

while 1:
    try:
        name, age = get_input()
        print('Hello ' + name + ' you are ' + str(age) + ' years old')
        break
    except ValueError:
        print('Incorrect value')
        continue
