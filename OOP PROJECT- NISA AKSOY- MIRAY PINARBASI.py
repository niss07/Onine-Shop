from abc import ABC, abstractmethod #To define a method that subclasses must implement
from random import randint #To give random integer

class Product(ABC): #Abstract class for product    
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    @abstractmethod 
    def get_price(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

    def get_color(self):
        return self.color #Color cannot be decorate so it returns

available_products = [] #List to store available products

def initialize_products():
    available_products.extend([ #To add products to the list individually
        Phone("iPhone 16", "Teal", 900.0),
        Thermos("Stanley 500ml Thermos", "Gray", 30.0),
        Bracelet("Friendship Bracelet", "Silver", 20.0),
        Phone("Samsung S24", "Purple", 800.0),
        Bracelet("Sunset Bracelet", "Gold", 50.0)
    ])

def display_products(): #Display all available products
    print("Available Products:")
    for i, product in enumerate(available_products): #For each enumerated item, write everything that is a product into available products
        print(f"{i + 1}. {product.get_color()} {product.get_name()} - {product.get_price()}$") #Start from i+1 to avoid item 0

def get_product(index): #Retrieve a product by index from the available products
    return available_products[index] 


class ProductDecorator(Product): #To decorate the selected product
    def __init__(self, decorated_product): 
        super().__init__(decorated_product.get_name(), decorated_product.get_color(), decorated_product.get_price()) 
        self.decorated_product = decorated_product #Creating an decorated product


class FastDeliveryDecorator(ProductDecorator): #Concrete decorator for Fast Delivery
    def get_price(self):
        return self.decorated_product.get_price() + 5.00 
    
    def get_name(self):
        return f"{self.decorated_product.get_name()} with fast delivery"


class GiftDecorator(ProductDecorator): #Concrete decorator for Gift Decorator
    def get_price(self):
        return self.decorated_product.get_price() + 7.00

    def get_name(self):
        return f"{self.decorated_product.get_name()} with gift box"


class InsuranceDecorator(ProductDecorator): #Concrete decorator with insurance
    def get_price(self):
        return self.decorated_product.get_price() / 100 * 110 #The price of the product increased by 10% with insurance
    def get_name(self):
        return f"{self.decorated_product.get_name()} with insurance"


class Bracelet(Product): #Concrete class for Bracelet
    def get_price(self):  #get_price Overriden
        return self.price  
    #get_color is not overridden because it is not a structure that will change
    def get_name(self): #get_name overriden
        return self.name


class Phone(Product): #Concrete class for Phone
    def get_price(self): #Overriding
        return self.price

    def get_name(self): #Overriding
        return self.name

class Thermos(Product): #Concrete class for Thermos
    def get_price(self): #Overriding
        return self.price

    def get_name(self): #Overriding
        return self.name


class ShoppingCart: #Not inherited because it is composition
    def __init__(self):
        self.product_list = [] 

    def add_product(self, product):
        self.product_list.append(product) 

    def total_price(self):
        return sum(product.get_price() for product in self.product_list) #Returns the total price of the items in the shopping cart

    def display_cart(self):
        if not self.product_list:
            print("You haven't added anything to your shopping cart yet.")
        else:
            print("Here are the products in your shopping cart:")
            for i, product in enumerate(self.product_list): #Prints the numbered items in the shopping cart on the screen
                print(f"{i + 1}. {product.get_name()} - {product.get_price()}$") 



if __name__ == "__main__": #Main function
    print("-" * 100)
    print("                                      Welcome to our store!")
    print("-" * 100)

    initialize_products() 

    display_products() #has to create the initialize_products first, cannot display without creating them

    shopping_cart = ShoppingCart() #Objectify for use

    made_purchase = False

    while True: #While loop was used to add products repeatedly
        print("-" * 100)
        print("Enter the number of the product to add to cart (Press 0 to finish - Press 9 to see your shopping cart):")
        choice = int(input()) #Get data from user
        if choice == 9:
            shopping_cart.display_cart() 
            continue 

        if choice == 0:
            if not made_purchase:
                print("\nSee you again, take care!")
            else:
                print(f"\nFinal total price of your cart: {shopping_cart.total_price()}$\n")
                print("Your purchase has been completed successfully, thank you!")
                delivery_time = randint(1, 10) #Randint was used to get random values
                print(f"Your order will arrive within {delivery_time} days.") 
            break

        chosen_product = get_product(choice - 1) #To restore the index to its original state, which I started from i+1
        print(f"You have chosen: {chosen_product.get_name()}")
        print("Choose decoration for the product:")
        print("1. Fast Delivery\n2. Add Gift Box\n3. Make Insurance\n4. No Decoration")
        decoration_choice = int(input())

        if decoration_choice == 1:
            chosen_product = FastDeliveryDecorator(chosen_product)
            print("You have applied: Fast Delivery")
        elif decoration_choice == 2:
            chosen_product = GiftDecorator(chosen_product)
            print("You have applied: Gift Box")
        elif decoration_choice == 3:
            chosen_product = InsuranceDecorator(chosen_product)
            print("You have applied: Insurance")
        else:
            print("No decoration applied.")

        print(f"The new price of the product is: {chosen_product.get_price()}$\n")
       
        shopping_cart.add_product(chosen_product) #Add the selected decorated product to the shopping cart
        made_purchase = True 
        
        print(f"Current total price of your cart: {shopping_cart.total_price()}$\n")
        print("-" * 100)
        display_products() #To ensure that products are displayed once again