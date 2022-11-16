from datetime import datetime

# List of user data
data_users = []

class Customer():

    # Constructor for each instance of the class Customer
    def __init__(self):
        self.name = ""
        self.address = ""
        self.mobile = ""
        self.password = ""
        self.dob = ""
        self.orders = []




# This function validates the address
def validate_address(address):
    if address == '':
        return False
    else:
        return True

# This function validates mobile number
def validate_mobile_number(mobile_number):
    
    if mobile_number.isnumeric() == False:
        print('The entered value is not a number\n')
                    
    elif len(mobile_number) != 10:
        print('Enter a 10 digit number\n')
    
    elif mobile_number[0] != '0':
        print('The cell number must begin with 0\n')
    else:    
        return mobile_number
    
    return False

# This function validates if password contains an @ or $
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

# This function validates passwords
def validate_password(password, confirm_password):
    s_character = validate_special_character(password)
    s_alphabetic = validate_alphabetic(password)
    s_numeric = validate_last_character(password)
    
    if password != confirm_password:
        print('Your passwords are not matching.\nPlease start again:\n')

    elif s_character == False:
        print('The password must have a @ or an &.\nPlease start again\n')
    
    elif s_alphabetic == False:
        print('The first character of the password must be a letter.\nPlease start again\n')
    
    elif s_numeric == False:
        print('The last element of the password must be a number\n')

    else:
        return password
    
    return False

# This function validates if last password character is numerical
def validate_last_character(password):
    if password[len(password) - 1].isnumeric():
        is_valid = True
    
    else:
        is_valid = False
    
    return is_valid

# This function validates date of birth
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

# Sign up function
def signup():
    is_valid = False
    temp_customer = Customer()
    temp_customer.name = input('\nPlease enter your full name: ')
    temp_customer.address = input('\nPlease enter your address or press enter to Skip: ')

    while is_valid == False:
        mobile_number = input('\nPlease enter your mobile number: ')
        response = validate_mobile_number(mobile_number)
        
        if response != False:
            temp_customer.mobile = mobile_number
            break
    
    while is_valid == False:
        password = input('\nPlease enter your password: ')
        confirm_password = input('\nPlease confirm your password: ')
        response = validate_password(password, confirm_password)
        
        if response != False:
            temp_customer.password = password
            break
    
    date_of_birth = input('\nPlease Enter your Date of Birth # DD/MM/YYYY (No Space): ')
    validate_date(date_of_birth)
    age = 2022 - int(date_of_birth[-4:])

    if age < 21:
        print('Only users over 21 years of age can register.\n')
        return
    
    print('\nHas been successfully registered. \n')
    data_users.append(temp_customer)

# Sign in function
def signin():
    address = data_users[0].address
    validate = False

    while validate == False:

        if validate_address(address) == False:
            address = input('\nPlease enter your address: ')
            data_users[0].address = address
        else:
            validate = True
    
    print(address)


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