from datetime import datetime
data_users = []

#This function validates mobile number
def validate_mobile_number(mobile_number):
    is_valid = False
    
    while is_valid == False:
        try:
            if mobile_number.isnumeric() == False:
                raise TypeError('The entered value is not a number\n')
            
            elif len(mobile_number) != 10:
                raise ValueError('Enter a 10 digit number\n')
            
            elif mobile_number[0] != '0':
                raise NameError('The cell number must begin with 0\n')
            
            else:
                is_valid = True

        except TypeError as TE:
            print(TE)
            mobile_number = input('Please enter your mobile number: ')
        
        except ValueError as VE:
            print(VE)
            mobile_number = input('Please enter your mobile number: ')
        
        except NameError as NE:
            print(NE)
            mobile_number = input('Please enter your mobile number: ')
    
    return mobile_number

#This function validates if password contains an @ or $
def validate_special_character(password):
    if '@' in password or '&' in password:
        is_valid = True
    
    else:
        is_valid = False
    
    return is_valid

#This function validates if first character is an alphabetic one
def validate_alphabetic(password):
    if password[0].isalpha():
        is_valid = True
    
    else:
        is_valid = False
    
    return is_valid

#This function validates if last password character is numerical
def validate_last_character(password):
    if password[len(password) - 1].isnumeric():
        is_valid = True
    
    else:
        is_valid = False
    
    return is_valid

#This function validates passwords
def validate_password(password, confirm_password):
    is_valid = False
    
    while is_valid == False:
        try:
            s_character = validate_special_character(password)
            s_alphabetic = validate_alphabetic(password)
            s_numeric = validate_last_character(password)
            
            if password != confirm_password:
                raise NameError('Your passwords are not matching.\nPlease start again:\n')

            elif s_character == False:
                raise ValueError('The password must have a @ or an &.\nPlease start again\n')
            
            elif s_alphabetic == False:
                raise AttributeError('The first character of the password must be a letter.\nPlease start again\n')
            
            elif s_numeric == False:
                raise TypeError('The last element of the password must be a number\n')

            else:
                is_valid = True
        
        except NameError as NE:
            print(NE)
            password = input('Please enter your password: ')
            confirm_password = input('\nPlease confirm your password: ')

        except TypeError as TE:
            print(TE)
            password = input('Please enter your password: ')
            confirm_password = input('\nPlease confirm your password: ')
        
        except AttributeError as AE:
            print(AE)
            password = input('Please enter your password: ')
            confirm_password = input('\nPlease confirm your password: ')
        
        except ValueError as VE:
            print(VE)
            password = input('Please enter your password: ')
            confirm_password = input('\nPlease confirm your password: ')
    
    return password

#This function validates date of birth
def validate_date(date):
    is_valid = False

    while is_valid == False:
        try:
            datetime.strptime(date, '%d/%m/%Y')
            is_valid = True
        
        except ValueError:
            print('The date format is DD/MM/YYYY\n')
            date = input('Please Enter your Date of Birth # DD/MM/YYYY (No Space): ')
    
    return date

#This funtion validates sign in information
def validate_signin(username, password):
    no_user_found = True

    for user in data_users:
        
        if user["mobile_number"] == username:

            if user["password"] == password:
                print('You have Successfully Signed in.\nWelcome ' + user["name"] + '\n')
                return user

            else:
                print('You have entered the wrong Password.\nPlease try againg\n')
                return any
    
    if no_user_found:
        print('You have not Signed up with this Contact Number, Please Sign Up first\n')
        return any

#This function validates if old password match with the saved user password   
def validate_user_password(user):
    username = input('\nPlease enter your Username (Mobile number): ')
    old_password = input('\nPlease enter your old password: ')
    
    if user["password"] == old_password:
        return True
    
    else:
        print("You have entered the wrong Password.\nPlease try again\n")
        return False

#This function allow to reset password when maximum attemp is over
def validate_max_attemp_user(user):
    username = input('\nPlease enter your Username (Mobile number) to confirm: ')

    if user["mobile_number"] == username:
        date_of_birth = input('\nPlease Enter your Date of Birth # DD/MM/YYYY (No Space): ')

        if user["date_of_birth"] == date_of_birth:
            new_password = input('\nPlease enter your new password: ')
            confirm_new_password = input('\nPlease enter your new password: ')
            validate_password(new_password,confirm_new_password)

            if user["password"] != new_password:
                user["password"] = new_password
                return user
            
            else:
                print("You cannot use the password used earlier.\n")
                return any
        
        else:
            print("You cannot use the password used earlier.\n")
            return any
    else:
        return any

#This function allow to reset user password  
def reset_password(user):
    attemp = 0
    is_valid = False

    while is_valid == False:
        valid_user = validate_user_password(user)

        if attemp == 2:
            print("You have used the maximum attemps of login:\nPlease reset the password by entering the below details:\n")
            return validate_max_attemp_user(user)
            
        if valid_user:
            new_password = input('\nPlease enter your new password: ')
            
            if user["password"] != new_password:
                confirm_new_password = input('\nPlease enter your new password: ')
                validate_password(new_password,confirm_new_password)

                user["password"] = new_password
                is_valid = True

            else:
                print("You cannot use the password used earlier.\nPlease try again")
                attemp += 1

        else:
            attemp += 1
            
def signin_menu(user):
    select_signin = input('Please Enter 1 for Resetting the Password.\nPlease Enter 2 for Signout.\n')
    while select_signin != '2':
        
        if select_signin == '1':
            if reset_password(user) != any:
                select_signin = '0'
            else:
                return
        else:
            select_signin = input('Please Enter 1 for Resetting the Password.\nPlease Enter 2 for Signout.\n')

    return

def signup():
    name = input('\nPlease enter your full name: ')

    mobile_number = input('\nPlease enter your mobile number: ')
    validate_mobile_number(mobile_number)
    
    password = input('\nPlease enter your password: ')
    confirm_password = input('\nPlease confirm your password: ')
    validate_password(password, confirm_password)
    
    date_of_birth = input('\nPlease Enter your Date of Birth # DD/MM/YYYY (No Space): ')
    validate_date(date_of_birth)
    age = 2022 - int(date_of_birth[-4:])

    if age < 21:
        print('Only users over 21 years of age can register.\n')
        return

    data_users.append({
        "name": name,
        "mobile_number": mobile_number,
        "password": password,
        "date_of_birth": date_of_birth
    })

    print('You have Successfully Signed up.\n')
    
    return data_users

def signin():
    user_name = input('\nPlease enter your username (Mobile Number): ')
    password = input('\nPlease enter your password: ')
    valid_user = validate_signin(user_name, password)
    
    if valid_user != any:
        signin_menu(valid_user)
        return

def run():
    select = input('Please Enter 1 for Sign up.\nPlease Enter 2 for Sign in.\nPlease Enter 3 for Quit.\n')

    while select != '3':
        
        if select == '1':
            signup()
            select = '0'
        
        elif select == '2':
            signin()
            select = '0'
        
        else:
            select = input('Please Enter 1 for Sign up.\nPlease Enter 2 for Sign in.\nPlease Enter 3 for Quit.\n')
    
    print('Thank You for using the Application')
    

if __name__ == '__main__':
    run()