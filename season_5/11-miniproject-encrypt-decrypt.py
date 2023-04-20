"""
پروژه رمز نگاری و رمز گشایی شده
"""
while True:
    print('Choice Your Option:\n\t1)Encrypt\n\t2)Decrypt\n\t3)Exit')
    choice = input('Your Choice: ')
    if choice == '1':
        plain_text = input('text: ')
        encrypted_text = ""
        for c in plain_text:
            x = ord(c) * 2 + 5
            encrypted_text += chr(x)
        print(f"encrypted text: {encrypted_text}")
        print("*" * 40 + "\n")
    elif choice == '2':
        encrypted_text = input('encrypted_text: ')
        plain_text = ""
        for c in encrypted_text:
            x = (ord(c) - 5) // 2
            plain_text += chr(x)
        print(f"plain text: {plain_text}")
        print("*" * 40 + "\n")
    elif choice == '3':
        print('GoodBye!')
        break
    else:
        print('Your choice is wrong!')
        print("*" * 40 + "\n")
