import sys
import random

def extract_digit(name):
    l = list()
    for i in name:
        if i.isdigit():
            l.append(i)
        else :
            l=l    
    return ''.join(l)
    
greetings=['Hello','Hola','Bonjour','Good Morning','Konichiwa','Buenos dia','Salam','what\'sup']
greet = random.choice(greetings)

if len(sys.argv) == 1:
    print('Fuck off Libtard')
elif sys.argv[1].isalpha():
    print('{} {}'.format(greet,sys.argv[1]))
else:
    robot=extract_digit(sys.argv[1])
    print('bipbip {}'.format(robot))
    sys.argv[1] == int()
    
