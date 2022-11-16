from datetime import datetime

data_users = []
food_list = []
drink_list = []
logged_user = any

##############################################
#
# Classes
#
##############################################
class Product:
    id : int
    name : str
    currency : str
    price : float

    def __init__ (self, id = 0, name = "", currency = "", price = 0.0):
        self.id = id
        self.name = name
        self.currency = currency
        self.price = price


##############################################
#
# Auxiliary functions
#
##############################################
""" Function that will print several spaces to simulate a screen wipe
    Parameters
        None
    Returns
        None
"""
def clean_screen ():
    for i in range (5):
        print ("")

def initialize_product_list():
    food_list.append(Product(1, "Noodles", "AUD", 2))
    food_list.append(Product(2, "Sandwich", "AUD", 4))
    food_list.append(Product(3, "Dumpling", "AUD", 6))
    food_list.append(Product(4, "Muffins", "AUD", 8))
    food_list.append(Product(5, "Pasta", "AUD", 10))
    food_list.append(Product(6, "Pizza", "AUD", 20))

    drink_list.append(Product(1, "Coffee", "AUD", 2))
    drink_list.append(Product(2, "Colddrink", "AUD", 4))
    drink_list.append(Product(3, "Shake", "AUD", 6))


##############################################
#
# Menu functions
#
##############################################
def main_menu():
    select = 0
    while select != '3':
        print ("")
        print ("***********************************************************************")
        print ("*                                                                     *")
        print ("*                          RESTAURANT APP                             *")
        print ("*                                                                     *")
        print ("***********************************************************************")
        print ("")
        print ("Please Enter 1 for Sign up")
        print ("Please Enter 2 for Sign in")
        print ("Please Enter 3 for Quit application")

        select = input('\n')

        if select == '1':
            signup()
            select = '0'
        
        elif select == '2':
            signin()
            select = '0'

        else:
            select = input('Please Enter a valid option.\n')

    logged_user = any


def signin_menu():
    select = 0
    while select != '2.3':
        clean_screen()
        print(logged_user)
        print ("***********************************************************************")
        print ("*")
        print ("* WELCOME " + logged_user[0])
        print ("*")
        print ("***********************************************************************")
        print ("")
        print ("* Please Enter 2.1 to Start Ordering")
        print ("* Please Enter 2.2 to Print Statistics")
        print ("* Please Enter 2.3 for Logout")

        select = input('\n')

        if select == '2.1':
            start_ordering_menu()
            select = '0'
        
        elif select == '2.2':
            statistics_menu()
            select = '0'

        else:
            select = input('Please Enter a valid option.\n')

def start_ordering_menu():
    select = 0
    while select != '3':
        clean_screen()
        print ("***********************************************************************")
        print ("* Please Enter 1 for Dine in")
        print ("* Please Enter 2 for Order Online")
        print ("* Please Enter 3 for Login Page")
        print ("***********************************************************************")

        select = input('\n')

        if select == '1':
            dine_in()
            select = '0'
        
        elif select == '2':
            statistics_menu()
            select = '0'

        else:
            select = input('Please Enter a valid option.\n')

def ordering_online_menu():
    select = 0
    while select != '3':
        clean_screen()
        print ("***********************************************************************")
        print ("* Please Enter 1 for Self Pickup")
        print ("* Please Enter 2 for Home Delivery")
        print ("* Please Enter 3 to go to previous Menu")
        print ("***********************************************************************")

        select = input('\n')

        if select == '1':
            self_pickup()
            select = '0'
        
        elif select == '2':
            home_delivery()
            select = '0'

        else:
            select = input('Please Enter a valid option.\n')

def food_menu(menu_option):
    select = 0
    while select != 7:
        clean_screen()
        for product in food_list:
            print("Enter " + str(product.id) + " for " + product.name + " \tPrice " + product.currency + " " + str(product.price))

        if menu_option == 2:
            print("Enter 7 for Drinks Menu:")
        else:
            print("Enter 7 for Checkout:")

        select = int(input('\n'))

        if select == 7 and menu_option == 2:
            drinks_menu()
            select = '0'

        if select == 7 and menu_option != 2:
            checkout()
            select = '0'
        
        elif select > 7 or select < 0:
            select = input('Please Enter a valid option.\n')

        else:
            add_product_to_order(select)

        
def drinks_menu():
    select = 0
    while select != 4:
        clean_screen()
        for product in drink_list:
            print("Enter " + str(product.id) + " for " + product.name + " \tPrice " + product.currency + " " + str(product.price))

        print("Enter 4 for Checkout:")

        select = int(input('\n'))

        if select > 7 or select < 0:
            select = input('Please Enter a valid option.\n')

        else:
            add_product_to_order(select)

    checkout()

def statistics_menu():
    select = 0
    while select != 4:
        clean_screen()
        print ("***********************************************************************")
        print ("* Please Enter the Option to print the Statistcs")
        print ("* 1 - All Dine in Orders")
        print ("* 2 - All Pick up Orders")
        print ("* 3 - All Deliveries")
        print ("* 4 - All Orders (Ascending Order)")
        print ("* 5 - Total Amount Spent on All Orders")
        print ("* 6 - To go to Previuos Menu")
        print ("***********************************************************************")

        select = input('\n')

        if select == '1':
            self_pickup()
            select = '0'
        
        elif select == '2':
            home_delivery()
            select = '0'

        else:
            select = input('Please Enter a valid option.\n')

