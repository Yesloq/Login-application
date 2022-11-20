from datetime import datetime


##############################################
#
# Global variables 
#
##############################################
#This list will store all registered customers
data_users = []

#This list will store all food type products
food_list = []

#This list will store all drink type products
drink_list = []

#This variable will store the successfully sign in user
logged_user = any

#This variable will store the customer order in proccess
customer_order = any

#This variable will store the general count of the orders created
order_counter = 0;


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
    mobile_number : str
    password : str
    dob : str
    orders : list

    def __init__(self, name = "", address = "", mobile_number = "", password = "", dob = ""):
        self.name = name
        self.address = address
        self.mobile_number = mobile_number
        self.password = password
        self.dob = dob
        self.orders = []

class Order():
    id : str
    order_type : str
    date : str
    time : str
    ordered_products : list
    sub_total_amount : float
    total_amount : float

    def __init__(self):
        self.id = id
        self.order_type = ""
        self.date = ""
        self.time = ""
        self.ordered_products = []
        self.sub_total_amount = 0.0
        self.total_amount = 0.0
    
    def add_ordered_product(self, product):
        print(self.order_type)
        print("llegue")
        self.ordered_products.append(product)

    def calculate_sub_total_amount(self):
        for product in self.ordered_products:
            self.sub_total_amount += product.price

class DineInOrder(Order):
    number_persons : int
    service_amount : float

    def __init__(self):
        super().__init__()
        self.number_persons = 0
        self.service_amount = 0.0

    def calculate_total_amount(self):
        self.calculate_sub_total_amount()
        self.calculate_service_amount()
        self.total_amount = self.sub_total_amount + self.service_amount

    def calculate_service_amount(self):
        if self.order_type == 'dine_in':
            self.service_amount = self.sub_total_amount * 0.15

class SelfPickupOrder(Order):
    name_pickup : str

    def __init__(self):
        super().__init__()
        self.name_pickup = ""

    def calculate_total_amount(self):
        self.calculate_sub_total_amount()
        self.total_amount = self.sub_total_amount 

class HomeDeliveryOrder(Order):
    distance : float
    delivery_amount : float

    def __init__(self):
        super().__init__()
        self.distance = 0.0
        self.delivery_amount = 0.0

    def calculate_total_amount(self):
        self.calculate_sub_total_amount()
        self.total_amount = self.sub_total_amount + self.delivery_amount


##############################################
#
# Auxiliary functions
#
##############################################
#This function will print several spaces to simulate a screen wipe
def clean_screen ():
    for i in range (5):
        print ("")

#This function validates dates
def validate_date(date):
    is_valid = False

    while is_valid == False:
        try:
            datetime.strptime(date, '%d/%m/%Y')
            is_valid = True
        
        except ValueError:
            print('The date format is DD/MM/YYYY\n')
            date = input('Please Enter your Date following the format # DD/MM/YYYY (No Space): ')
    
    return date

#This function validate hours
def validate_hour(hour):
    is_valid = False

    while is_valid == False:
        try:
            datetime.strptime(hour, '%H:%M')
            is_valid = True
        
        except ValueError:
            print('The hour format is HH:MM\n')
            hour = input('Please enter your hour time following the format # HH:MM (No Space): ')
    
    return hour

#This function initialize food and drink product list (catalog)
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
# Task 1. Signup/Sign in Process for Customers 
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
        raise SystemExit

    else:
        print('Please Enter a valid option\n')
        clean_screen()
        main_menu()

#********************************************************************************
#This function is in charge of the sign up proccess 
def signup():
    is_valid = False
    customer = Customer()
    customer.name = input('\nPlease enter your full name: ')
    customer.address = input('Please enter your address or press enter to Skip: ')

    while is_valid == False:
        mobile_number = input('Please enter your mobile number: ')
        response = validate_mobile_number(mobile_number)
        
        if response != False:
            customer.mobile_number = mobile_number
            break
    
    while is_valid == False:
        password = input('Please enter your password: ')
        confirm_password = input('Please confirm your password: ')
        response = validate_password(password, confirm_password)
        
        if response != False:
            customer.password = password
            break
    
    date_of_birth = input('Please Enter your Date of Birth # DD/MM/YYYY (No Space): ')
    customer.dob = validate_date(date_of_birth)
    age = 2022 - int(date_of_birth[-4:])

    if age < 21:
        print('Only users over 21 years of age can register.')
        customer = any
        clean_screen()
        main_menu()
    
    data_users.append(customer)

    print('You have Successfully Signed up.')
    clean_screen()
    main_menu()

