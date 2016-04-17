print('Hello, Django girls.')

def hello(name):
    if name == '':
        print('Hello, world!')
    else:
        print('Hello, ' + name)

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', '']

def greetings(people):
    for name in people:
        hello(name)

def count(n):
    for i in range(0, n):
        print(i)

# MAIN
# greetings(girls)
# count(5)
# hello('Hamster')
# hello('')

class Cat():
    name = 'Mewer'
    food = []

cat1 = Cat()
print(cat1.food)

cat2 = Cat()
print(cat2.food)

cat1.food.append('Fish')
# cat1.__class__.name
print(cat1.food)
print(cat2.food)