##############################################
#
# Core functions
#
##############################################

def signin():
    global logged_user

    attemp = 0
    is_valid = False

    while is_valid == False:
        if attemp == 3:
            print("You have used the maximum attemps of login.\nPlease reset the password by entering the below details:")
            return signin_max_attemp_user()
        
        valid_user = validate_signin()
    
        if valid_user == False:
            return

        elif valid_user != any:
            logged_user = valid_user
            print(logged_user)
            signin_menu()
            attemp = 0
            is_valid = True
        
        else:
            attemp += 1

def signup():
    is_valid = False
    name = input('\nPlease enter your full name: ')

    while is_valid == False:
        mobile_number = input('Please enter your mobile number: ')
        response = validate_mobile_number(mobile_number)
        
        if response != False:
            break
    
    while is_valid == False:
        password = input('Please enter your password: ')
        confirm_password = input('Please confirm your password: ')
        response = validate_password(password, confirm_password)
        
        if response != False:
            break
    
    date_of_birth = input('Please Enter your Date of Birth # DD/MM/YYYY (No Space): ')
    validate_date(date_of_birth)
    age = 2022 - int(date_of_birth[-4:])

    if age < 21:
        print('Only users over 21 years of age can register.\n')
        return

    data_users.append([
        name,
        mobile_number,
        password,
        date_of_birth
    ])

    print('You have Successfully Signed up.\n')
    
    return data_users

def dine_in():
    print("Dine in options")

def order_online():
    print("Dine in options")

def self_pickup():
    print("Self Pickup options")

def home_delivery():
    print("Home Delivery options")

def add_product_to_order(product_id):
    print("Add product by id process" + str(product_id))

def checkout():
    print("Checkout process")

def all_dine_orders():
    print("All Dine in Orders")

def all_pickup_orders():
    print("All Pick up Orders")

def all_deliveries():
    print("All Deliveries")

def all_orders():
    print("All Orders (Ascending Order)")

def all_total_amount_orders():
    print("Total Amount Spent on All Orders")


##############################################
#
# Validate functions
#
##############################################

#This function validates mobile number
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

#This function search a user by username
def find_user_by_username(username):
    user_found = False
    for user in data_users:
        
        if user[1] == username:
            user_found = True
            return user
    
    if user_found == False:
        print('You have not Signed up with this Contact Number, Please Sign Up first\n')
        return any

#This function validates if old password match with the saved user password   
def validate_user_password():
    username = input('\nPlease enter your Username (Mobile number): ')
    user = find_user_by_username(username)

    if user != any:
        old_password = input('\nPlease enter your old password: ')
        
        if user[2] == old_password:
            return True
        
        else:
            print("You have entered the wrong Password.\nPlease try again\n")
            return False
    
    return False

#This function allow to reset user password from signin option 1  
def reset_password(user):
    is_a_valid_user = validate_user_password()
            
    if is_a_valid_user:
        is_a_valid_password = False

        while is_a_valid_password == False:
            new_password = input('\nPlease enter your new password: ')
            confirm_new_password = input('\nPlease confirm your new password: ')
            response = validate_password(new_password,confirm_new_password)

            if response != False:
        
                if user[2] != new_password:
                    user[2] = new_password
                    print("Your password has been reset succesfully.")
                    return user
                    
                else:
                    print("You cannot use the password used earlier.\n")
                    return any

    return any

#This function allow to reset password when maximum attemp is over
def signin_max_attemp_user():
    username = input('Please enter your Username (Mobile number) to confirm: ')
    user = find_user_by_username(username)

    if user != any:
        date_of_birth = input('Please Enter your Date of Birth # DD/MM/YYYY (No Space): ')
        print(user[3])

        if user[3] == date_of_birth:
            is_a_valid_password = False

            while is_a_valid_password == False:
                new_password = input('Please enter your new password: ')
                confirm_new_password = input('Please confirm your new password: ')
                response = validate_password(new_password,confirm_new_password)

                if response != False:
                    if user[2] != new_password:
                        user[2] = new_password
                        print("Your password has been reset succesfully.")
                        return user
                    
                    else:
                        print("You cannot use the password used earlier.\n")
                        return any
        
        else:
            print("You type a wrong date of birth.\n")
            return any
    else:
        return any

#This funtion validates sign in information
def validate_signin():
    username = input('\nPlease enter your username (Mobile Number): ')
    password = input('Please enter your password: ')
    user = find_user_by_username(username)

    if user != any:
        if user[1] == username:

            if user[2] == password:
                print('You have Successfully Signed in.\nWelcome ' + user[0] + '\n')
                return user

            else:
                print('You have entered the wrong Password.\nPlease try againg\n')
                return any
    else:
        return False





def run():
    initialize_product_list()
    main_menu()
    
    

if __name__ == '__main__':
    run()