#This function validates mobile number
def validate_mobile_number(mobile_number):
    
    if mobile_number.isnumeric() == False:
        print('The entered value is not a number\n')
                    
    elif len(mobile_number) != 10:
        print('Enter a 10 digit number\n')
    
    elif mobile_number[0] != '0':
        print('The cell number must begin with 0\n')

    elif validate_user_exists(mobile_number) == False:
        print('There is already a registered user with this mobile number\n')
    else:    
        return mobile_number
    
    return False

#This function validates if exists an user registered with the mobile number
def validate_user_exists(username):
    for user in data_users:
        if user.mobile_number == username:
            return False
    return True

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
        print('The last element of the password must be a number.\nPlease start again\n')

    else:
        return password
    
    return False

#This function validates if password contains an @ or $
def validate_special_character(password):
    if '@' in password or '&' in password:
        is_valid = True
    
    else:
        is_valid = False
    
    return is_valid

#This function validates if first password character is an alphabetic one
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

# This function validates the address
def validate_address(address):
    if address == '':
        return False
    else:
        return True

#********************************************************************************
#This function is in charge of the registration process, it also validates the number of attempts
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
            clean_screen()
            main_menu()

        elif valid_user != any:
            logged_user = valid_user
            signin_menu()
            attemp = 0
            is_valid = True
        
        else:
            attemp += 1

#This function allow to reset password when maximum attemp is over
def signin_max_attemp_user():
    username = input('Please enter your Username (Mobile number) to confirm: ')
    user = find_user_by_username(username)

    if user != any:
        date_of_birth = input('Please Enter your Date of Birth # DD/MM/YYYY (No Space): ')

        if user.dob == date_of_birth:
            is_a_valid_password = False

            while is_a_valid_password == False:
                new_password = input('Please enter your new password: ')
                confirm_new_password = input('Please confirm your new password: ')
                response = validate_password(new_password,confirm_new_password)

                if response != False:
                    if user.password != new_password:
                        user.password = new_password
                        print("Your password has been reset succesfully.")
                        break
                    
                    else:
                        print("You cannot use the password used earlier.")
                        break
        
        else:
            print("You type a wrong date of birth.")
            
    clean_screen()
    main_menu()

#This funtion validates sign in information
def validate_signin():
    username = input('\nPlease enter your username (Mobile Number): ')
    password = input('Please enter your password: ')
    user = find_user_by_username(username)

    if user != any:
        if user.mobile_number == username:

            if user.password == password:
                return user

            else:
                print('You have entered the wrong Password.\nPlease try againg\n')
                return any
    else:
        return False

#This function search an user by username
def find_user_by_username(username):
    user_found = False
    for user in data_users:
        
        if user.mobile_number == username:
            user_found = True
            return user
    
    if user_found == False:
        print('You have not Signed up with this Contact Number, Please Sign Up first')
        return any

#This function allow to reset logged user password when user choose 'Reset password' from menu options
def reset_password():
    global logged_user
            
    if validate_logged_user_password():
        is_valid_new_password = False

        while is_valid_new_password == False:
            new_password = input('Please enter your new password: ')
            confirm_new_password = input('Please confirm your new password: ')
            response = validate_password(new_password, confirm_new_password)

            if response != False:
                if logged_user.password != new_password:
                    logged_user.password = new_password
                    print("Your password has been reset succesfully.")
                    break
                    
                else:
                    print("You cannot use the password used earlier.")
                    break

    clean_screen()
    main_menu()

#This function validates if old password match with the logged user password   
def validate_logged_user_password():
    global logged_user

    username = input('Please enter your Username (Mobile number): ')

    if logged_user.mobile_number == username:
        old_password = input('Please enter your old password: ')
        
        if logged_user.password == old_password:
            return True
        
        else:
            print("You have entered the wrong Password.\nPlease try again\n")
            return False
    else:
        print("You have entered the wrong username (mobile number)")

    return False


