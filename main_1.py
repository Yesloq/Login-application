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
class Product():
    id : int
    name : str
    currency : str
    price : float

    def __init__ (self, id = 0, name = "", currency = "", price = 0.0):
        self.id = id
        self.name = name
        self.currency = currency
        self.price = price

class Customer():
    name : str
    address : str
    mobile : str
    password : str
    dob : str
    orders : list

    def __init__(self, name = "", address = "", mobile = "", password = "", dob = ""):
        self.name = name
        self.address = address
        self.mobile = mobile
        self.password = password
        self.dob = dob
        self.orders = []

class Order():
    id : str
    order_type : str
    date : str
    customer : Customer()
    product_list : list
    sub_total_amount : float
    service_amount : float
    delivery_amount : float
    total_amount : float

    def __init__(self, date = "", customer = any):
        self.id = ""
        self.order_type = ""
        self.date = date
        self.customer = customer
        self.product_list = []
        self.sub_total_amount = 0.0
        self.service_amount = 0.0
        self.delivery_amount = 0.0
        self.total_amount = 0.0
    
    def add_product(self, product):
        pass

    def calculate_sub_total_amount(self):
        pass

    def calculate_total_amount(self):
        pass

    def calculate_service_amount(self):
        pass

    def calculate_delivery_amount(self):
        pass

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
    global logged_user
    logged_user = any

    print ("***********************************************************************")
    print ("*                                                                     *")
    print ("*                          RESTAURANT APP                             *")
    print ("*                                                                     *")
    print ("***********************************************************************")
    print ("Please Enter 1 for Sign up")
    print ("Please Enter 2 for Sign in")
    print ("Please Enter 3 for Quit application")

    select = input()

    if select == '1':
        signup()
    
    elif select == '2':
        signin()

    elif select == '3':
        print('Thank You for using the Application')
        return

    else:
        print('Please Enter a valid option\n')
        main_menu()

def signin_menu():
    global logged_user
    
    clean_screen()
    print ("***********************************************************************")
    print ("*")
    print ("* WELCOME " + logged_user.name)
    print ("*")
    print ("***********************************************************************")
    print ("* Please Enter 2.1 to Start Ordering")
    print ("* Please Enter 2.2 to Print Statistics")
    print ("* Please Enter 2.3 for Logout")

    select = input()

    if select == '2.1':
        start_ordering_menu()
    
    elif select == '2.2':
        statistics_menu()

    elif select == '2.3':
        print("Logout Successfully")
        logged_user = any
        main_menu()

    else:
        print('Please Enter a valid option.\n')
        signin_menu()

def start_ordering_menu():
    clean_screen()
    print ("***********************************************************************")
    print ("*                     START ORDENING MENU                             *")
    print ("***********************************************************************")
    print ("* Please Enter 1 for Dine in")
    print ("* Please Enter 2 for Order Online")
    print ("* Please Enter 3 for Login Page")

    select = input()

    if select == '1':
        dine_in()
    
    elif select == '2':
        ordering_online_menu()

    elif select == '3':
        signin_menu()

    else:
        print('Please Enter a valid option.\n')
        start_ordering_menu()

def ordering_online_menu():
    clean_screen()
    print ("***********************************************************************")
    print ("*                      ORDENING ONLINE MENU                           *")
    print ("***********************************************************************")
    print ("* Please Enter 1 for Self Pickup")
    print ("* Please Enter 2 for Home Delivery")
    print ("* Please Enter 3 to go to previous Menu")

    select = input('\n')

    if select == '1':
        self_pickup()
    
    elif select == '2':
        home_delivery()

    elif select == '3':
        start_ordering_menu()

    else:
        print('Please Enter a valid option.\n')
        ordering_online_menu()

def food_menu(order_type):
    clean_screen()
    print ("***********************************************************************")
    print ("*                            FOOD MENU                                *")
    print ("***********************************************************************")

    for product in food_list:
        print("Enter " + str(product.id) + " for " + product.name + " \tPrice " + product.currency + " " + str(product.price))

    if order_type == '2':
        print("Enter 7 for Drinks Menu:")
    else:
        print("Enter 7 for Checkout:")

    select = int(input('\n'))

    if select == 7 and order_type == 2:
        drinks_menu()

    if select == 7 and order_type != 2:
        checkout()
    
    elif select > 7 or select < 0:
        print('Please Enter a valid option.\n')
        food_menu(order_type)

    else:
        add_product_to_order(select)
        food_menu()

        
def drinks_menu():
    clean_screen()
    print ("***********************************************************************")
    print ("*                          DRINKS MENU                                *")
    print ("***********************************************************************")
    for product in drink_list:
        print("Enter " + str(product.id) + " for " + product.name + " \tPrice " + product.currency + " " + str(product.price))

    print("Enter 4 for Checkout:")

    select = int(input('\n'))

    if select > 4 or select < 0:
        select = input('Please Enter a valid option.\n')

    elif select == 4:
        checkout()

    else:
        add_product_to_order(select)
        drinks_menu()

def statistics_menu():
    clean_screen()
    print ("***********************************************************************")
    print ("*                   PRINT STATISTICS MENU                             *")
    print ("***********************************************************************")
    print ("* Please Enter the Option to print the Statistcs")
    print ("* 1 - All Dine in Orders")
    print ("* 2 - All Pick up Orders")
    print ("* 3 - All Deliveries")
    print ("* 4 - All Orders (Ascending Order)")
    print ("* 5 - Total Amount Spent on All Orders")
    print ("* 6 - To go to Previuos Menu")

    select = input('\n')

    if select == '1':
        all_dine_orders()
    
    elif select == '2':
        all_pickup_orders()

    elif select == '3':
        all_deliveries()

    elif select == '4':
        all_orders()

    elif select == '5':
        all_total_amount_orders()

    elif select == '6':
        signin_menu()

    else:
        print('Please Enter a valid option.\n')
        statistics_menu()

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
            signin_menu()
            attemp = 0
            is_valid = True
        
        else:
            attemp += 1

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
    
    data_users.append(temp_customer)

    print('You have Successfully Signed up.\n')
    

def dine_in():
    print("Dine in options")
    start_ordering_menu()

def order_online():
    print("Dine in options")
    start_ordering_menu()

def self_pickup():
    print("Self Pickup options")
    ordering_online_menu()

def home_delivery():
    print("Home Delivery options")
    ordering_online_menu()

def add_product_to_order(product_id):
    print("Add product by id process" + str(product_id))

def checkout():
    print("Checkout process")

def all_dine_orders():
    print("All Dine in Orders")
    statistics_menu()

def all_pickup_orders():
    print("All Pick up Orders")
    statistics_menu()

def all_deliveries():
    print("All Deliveries")
    statistics_menu()

def all_orders():
    print("All Orders (Ascending Order)")
    statistics_menu()

def all_total_amount_orders():
    print("Total Amount Spent on All Orders")
    statistics_menu()


##############################################
#
# Validate functions
#
##############################################

# This function validates the address
def validate_address(address):
    if address == '':
        return False
    else:
        return True

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
        
        if user.mobile == username:
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
        if user.mobile == username:

            if user.password == password:
                print('You have Successfully Signed in.\nWelcome ', user.name, '\n')
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