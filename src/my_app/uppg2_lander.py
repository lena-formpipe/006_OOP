# 2 Länder
#
# 1a På Island bor det 383726 invånare och i Danmark 5961249.
# Skapa objekt för länderna. (Data från januari 2024. Avrunda befolkningen.)
class Country:
    # 1c Lägg till landets area som en egenskap till klassen.
    # Använd en parameter till konstruktorn, alltså __init__ metoden.
    # Ge arean ett default värde på None så att man inte måste ange arean när man skapar ett landsobjekt.
    def __init__(self, name, pop, area = None):
        self.__name = name
        self.__population = pop
        self.__area = area
        self.__language = []

    # 1b Lägg till en metod med namnet "print_info". Metoder ska använda klassens egenskaper,
    # så att den fungerar för de andra länderna och inte bara för Sverige.
    # 1d Ändra i metoden "print_info" så att den skriver ut arean också, men bara om arean inte är None.
    def print_info(self):
        if self.__area == None:
            print(f"I {self.__name} bor det {round(self.__population, 2)} miljoner invånare.")

        else:
            print(f"I {self.__name} bor det {round(self.__population, 2)}  miljoner invånare och en area på {self.__area} kvm.")

        # 1f Ändra i "print_info" så att den skriver ut alla officiella språk, på en ny rad.
        i = len(self.__language)
        if i > 0:
            string_of_languages =""
            while i > 0:
                string_of_languages += self.__language[i-1] + " "
                i = i - 1
            print(f"{self.__name} har följande officiella språk: {string_of_languages}")

    # 1d kunna ange area på landet
    def area(self, int):
        self.__area = int

    # 1e Skapa en ny metod med namnet "add_language". Den ska lägga till ett av landets officiella språk.
    # (Sverige har bara ett, men Finland har två språk (svenska och finska) och Schweiz har fyra.)
    # För att kunna spara ett varierande antal behöver du använda en lista.
    def add_language(self, string):
        self.__language.append(string)

    def __str__(self):
        return f"I {self.__name} bor det {self.__population} miljoner invånare och en area på {self.__area}. och {self.__language}"



# använder klassen Country
print("\n____________________ Uppgift 2 länder __________________________________\n")
print("Skapar landet sverige med pop 10.5555 miljoner invånare.")
se = Country("Sverige", 10.5555)
print("Sätt area = 100.")
se.area(100)
print("Sätt språk svenska.")
se_sv = "svenska"
se.add_language(se_sv)
print("Skapa landet island.")
isl = Country("Island", 0.4)
print("Lägg till språk samiska i sverige.")
se.add_language("samiska")
print("\nSkriv ut ländernas information:")

se.print_info()
isl.print_info()

