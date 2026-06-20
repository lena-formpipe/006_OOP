from my_app.uppg3_banken import *
from my_app.uppg4_webbshop import *

# MAIN.PY ANVÄNDER KODEN FRÅN UPPGIFT 3 OCH UPPGIFT 4

print("------------------------ Uppgift 3 __________________________________________")
#skapa ett bankkonto
mitt_konto = Bank_account("Mitt konto", 500)
deposit_amount = 600
withdrawal_amount = 100
interest = 0.1
bill = 900
print("Har skapat ett konto.")
print(f"Saldot är {mitt_konto.balance()}.")
mitt_konto.deposit(deposit_amount)
print(f"Efter insättning {deposit_amount} är saldot {mitt_konto.balance()} kr.")
mitt_konto.withdraw(withdrawal_amount)
print(f"Efter uttag {withdrawal_amount} är saldot {mitt_konto.balance()} kr.")
mitt_konto.apply_interest()
print(f"Efter fast ränta är saldot {mitt_konto.balance()} kr.")
print(f"Du har en räkning på {bill} kr.")
print(f"Har du råd att betala den? = {mitt_konto.pay_a_bill(bill)}!")


print("\n________________________ Uppgift 4 ____________________________________________")
# skapa artiklar till webbshoppen
hammare = Product("Hammare", 150)
skruvmejsel = Product("Skruvmejselset", 300)
skiftnyckel = Product("Skiftnyckel", 200)
tumstock = Product("Tumstock", 50)
vattenpass = Product("Vattenpass", 150)
borrmaskin = Product("Borrmaskin", 1000)
avbitare = Product("Avbitare", 150)
kniv = Product("Kniv", 100)
hylsnyckel = Product("Hylsnyckelsats", 500)
fogsvans = Product("Fogsvans", 200)
produktlista = [hammare, skruvmejsel, skiftnyckel, tumstock, vattenpass, borrmaskin, avbitare, kniv, hylsnyckel, fogsvans]
print("Följande artiklar till webbshoppen har skapats:")
print(produktlista)

# skapa två kundvagnar
a_kundvagn = Shopping_cart()
b_kundvagn  = Shopping_cart()
print("\nTvå tomma kundvagnar har skapats:")
print(a_kundvagn)
print(b_kundvagn)

#  lägg till/ta bort artiklar
a_kundvagn.add_product_to_cart(vattenpass)
a_kundvagn.add_product_to_cart(vattenpass)
a_kundvagn.add_product_to_cart(hammare)
a_kundvagn.add_product_to_cart(kniv)
a_kundvagn.remove_product_from_cart(vattenpass)

b_kundvagn.add_product_to_cart(hammare)
b_kundvagn.add_product_to_cart(kniv)
b_kundvagn.add_product_to_cart(hammare)
b_kundvagn.add_product_to_cart(kniv)
b_kundvagn.remove_product_from_cart(kniv)

# skriv ut kundvagnarna
print("\nNu har kundvagnarna fyllts med innehåll:")
print(a_kundvagn)
print(b_kundvagn)

# skapa order från kundvagn
a_order = Order(a_kundvagn)
b_order = Order(b_kundvagn)
print("\nNu har två order skapats från de två kundvagnarna:")

# skriv ut order
print(a_order)
print(b_order)

cart = Shopping_cart()
cart.add_product_to_cart(kniv)
cart.add_product_to_cart(kniv)
cart.remove_product_from_cart(kniv)
