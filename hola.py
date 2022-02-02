import sys
import random


greetings=['Hello','Hola','Bonjour','Good Morning','Konichiwa','Buenos dia','Salam','what\'sup']

greet = random.choice(greetings)

if len(sys.argv)==1:
    print('Fuck off Libtard')
elif sys.argv[1].isdigit():
    print('bipbip {}'.format(sys.argv[1]))
    sys.argv[1]==int()
else:
    print('{} {}'.format(greet,sys.argv[1]))
