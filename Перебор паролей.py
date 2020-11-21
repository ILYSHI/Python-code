import simplecrypt

encrypted = open('encrypted.bin','rb').read()
passwords = open('passwords.txt', 'r').readlines()
print(passwords)
for i in passwords:
    print('Пробую пароль '+i)
    try:
        a=simplecrypt.decrypt(i,encrypted)
        a=a.decode('utf-8')
        break
    except simplecrypt.DecryptionException:
        print('Неверный пароль')
        continue