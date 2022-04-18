#!/usr/bin/python3

# run this to make executable systemwide:
# chmod +x standup.py && ln -sv standup.py ~/usr/local/bin/standup

from os import system
import random


title = """
   _____ __                  __
  / ___// /_____ _____  ____/ /_  ______
  \__ \/ __/ __ `/ __ \/ __  / / / / __ \\
 ___/ / /_/ /_/ / / / / /_/ / /_/ / /_/ /
/____/\__/\__,_/_/ /_/\__,_/\__,_/ .___/
                                /_/
"""

footer = """
    ___    ____       __                 __
   /   |  / / /  ____/ /___  ____  ___  / /
  / /| | / / /  / __  / __ \/ __ \/ _ \/ / 
 / ___ |/ / /  / /_/ / /_/ / / / /  __/_/  
/_/  |_/_/_/   \__,_/\____/_/ /_/\___(_)
"""

grey   = '\33[90m'
bold   = '\033[1m'
italic = '\033[3m'
end    = '\033[0m'
pad = '    '

team = [
    'Dustin',
    'Bezos',
    'Gates',
    'Elon-chan',
    'Shkreli',
]

random.shuffle(team)

count = 0
while(count <= len(team)):
    system('clear')
    print(f'{bold}{title}{end}')

    for key, value in enumerate(team):
        if key < count:
            print(f'{pad}{pad}{grey}{team[key]}{end}')
        elif key == count:
            print(f'{pad}{bold} -> {team[count]} <- {end}')
        else:
            print(f'{pad}{pad}{value}')

    if count < len(team):
        input()
    count += 1

print (f'{bold}{footer}{end}')
input()
system('clear')
