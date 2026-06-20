# 3 Banken. Skapa en klass som representerar ett bankkonto. Gör en metod för varje funktionalitet.:
# ●	sätta in pengar (deposit)
# ●	ta ut pengar (withdraw)
# ●	returnera nuvarande saldo (balance)
# ●	räkna ut ränta (apply_interest, lägger till räntan till kontot)
# ●	tala om ifall man har råd att betala en räkning (returnera True/False)
# Skriv enhetstester för varje funktion.
# Använd gärna TDD-metoden, att börja med testfallen innan du skriver koden.

class Bank_account:
    # när kontot öppnas är startsumman samma som current_sum
    def __init__(self, name, startsum = 0, interest=0.01):
        self.__name = name
        self.__startsum = startsum
        self.__interest = interest
        self.__current_sum = startsum
        # gör en synlig variabel
        self.visible = startsum

    # ●	sätta in pengar (deposit)
    def deposit(self, sum_to_deposit):
        self.__current_sum += sum_to_deposit


    # ●	ta ut pengar (withdraw)
    def withdraw(self, sum_to_withdraw):
        self.__current_sum -= sum_to_withdraw


    # ●	returnera nuvarande saldo (balance)
    def balance(self):
        return self.__current_sum


    # ●	räkna ut ränta (apply_interest, lägger till räntan till kontot)
    def apply_interest(self):
        self.__current_sum = self.__current_sum * ((1 + self.__interest))


    # ●	tala om ifall man har råd att betala en räkning (returnera True/False)
    def pay_a_bill(self, bill):
        if self.__current_sum >= bill:
            return True
        else:
            return False



