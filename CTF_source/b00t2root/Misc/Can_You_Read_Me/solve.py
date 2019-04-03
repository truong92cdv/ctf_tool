message = """pikachu pika pikachu pika pika pi pi pika pikachu pika pikachu pi pikachu pi pikachu pi pika pi pikachu pikachu pi pi pika pika pikachu pika pikachu pikachu pi pika pi pika pika pi pikachu pikachu pi pikachu pi pika pikachu pi pikachu pika pikachu pi pikachu pikachu pi pikachu pika pika pikachu pi pikachu pi pi pikachu pikachu pika pikachu pi pika pi pi pika pika pikachu pikachu pi pi pikachu pi pikachu
pikachu pikachu pi pikachu
pikachu pika pika pikachu pika pikachu pikachu pika pika pikachu pikachu pi pi pikachu pika pikachu pika pika pi pika pikachu pikachu pi pika pika pikachu pi pika pi pika pi pikachu pi pikachu pika pika pi pi pika pi pika pika pikachu pikachu pika pikachu pikachu pika pi pikachu pika pi pikachu pi pika pika pi pikachu pika pi pika pikachu pi pi pikachu pika pika pi pika pi pikachu
pikachu pikachu pi pikachu
pikachu pika pi pika pika pikachu pika pikachu pi pikachu pi pi pika pi pikachu pika pi pi pika pikachu pi pikachu pi pi pikachu pikachu pika pikachu pikachu pika pi pikachu pi pika pikachu pi pikachu pika pika pikachu pika pi pi pikachu pikachu pika pika pikachu pi pika pikachu pikachu pi pika pikachu pikachu pika pi pi pikachu pikachu pi pikachu pi pikachu pi pikachu pi pika pikachu pi pikachu pika pikachu pi pika pi pikachu
pi pika
pikachu pikachu pi pikachu
pika pi
pikachu pikachu pi pikachu
pikachu pi pikachu pi pi pikachu pi pikachu pika pikachu pikachu pi pikachu pikachu pika pi pi pika pikachu pika pikachu pi pi pikachu pika pi pi pikachu pika pika pi pika pika pikachu pika pikachu pi pi pika pikachu pika pi pikachu pikachu pi pikachu pika pikachu pikachu pika pi pi pikachu pikachu pi pika pikachu pi pikachu pika pikachu pikachu pika pi pikachu pikachu pika pikachu pi pikachu pika pika pi pikachu pi pika pi pikachu pikachu pi pikachu
pi pika
pikachu pikachu pi pikachu
pikachu pikachu pi pika pikachu pi pika pika pi pi pika pi pikachu pi pika pi pika pi pika pikachu pika pi pi pikachu pi pikachu pi pika pi pika pika pikachu pi pikachu
pikachu pikachu pi pikachu
pikachu pi pikachu pika pikachu pi pika pi pikachu pikachu pika pika pi pi pikachu pi pika pi pikachu pi pika pikachu pi pika pi pi pikachu pikachu pika pika pikachu pikachu pi pi pikachu pi pikachu pi pikachu pi pi pikachu pikachu pi pikachu pi pikachu pi pika pika pikachu pikachu pika pi pika pikachu pi pikachu pi pi pika pikachu pika pi pikachu pi pika pi pi pikachu pikachu pika pika pikachu pika pika pikachu pi pika pi pika pikachu pi pika pikachu pika pi pika pikachu
pikachu pikachu pika pikachu
pikachu pikachu pika pikachu
pi pi pikachu pi pikachu pika pika pi pikachu pika pika pi pi pika pika pikachu pi pi pikachu pi pika pi pika pikachu pi pikachu pi pikachu pikachu pi pi pika pika pi pika pika pi pika pikachu pikachu pi pikachu pika pi pi pika pi pi pikachu pikachu pika pi pi pika pika pi pika pikachu pi pikachu pi pi pika pi pika pika pikachu pika pi pika pikachu pi pikachu pikachu pi pi pika pi pika pika pikachu pikachu pi pikachu
pikachu pikachu pi pikachu
pikachu pi pikachu pikachu pika pikachu pikachu pika pika pikachu pikachu pika pikachu pi pika pikachu pika pika pi pikachu pi pi pika pi pi pikachu pika pika pikachu pikachu pika pikachu pikachu pi pika pi pi pikachu pikachu pika pi pi pikachu pikachu pika pikachu pika pi pikachu pi pika pi pika pikachu pika pi pikachu pi pikachu pikachu pi pika pikachu pi pikachu pikachu pi pika pi pikachu pikachu pi pikachu pika pika pi pi pikachu
pikachu pi pi pika pi pi pikachu pika pikachu pikachu pika pika pi pi pika pikachu pi pikachu pi pi pika pi pika pi pi pika pikachu pi pika pi pikachu pika pikachu pika pi pi pika pi pi pikachu pi pikachu pikachu pika pi pikachu pi pi pika pi pikachu pi pi pika pi pi pikachu pika pikachu pika pikachu pika pi pikachu pikachu pi pi pika pika pikachu
pikachu pikachu pi pikachu
pikachu pikachu pika pikachu"""

t = {'pikachu': 'Ook?',
	'pika': 'Ook!',
	'pi': 'Ook.'}

message = message.strip().replace('pikachu', t['pikachu']).replace('pika', t['pika']).replace('pi', t['pi'])
print(message)


from collections import defaultdict
import sys
import re


__author__ = 'ipetrash'



def get_loops_block(source):
    begin_block = []
    blocks = {}
    i = 0
    words = re.findall("Ook[.?!] Ook[.?!]", source)
    l = len(words)  # Number of code symbols
    while i < l:
        s = words[i]
        if s == 'Ook! Ook?':
            begin_block.append(i)
        elif s == 'Ook? Ook!':
            b_i = begin_block.pop()  # b_i -- begin index
            blocks[i] = b_i
            blocks[b_i] = i
        i += 1
    return blocks


def execute(source):
   

    i = 0  # A pointer to the row index in the code
    x = 0  # Cell index
    ook = defaultdict(int)  # Dictionary, which is stored in the key index of the cell, and in the value - its value
    words = re.findall("Ook[.?!] Ook[.?!]", source)
    l = len(words)  # Number of code symbols
    loops_block = get_loops_block(source)

    while i < l:
        s = words[i]
        if s == 'Ook. Ook?':  # Go to the next cell
            x += 1
        elif s == 'Ook? Ook.':  # Go to the previous cell
            x -= 1
        elif s == 'Ook. Ook.':  # Increasing the value of the current cell on 1
            ook[x] += 1
        elif s == 'Ook! Ook!':  # Decrease the value of the current cell on 1
            ook[x] -= 1
        elif s == 'Ook! Ook.':  # Printing the value of the current cell
            print(chr(ook[x]), end='')
        elif s == 'Ook. Ook!':  # Enter a value in the current cell
            ook[x] = int(input("Input = "))
        elif s == 'Ook! Ook?':  # Begin loop
            if not ook[x]:  # If bf[x] == 0, then gets the index of the closing parenthesis
                i = loops_block[i]
        elif s == 'Ook? Ook!':  # End loop
            if ook[x]:  # Если bf[x] != 0, then gets the index of the opening parenthesis
                i = loops_block[i]
        i += 1

execute(message)