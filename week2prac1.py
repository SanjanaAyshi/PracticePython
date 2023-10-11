#Create a Product class and a Shop class.
class Product:
     def __init__(self, name, price,quantity):
        self.name = name
        self.price = price
        self.quantity=quantity

class Shop:
    def __init__(self):
        self.products = []

#Inside the Shop class, create a method name 
# add_product which adds products using the
#  Product class to the Shop class.


    def add_product(self,product):
        self.products.append(product)

    def buy_product(self,name,quantity): #check product is available or not
        for product in self.products:
            if product.name== name and product.quantity>= quantity:
                product.quantity-=quantity
                print(f"Congratulations! You bought {quantity} of {name}.")
                return
        print(f"Sorry {quantity} of {name} are not available.")

product1=Product("Coca-cola", 25 ,2)
product2=Product("RC", 18 ,50)
product3=Product("Pepsi", 25 ,30)
my_shop=Shop()
my_shop.add_product(product1)
my_shop.add_product(product2)
my_shop.add_product(product3)

my_shop.buy_product("RC",5)
my_shop.buy_product("Coca-cola",5)


