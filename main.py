from datetime import datetime

def val_mnumber():
    mnumber = input('\nPlease enter your mobile number: ')
    val = False
    while val == False:
        try:
            if mnumber.isnumeric() == False:
                raise TypeError('The entered value is not a number')
                
            
            elif len(mnumber) != 10:
                raise ValueError('Enter a 10 digit number')
                
            
            elif mnumber[0] != '0':
                raise NameError('The cell number must begin with 0')
                
            
            else:
                #print('The mobile number is correct.')
                val = True

        except TypeError as TE:
            print(TE)
            mnumber = input('\nPlease enter your mobile number: ')
        
        except ValueError as VE:
            print(VE)
            mnumber = input('\nPlease enter your mobile number: ')
        
        except NameError as NE:
            print(NE)
            mnumber = input('\nPlease enter your mobile number: ')
    
    return mnumber

def val_character(password):
    if '@' in password or '&' in password:
        val = True
    else:
        val = False
    
    return val

def val_alphabetic(password):
    if password[0].isalpha():
        val = True
    else:
        val = False
    
    return val

def val_password():
    password = input('\nPlease enter your password: ')
    confirm_password = input('\nPlease confirm your password: ')
    val = False
    
    while val == False:
        try:
            s_character = val_character(password)
            s_alphabetic = val_alphabetic(password)
            s_numeric = password[len(password) - 1].isnumeric()
            
            if s_character == False:
                raise ValueError('The password must have a @ or an &.\nPlease start again')
            
            elif s_alphabetic == False:
                raise AttributeError('The first character of the password must be a letter.\nPlease start again')
            
            elif s_numeric == False:
                raise TypeError('The last element of the password must be a number')

            elif password != confirm_password:
                raise NameError('Your passwords are not matching.\nPlease start again:\n')
            
            else:
                #print('\nYour password is correct.')
                val = True
        
        except TypeError as TE:
            print(TE)
            password = input('\nPlease enter your password: ')
            confirm_password = input('\nPlease confirm your password: ')
        
        except AttributeError as AE:
            print(AE)
            password = input('\nPlease enter your password: ')
            confirm_password = input('\nPlease confirm your password: ')

        except NameError as NE:
            print(NE)
            password = input('\nPlease enter your password: ')
            confirm_password = input('\nPlease confirm your password: ')
        
        except ValueError as VE:
            print(VE)
            password = input('\nPlease enter your password: ')
            confirm_password = input('\nPlease confirm your password: ')
    
    return password

def val_date():
    date = input('\nPlease Enter your Date of Birth # DD/MM/YYYY (No Space): ')
    val = False

    while val == False:
        try:
            datetime.strptime(date, '%d/%m/%Y')
            val = True
        except ValueError:
            print('The date format is DD/MM/YYYY')
            date = input('\nPlease Enter your Date of Birth # DD/MM/YYYY (No Space): ')
    
    print()
    #print('The date is correct')
    return date

data_users = []

def signup(user):
    name = input('\nPlease enter your full name: ')
    mobile_number = val_mnumber()
    password = val_password()
    dob = val_date()

    data_users.insert(user, {
        "name": name,
        "mobile_number": mobile_number,
        "password": password,
        "dob": dob
    })

    print('\nYou have Successfully Signed up.')
    
    return data_users

def signin():
    print('Sign in!')

def run():
    user = 0 #Esta variable permite saber la posicion dentro de la lista del usuario registrado
    select = input('Please Enter 1 for Sign up.\nPlease Enter 2 for Sign in.\nPlease Enter 3 for Quit.\n')

    while select != '3':
        
        if select == '1':
            print(signup(user))
            user += 1
            select = '0'
        
        elif select == '2':
            signin()
            select = '0'
        
        else:
            select = input('Please Enter 1 for Sign up.\nPlease Enter 2 for Sign in.\nPlease Enter 3 for Quit.\n')
    
    print('Thank You for using the Application')
    


if __name__ == '__main__':
    run()