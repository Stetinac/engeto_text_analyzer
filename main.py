'''
author = Pavel Stetina
'''
# promene
delimiter = ("-" * 50)
vycistena_slova = []
upper_start = 0
upper_all = 0
numbers = 0
numbers_sum = 0
lower_all = 0
delka_slov = {}
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

         '''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

         '''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
         ]

users = dict(bob="123", ann="pass123", mike="password123", liz="pass123")

print(delimiter)
user_name = input("Uživatelské jméno: ")
password = input("Heslo: ")

# Prihlasovani uzivatele
if password != users[user_name]:
    print("Zadal jsi špatné jméno nebo heslo!")
    quit()
else:
    print(f"Ahoj{user_name}, vítej v naší aplikaci!")
    print(delimiter)

for index, text in enumerate(TEXTS):  # vytisknutí textu z TEXTS
    print(f"Text č.{index + 1}: {TEXTS[index]}\n")

volba = input("Vyber si číslo textu k analyzování: ")  # vyber textu k analyzovaní
if volba.isalpha() or int(volba) not in range(1, 4):    # pokd neni vybrano spravne, nebo je vlozeno pismeno tak quit()
    print("Vybral jsi hodnotu/číslo textu, které není v nabídce!")
    quit()
else:
    volba = int(volba)
    # print(f"Vybral jsi si text č.{volba}")
vybrany_text = TEXTS[volba - 1]
# print(vybrany_text)

for slovo in vybrany_text.split():  # rozseka list na slova a oreze je o nezadouci znaky
    ciste_slovo = slovo.strip(' .,!')
    vycistena_slova.append(ciste_slovo)
words_len = len(vycistena_slova)
print(f"Ve vybranem textu je celkem: {words_len} slov!")  # Zjisteni poctu slov ve vybranem textu

# vypocet prislusne skupiny slov
for slovo in vycistena_slova:
    if slovo[0].isupper() and not slovo.isdigit():  # Pokud prvni pismeno je velke a nejedna se o cislo
        # print(f"{slovo} ma upper!")
        upper_start = upper_start + 1
        if slovo.isupper():     # zkus zda i cele slovo neni velkyma
            # print(f"{slovo} je cele velke")
            upper_all = upper_all + 1
    elif slovo.isdigit():   # pokdu je slovo cislo, zpracuj
        # print(f"{slovo} je cislo")
        numbers = numbers + 1
        numbers_sum = numbers_sum + int(slovo)
    elif slovo.islower():   # pokud je slovo malejma, zpracuj
        lower_all = lower_all + 1
    else:   # slova, ktera neprosla podminkama a v zadani neni co se s nima ma delat
        # print(f"zbytek je {slovo}")
        continue
# vystupy na obrazovku
print(delimiter)
print(f"Ve vybranem textu je celkem: {upper_start} slov začínajících velkým písmenem!")
print(f"Ve vybranem textu je celkem: {upper_all} slov velkým písmem!")
print(f"Ve vybranem textu je celkem: {lower_all} slov malým písmem!")
print(f"Ve vybranem textu je celkem: {numbers} čísel!")
print(f"Součet všech čísel ve vybraném textu je: {numbers_sum}")
print(delimiter)
print("    Delka    |      Graf      |    Počet")
print(delimiter)

for slovo in vycistena_slova:    # priradi do klice delku slova a pokud jiz klic existuje, navysi jeho hodnotu o +1
    if len(slovo) in delka_slov.keys():
        delka_slov[len(slovo)] = delka_slov[len(slovo)] + 1
    else:
        delka_slov[len(slovo)] = 1

# print(delka_slov)
for keys in sorted(delka_slov):    # pro serazeny seznam vypise klice od nejnizsiho a vypise jejich hodnoty
    print(keys, "|", ("*" * delka_slov[keys]), "|", delka_slov[keys])
