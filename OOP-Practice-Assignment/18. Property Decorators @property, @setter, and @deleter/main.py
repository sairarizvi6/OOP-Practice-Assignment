#Assignment No-18:
#Create a class Product with a private attribute _price. 
#Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self, price) -> None:
        self.__price = price

    @property
    def price(self) -> int | float:
        try:
            return self.__price
        except AttributeError:
            print("Please set a price first.")
    
    @price.setter
    def price(self, new_price) -> None:
        if new_price > 0 and isinstance(new_price, (int, float)):
            self.__price = new_price
        else:
            print("Please enter a valid price")
    
    @price.deleter
    def price(self) -> None:
        del self.__price

# Example usage:
product = Product(100)
print(product.price)  # Getting price
product.price = 200   # Setting price
print(product.price)  # Getting price
del product.price     # Deleting price
print(product.price)