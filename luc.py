from colorama import init
from termcolor import colored, cprint
init()

print(colored('BEM VINDO AO LUCIFER!', 'green','on_red'))

for i  in range(10):
	cprint(i,'magenta', end='')
