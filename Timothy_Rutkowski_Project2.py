# Timothy Rutkowski 04/10/2024 Timothy_Rutkowski_Project2.py

# CoffeeShop02
# This program will prompt users to select options from three menus to complete 
# and calculate the cost of a coffee order or to process existing orders from
# a file and calculate those order totals.

# For easy reading, throughout this program casing is used in the following manner: 
# constants are MACRO_CASED, 
# variables are snake_cased, 
# and functions are camelCased.

# Global Constants
# Coffee size in ounces
REGULAR = 8
GRANDE = 16
VENTI = 24
# Coffee product price per ounce
PLAIN_PRICE = 0.28
LATTE_PRICE = 0.36
MACCHIATO_PRICE = 0.39
FRAPPUCCINO_PRICE = 0.42

SALES_TAX_RATE = 0.0725

# Functions
# The Main Function of the program
def main():
    while True:
        option = mainMenu()

        if option == '1':
            coffee_type = coffeeMenu()
            coffee_size = sizeMenu()
            price = calcPriceSingleOrder(coffee_type, coffee_size)
            sales_tax = calcSalesTax(price)
            order_total = price + sales_tax

            customer_name = input('\nEnter customer name: ').strip()
            coffee_type_str = convertSelectionToString(coffee_type, ['Plain Coffee', 'Latte', 'Macchiato', 'Frappuccino'])
            coffee_size_str = convertSelectionToString(coffee_size, ['Regular', 'Grande', 'Venti'])
            
            displayResults(customer_name, coffee_type_str, coffee_size_str, price, sales_tax, order_total)
        elif option == '2':
            processOrderFile()
        elif option == '3':
            print('Thank you for your business!')
            break
        else:
            print('Invalid option.')




# Function to display the order menu and get user input
def mainMenu():
    print('\nWelcome to the World\'s Best Coffee Shop!')
    print('\n\tMain Menu')
    print('1-Process single order')
    print('2-Process order file')
    print('3-End program')
    return input('\nSelect Option: ')
            
# Function to display the coffee choices menu and get user input
def coffeeMenu():
    print('\n\tCoffee Menu')
    print('1-Plain Coffee')
    print('2-Latte')
    print('3-Macchiato')
    print('4-Frappuccino')
    while True:
        selection = input('\nSelect Option: ')
        if selection in ['1', '2', '3', '4']:
            return selection
        else:
            print('Invalid selection. Please choose a valid option.')

# Function to display the coffee sizes menu and get user input
def sizeMenu():
    print('\n\tSize Menu')
    print('1-Regular')
    print('2-Grande')
    print('3-Venti')
    while True:
        selection = input('\nSelect Option: ')
        if selection in ['1', '2', '3']:
            return selection
        else:
            print('Invalid selection. Please choose a valid option.')
            
# Function to calculate the price of coffee based on type and size for a single order
def calcPriceSingleOrder(coffee_type, coffee_size):
    size_in_ounces = 8 if coffee_size == '1' else 16 if coffee_size == '2' else 24
    price_per_ounce = (
        0.28 if coffee_type == '1' else
        0.36 if coffee_type == '2' else
        0.39 if coffee_type == '3' else
        0.42
    )
    return size_in_ounces * price_per_ounce

# Function to convert numeric selection to string name
def convertSelectionToString(selection, menu_options):
    return menu_options[int(selection) - 1]   

   
    
    
# Function to process orders from a file
def processOrderFile():
    coffee_sizes = {'8': 'Regular', '16': 'Grande', '24': 'Venti'}  # Map size codes to size names

    try:
        with open('coffeeShopData.txt', 'r') as file:
            orders = file.readlines()  # Read lines into a list

            for order in orders:
                data = order.strip().split(',')  # Split each line into parts
                if len(data) >= 3:
                    customer_name = data[0]
                    coffee_type = data[1]
                    coffee_size_code = data[2]  # Get size code
                    coffee_size = coffee_sizes.get(coffee_size_code, 'Unknown Size')  # Get size name from code

                    try:
                        price = calcPriceOrderFile(coffee_type, coffee_size_code, coffee_sizes)
                        sales_tax = calcSalesTax(price)
                        order_total = price + sales_tax                  
                        displayResults(customer_name, coffee_type, coffee_size, price, sales_tax, order_total)
                    except ValueError as e:
                        print(f'Error processing order for {customer_name}: {e}')
                else:
                    print(f'Invalid data format: {order.strip()}')
    except IOError:
        print('Error: could not read the file.')
    except FileNotFoundError:
        print('Error: File not found.')
        
# Function to calculate the price of coffee based on type and size for orders from a file
def calcPriceOrderFile(coffee_type, coffee_size_code, coffee_sizes):
    size_name = coffee_sizes.get(coffee_size_code, 'Unknown Size')  # Get size name from code
    size_in_ounces = 8 if size_name == 'Regular' else 16 if size_name == 'Grande' else 24
    price_per_ounce = (
        0.28 if coffee_type == 'Plain Coffee' else
        0.36 if coffee_type == 'Latte' else
        0.39 if coffee_type == 'Macchiato' else
        0.42
    )
    return size_in_ounces * price_per_ounce




# Function to calculate the sales tax based on coffee price
def calcSalesTax(price):
    return price * SALES_TAX_RATE

# Function to display the results of the order
def displayResults(customer_name, coffee_type, coffee_size, price, sales_tax, order_total):
    print('\n\tOrder Details')
    print('Customer -', customer_name)
    print('Ordered -', coffee_type, coffee_size)
    print('Coffee price\t{:.2f}'.format(price))
    print('Sales tax\t{:.2f}'.format(sales_tax))
    print('Order_total\t{:.2f}'.format(order_total)) 

# Call the Main Function
if __name__ == '__main__':
    main()

