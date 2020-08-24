import sys
import time
import os

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.08)

print("-- Developed By PROJECT --")
print_slow("Вообщем, тебя ждёт взлом жопы!")
print()
print_slow("Инструкция: нахуй инструкцию")
print()
print_slow("Ты готов наебашить? (y/n)")
print()

while 1:
    answere = input()
    if answere == "y":
        os.startfile('ddos.bat')
        break
    else:
        print_slow("Эу, Пёс! Я тут хуярил, гонял этого питона, а ты?")
        print()
        print_slow("Ещё одна попытка(y/n)")
