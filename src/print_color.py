import ctypes
import random
import string
import colorama
from colorama import Fore, Back, Style

kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

colorama.init()
rand = 0
color = ""

def buildblock(size):
    return ''.join(random.choice(string.ascii_letters) for _ in range(size))

for i in range(0,200):
    for k in range(0,500):
        rand = random.random()
        rand *= 10
        rand = round(rand)
        if rand == 1:
            print(Fore.RED + buildblock(1), sep='', end='')
        if rand == 2:
            print(Fore.GREEN + buildblock(1), sep='', end='')
        if rand == 3:
            print(Fore.YELLOW + buildblock(1), sep='', end='')
        if rand == 4:
            print(Fore.BLUE + buildblock(1), sep='', end='')
        if rand == 5:
            print(Fore.MAGENTA + buildblock(1), sep='', end='')
        if rand == 6:
            print(Fore.CYAN + buildblock(1), sep='', end='')
        if rand >= 7:
            print(Fore.WHITE + buildblock(1), sep='', end='')
