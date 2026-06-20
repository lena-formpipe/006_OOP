# 4 Webbshop
# Skapa klasser som representerar en webbshop:
# ●	produkter (Product)
# ●	beställningar (Order)
# ●	kundvagn (ShoppingCart)
#
# Tips 1! Ge varje klass en egenskap "__id".
# Tips 2! Du kan använda AI för att skapa realistisk testdata.

class Product:
    # id ska genereras automatiskt med start från 1
    next_id_product = 1

    def __init__(self, name, price):
        # generera automatiskt id-nummer för nya produkter och stega upp ett steg för nästa
        self.__id_product = Product.next_id_product
        Product.next_id_product += 1
        self.__name = name
        self.__price = price

    # möjlighet att ändra pris
    def set_price(self, price):
        self.__price = price

    # möjlighet att ändra namn
    def set_name(self, name):
        self.__name = name

    # hämta pris för att kunna presentera
    def get_price(self):
        return self.__price

    # hämta namn för att kunna presentera
    def get_name(self):
        return self.__name

    # gjorde denna enkom för test, är antagligen inte god praxis men ett val i denna veckouppgift
    def get_item_info_for_test (self):
        return self.__name + str(self.__price) + str(self.__id_product)

    # kunna anropa produkten för att presentera i sin helhet
    # print(product)      # använder __str__
    def __str__(self):
        return f"{self.__name} {self.__price} kr, id: {self.__id_product}"

    # kunna anropa en lista av produkter
    # print([product])    # använder __repr__ för elementen i listan
    def __repr__(self):
        return f"\n{self.__name} {self.__price} kr, id: {self.__id_product}"

class Shopping_cart:
    # id ska genereras automatiskt med start från 1
    next_id_shopping_cart = 1

    def __init__(self):
        # generera automatiskt id-nummer för nya produkter och stega upp med +1
        self.__id_cart = Shopping_cart.next_id_shopping_cart
        Shopping_cart.next_id_shopping_cart += 1
        # börja kundvagnen med en tom lista med produkter
        self.products_in_cart = []


    # lägg till produkt till kundvagnens lista
    def add_product_to_cart(self, product):
        self.products_in_cart.append(product)

    # ta bort produkt från kundvagnens lista
    def remove_product_from_cart(self, product):
        self.products_in_cart.remove(product)

    # totalsumma pris av alla produkter i kundvagnen
    def total_sum_of_cart (self):
        total_sum = 0
        for product in self.products_in_cart:
            total_sum += product.get_price()
        return total_sum

    # gjorde denna enkom för test, är antagligen inte god praxis men ett val i denna veckouppgift
    def get_cart_info_for_test (self):
        text=""
        for product in self.products_in_cart:
            text += f"{product.get_name()}{product.get_price()}"
        return text


    # skriv ut hela kundvagnen för överblick
    def __str__(self):
        text = f"\nKundvagn {self.__id_cart}\n"
        for product in self.products_in_cart:
            text += f"{product.get_name()} - {product.get_price()} kr\n"
        text += f"Totalpris: {self.total_sum_of_cart()} kr"
        return text

class Order:
    next_id_order = 1

    # order är en kopia av produkterna i kundvagnen, tar in kundvagnen som inparameter
    # skicka kundvagnen till konstruktorn för Order
    def __init__(self, shopping_cart):
        # generera automatiskt id-nummer för nya order
        self.__id_order = Order.next_id_order
        Order.next_id_order += 1
        # orderns produkter ska vara samma som kundvagnens produkter
        self.products_in_order = shopping_cart.products_in_cart

    # totalsumman av alla produkter i order
    def total_sum_of_order (self):
        total_sum = 0
        for product in self.products_in_order:
            total_sum += product.get_price()
        return total_sum

    # skriv ut hela ordern för överblick
    def __str__(self):
        text = f"\nOrder {self.__id_order}\n"
        for product in self.products_in_order:
            text += f"{product.get_name()} - {product.get_price()} kr\n"
        text += f"Totalpris Order: {self.total_sum_of_order()} kr"
        return text
        return