##############################################
#
# Task 2: Ordering
#
##############################################
#This function is in charge to print the main menu when user sign in successfully
def signin_menu():
    global logged_user
    
    clean_screen()
    print ("***********************************************************************")
    print ("*")
    print ("* WELCOME ", logged_user.name)
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
        clean_screen()
        main_menu()

    else:
        print('Please Enter a valid option.\n')
        signin_menu()

#This function is in charge to print Start ordering menu
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

#This function is in charge to print ordering online menu. It also validates if logger user address is not empty to delivery option
def ordering_online_menu():
    global logged_user

    clean_screen()
    print ("***********************************************************************")
    print ("*                      ORDENING ONLINE MENU                           *")
    print ("***********************************************************************")
    print ("* Please Enter 1 for Self Pickup")
    print ("* Please Enter 2 for Home Delivery")
    print ("* Please Enter 3 to go to previous Menu")

    select = input()

    if select == '1':
        self_pickup()
    
    elif select == '2':
        if logged_user.address == "":
            print('\nYou have not mentioned your address, while signing up.\nPlease Enter Y if you would like to enter your address.\nEnter N if you would like other mode of order.')
            select = input()

            if select == 'Y':
                logged_user.address = input('Please enter your address: ')

            elif select == 'N':
                signin_menu()

            else:
                print('Please Enter a valid option.\n')
                ordering_online_menu()

        home_delivery()

    elif select == '3':
        start_ordering_menu()

    else:
        print('Please Enter a valid option.\n')
        ordering_online_menu()

#This function is in charge to set customer order information whit 'dine_in' order type
def dine_in():
    global customer_order
    customer_order = DineInOrder()
    customer_order.order_type = "dine_in"
    food_menu()

#This function is in charge to set customer order information whit 'self_pickup' order type
def self_pickup():
    global customer_order
    customer_order = SelfPickupOrder()
    customer_order.order_type = "self_pickup"
    food_menu()

#This function is in charge to set customer order information whit 'delivery' order type
def home_delivery():
    global customer_order
    customer_order = HomeDeliveryOrder()
    customer_order.order_type = "delivery"
    food_menu()

#********************************************************************************
#This function is in charge to print food catalog menu
def food_menu():
    global customer_order
    
    clean_screen()
    print ("***********************************************************************")
    print ("*                            FOOD MENU                                *")
    print ("***********************************************************************")

    for product in food_list:
        print("Enter " + str(product.id) + " for " + product.name + " \tPrice " + product.currency + " " + str(product.price))

    if customer_order.order_type == 'dine_in':
        print("Enter 7 for Drinks Menu:")
    else:
        print("Enter 7 for Checkout:")

    select = int(input())

    if select == 7 and customer_order.order_type == 'dine_in':
        drinks_menu()

    elif select == 7 and customer_order.order_type != 'dine_in':
        checkout()
    
    elif select > 7 or select < 0:
        print('Please Enter a valid option.\n')
        food_menu()

    else:
        add_product_to_order(select, 'food_list')
        food_menu()

#This function is in charge to print drink catalog menu   
def drinks_menu():
    global customer_order

    clean_screen()
    print ("***********************************************************************")
    print ("*                          DRINKS MENU                                *")
    print ("***********************************************************************")
    for product in drink_list:
        print("Enter " + str(product.id) + " for " + product.name + " \tPrice " + product.currency + " " + str(product.price))

    print("Enter 4 for Checkout:")

    select = int(input())

    if select > 4 or select < 0:
        select = input('Please Enter a valid option.\n')
        drinks_menu()

    elif select == 4:
        checkout()

    else:
        add_product_to_order(select, 'drink_list')
        drinks_menu()

#This function is in charge to add a product to the customer order in proccess
def add_product_to_order(product_id, product_type):
    global customer_order
    
    if product_type == 'food_list':
        for product in food_list:

            if product.id == product_id:

                customer_order.add_ordered_product(product)
    
    else:
        for product in drink_list:

            if product.id == product_id:

                customer_order.add_ordered_product(product)

