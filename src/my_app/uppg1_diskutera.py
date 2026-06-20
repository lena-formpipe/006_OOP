# 1 Vad gör följande kod?
class SafeStorage:
    __data = None   #__privat
    def get(self):
        return self.__data
    def put(self, data):
        self.__data = data


# skapar ett objekt av typen safestorage
safe = SafeStorage()
# använder klassens metod (funktion) put för att ange data
safe.put("Anakonda")

#skapa en variabel som hämtar data Anakonda
x = safe.get()

# skriv över till Boaorm
safe.put("Boaorm")

#skapa en variabel som hämtar data Boaorm
y = safe.get()

# skriv ut variabler anakonda och boaorm
print(x, y)

# 2a Vad gör följande kod? Fixa eventuella fel.
class Animal:
    def make_noise(self):
        print("Detta djur har vi inget ljud för.")

# Om man specificerar klassen make_noise så skriver den över klassen Animal
class Dog(Animal):
    def make_noise(self):
        print("Voff!")


# om man anropar super().make_noise() OCH definierar egen make_noice
# så får objektet BÅDA egenskaperna i den ordning de definiteras in (?)

class Cat(Animal):
    def make_noise(shelf):
        super().make_noise()
        print("Mjau!")

# om man inte specificerar make_noise blir det samma som klassen Animal
class Rooster(Animal):
    print("Hej")

# anropar objektets make_noise()
def sound_off(animal):
    animal.make_noise()

# 2b Lägg till en klass för ett annat djur, till exempel en papegoja.
class Parrot(Animal):
    def make_noise(self):
        print("Krax!")



c = Cat()
d = Dog()
h = Rooster()
print("Skriv ut Dog")
d.make_noise()
print("---------------")
print("Skriv ut Cat")
c.make_noise()
print("---------------")
print("Skriv ut Rooster")
h.make_noise()
print("---------------")

# Kan inte anropa med en lista, måste anropa per objekt
# sound_off([c, d, h])
# skriv in en loop
list = [c, d, h]
i = 0
while i <= (len(list)-1):
    sound_off(list[i])
    print
    i += 1


# kan anropa med ett objekt animal
# sound_off(c)


