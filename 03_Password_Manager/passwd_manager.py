def add_passwd(name, passwd):
    with open('passwd.txt', 'a') as f:
        f.write(f"{name}|{passwd}\n")

def view_passwd():
    with open('passwd.txt','r') as f:
        for line in f:
            data=line.rstrip()
            user,passw = data.split('|')
            print(f'Site:{user} -> password: {passw}')


while True:
    try:
        op=int(input('What do you want:\n'
                 '1-Add New Password\n'
                 '2-View Password\n'
                 '3-Exit\n'
                  'Choice: '))
        if op==1:
            n=input('enter the name: ')
            p=input('enter the password of this app: ')
            add_passwd(n,p)
            print('Password added successfully')

        elif op==2:
            print('\n---Your Passwords---')
            view_passwd()
            print('----------------')

        elif op==3:
            print('Good bye!')
            break

        else:
            print('You can choose 1 , 2 or 3 only ')

    except ValueError:
        print('enter a valid number')