#This function is in charge to complete the customer order proccess
def checkout():
    global customer_order
    global logged_user

    select = input('\nPlease Enter Y to proceed to Checkout or Enter N to cancel the order: ')

    if select == 'Y':

        customer_order.calculate_total_amount()

        if customer_order.order_type == 'dine_in':
            print('Your total payble amount is: ', customer_order.total_amount, 'inclusing AUD ', customer_order.service_amount, 'for service charges\n')

            date = input('Please enter the Date of Booking for Dine in (DD/MM/YYYY): ')
            customer_order.date = validate_date(date)
            
            time = input('Please enter the Time of Booking for Dine in (HH:MM): ')
            customer_order.time = validate_hour(time)

            customer_order.number_persons = input('Please enter the number of persons: ')
            print('Thank You for entering the details, your booking is confirmed.')
            
        elif customer_order.order_type == 'self_pickup':
            print('Your total payble amount is: ', customer_order.total_amount, 'AUD\n')

            date = input('Please enter the Date of pick up (DD/MM/YYYY): ')
            customer_order.date = validate_date(date)

            time = input('Please enter the Time of pick up (HH:MM): ')
            customer_order.time = validate_hour(time)

            customer_order.name_pickup = input('Please enter the name of the person: ') 
            print('Thank You for entering the details, your booking is confirmed.')           
        
        elif customer_order.order_type == 'delivery':
            print('Your total payble amount is: ', customer_order.total_amount, 'AUD and there will be an additional charges for Delivery\n')

            date = input('Please enter the Date of delivery (DD/MM/YYYY): ')
            customer_order.date = validate_date(date)

            time = input('Please enter the Time of delivery (HH:MM): ')
            customer_order.time = validate_hour(time)

            distance = float(input('Please enter the distance from the restaurant: '))
            delivery_amount = calculate_delivery_amount(distance)

            if delivery_amount == False:
                customer_order.order_type = 'self_pickup'
                print('Delivery distance limit exceeded. Self Pickup option will be enabled.')
                checkout()
            
            else:
                customer_order.distance = distance
                customer_order.delivery_amount = delivery_amount
                customer_order.calculate_total_amount() #To include delivery amount on total amount calculation
                print('Thank You for your orden, your order has been confirmed.')

        customer_order.id = create_order_id_format()
        logged_user.orders.append(customer_order)
        signin_menu()

    elif select == 'N':
        signin_menu()

    else:
        print('Please enter a valid oprtion.')
        checkout()

#This function calculate delivery amount based on the distance 
def calculate_delivery_amount(distance):
    delivery_amount = False

    if distance > 0.0 and distance <= 5.0:
        delivery_amount = 5.0
    
    elif distance > 5.0 and distance <= 10.0:
        delivery_amount = 10.0
    
    elif distance > 10.0 and distance <= 15.0:
        delivery_amount = 18.0

    return delivery_amount
    
#This function allow to create order id with format S000x
def create_order_id_format():
    global order_counter

    order_counter += 1
    return 'S' + str(order_counter).zfill(4)

##############################################
#
# Task 3: Summary of Transactions 
#
##############################################

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

    select = input()

    if select == '1':
        print_statistics('dine_in', 'All Dine in Orders statistics')
    
    elif select == '2':
        print_statistics('self_pickup', 'All Pick up Orders statistics')

    elif select == '3':
        print_statistics('delivery', 'All Deliveries statistics')

    elif select == '4':
        print_statistics('all_orders', 'All Orders statistics')

    elif select == '5':
        all_total_amount_orders()

    elif select == '6':
        signin_menu()

    else:
        print('Please Enter a valid option.\n')
    
    statistics_menu()

def print_statistics(order_type, title):
    global logged_user

    clean_screen()
    print ("***********************************************************************")
    print ("*               ", title)
    print ("***********************************************************************")

    if order_type == 'dine_in' or order_type == 'self_pickup':
        print('Order ID\t Date\t\t Total Amount Paid\t Type of Order')
    else:
        print('Order ID\t Date\t\t Order Amount Paid\t Type of Order')

    for order in logged_user.orders:

        if order.order_type == order_type or order_type == 'all_orders':
            print(order.id, '\t\t', order.date, '\t', order.total_amount, '\t\t\t', order.order_type)

def all_total_amount_orders():
    global logged_user
    total_amount = 0.0

    for order in logged_user.orders:
        total_amount += order.total_amount
    
    print('\nTotal amount spent on all orders AUD: ', total_amount)

#********************************************************************************

def run():
    initialize_product_list()
    main_menu()

if __name__ == '__main__':
    run()