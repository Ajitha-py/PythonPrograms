import string
import re
existing_user={'ajitha':'aji@123','nani':'nani@123'}
#Registration
while True:
    user=input('enter user name:')
    if re.search('\s',user):
        print('user name should not contain space')
        continue
    elif re.search('^[0-9]',user):
        print('username should not start with digits')
        continue
    elif re.search('[@_!#$%^&*()<>?/|}{~:]',user):
        print('user should not start with special characters')
        continue
    if user in existing_user:
        print('{} is already existed,please enter new username'.format(user))
        continue
    else:
        while True:
            pwd=input('enter the password')
            if len(pwd)<8:
                print('length of the password should be  8 Character')
                continue
            elif len(pwd)>20:
                print('length of the password should be below 20 characters')
                continue
            elif not re.search('[A-Z]',pwd):
                print('please enter the at least one upper case character')
                continue
            elif not re.search('[a-z]',pwd):
                print('please enter the at least one lower case character')
                continue
            elif not re.search('[0-9]',pwd):
                print('please enter the atleast one digit')
                continue
            elif re.search('\s',pwd):
                print('please should not contain space')
                continue
            existing_user[user]=pwd
            print('account created successfully')
            break
        
    print(existing_user)
    break
        

#login
while True:
    user=input('enter user name:')
    if user in existing_user:
        while True:
            pwd=input('enter password:')
            if existing_user[user]==pwd:
                print('login success')
                break
            else:
                print('Invalid password,Please enter again')
                continue
    else:
        print('{} is invalid,please enter correct username'.format(user))
        continue
    break






















    
