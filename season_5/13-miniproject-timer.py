from time import sleep
from os import system, name
while True:
    choice = input("Do you want to start? (y/n): ")
    if "y" in choice.lower():
        hour = int(input("Enter Amount of hour: "))
        minutes = int(input("Enter Amount of minutes: "))
        seconds = int(input("Enter Amount of seconds: "))
        total = hour * 60 * 60 + minutes * 60 + seconds
        print('Timer starts now...')
        sleep(1)
        while total >= 1:
            print(total)
            total -= 1
            sleep(1)
            if name == 'nt':
                system("cls")
            else:
                system('clear')
        print('Timer ended')
    elif 'n' in choice.lower():
        print("Exiting...")
        break
    else:
        print("Invalid input...")
