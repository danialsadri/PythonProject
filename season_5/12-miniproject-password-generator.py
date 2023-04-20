"""
پروژه پسورد ساز
"""
import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
symbols = "!@#$%^&*(){}|:?><"
numbers = "0123456789"
all = lower + upper + symbols + numbers

while True:
    print("choose an option:\n\t1)Create a password\n\t2)Exit")
    choice = input("Your choice: ")
    if choice == '1':
        length = int(input("Inter the length of password: "))
        password = "".join((random.sample(all, length)))
        print(password)

    elif choice == '2':
        break

    else:
        print('your choice is wrong\n')
