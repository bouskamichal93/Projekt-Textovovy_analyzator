"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Michal Bouška
email: michal.bouska93@gmail.com
"""

#DATA
#registrovaní uživatelé
users_registered = {
    'bob':'123',
    'ann':'pass123',
    'mike':'password123',
    'liz':'pass123'}

#texty
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
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
    garpike and stingray are also present.''']

first_text = TEXTS[0]
second_text = TEXTS[1]
third_text = TEXTS[2]

#ANALÝZA FCE
#počítání slov
def word_counter(text): 
    text_splited = text.split() #rozsekání textu na jednotlivá slova a uložení do listu text_splited
    pocet_slov = len(text_splited)
    print(f'Počet slov v textu: {pocet_slov}')


#počítání velkých písmen   
def pocet_velkych_pismen(text):
    text_splited = text.split()
    
    #počítání velkých písmen   
    pocet_velkych = 0
    for x in text_splited: 
        b=x[0] # první znak stringu
        if b>='A' and b<='Z':
            pocet_velkych+=1
    print(f'Celkový počet slov začínajících velkým písmenem {pocet_velkych}')  
    
    #počítání vět, tedy slov začínajících velkým pismenem    
    text_splited = text.split(". ") #text rozdělený do vět
    pocet_vet = len(text_splited)
    print(f'Počet slov začínajících velkým písmenem: {pocet_vet}')
    
    #počítání názvů
    nazev = pocet_velkych - pocet_vet
    print(f'Počet názvů: {nazev}')
    
    
#počítání malých písmen   
def pocet_malych_pismen(text):
    text_splited = text.split()   
    pocet_malych = 0
    for x in text_splited: 
        b=x[0]
        if b>='a' and b<='z':
            pocet_malych+=1
    print(f'Počet slov začínajících malým písmenem: {pocet_malych}')
    
    
def pocet_num(text):
    text_splited = text.split()   
    pocet_num = 0
    for x in text_splited: 
        b=x[0]
        if b>='1' and b<='9':
            pocet_num+=1
    print(f'Počet numerických stringů: {pocet_num}') 
    
def suma_num(text):
    text_splited = text.split()   
    suma_num = 0
    numeric_list = []
    for x in text_splited: 
        b=x[0]
        if b>='1' and b<='9':
            numeric_list.append(int(x))        
    for y in numeric_list:
        suma_num += y
    print(f'Suma všech čísel obsažených v textu: {suma_num}') 



def analyza_poctu_znaku(text):
    text_bez_tecek = text.replace(".","") #odstraní z textu tečky
    text_bez_carek = text_bez_tecek.replace(",","") #odstraní z textu čárky
    cisty_text = text_bez_carek.split() #rozbije text na slova
    delka_slova = [] #prázdný text do kterého se bude ukládat délka slova
    for x in cisty_text: 
        delka_slova.append(int((len(x)))) #zjistí délku slova a přidá jí do listu delka_slova
    delka_slova.sort() #seřadí naplněný list podle velikosti
    
    pocet_1 = delka_slova.count(1)
    pocet_2 = delka_slova.count(2)
    pocet_3 = delka_slova.count(3)
    pocet_4 = delka_slova.count(4)
    pocet_5 = delka_slova.count(5)
    pocet_6 = delka_slova.count(6)
    pocet_7 = delka_slova.count(7)
    pocet_8 = delka_slova.count(8)
    pocet_9 = delka_slova.count(9)
    pocet_10 = delka_slova.count(10)
    pocet_11 = delka_slova.count(11)
    pocet_12 = delka_slova.count(12)
    pocet_13 = delka_slova.count(13)
    pocet_14 = delka_slova.count(14)
    pocet_15 = delka_slova.count(15)
    
    print ("DÉLKA SLOVA|\tVÝSKYT\t|POČET")
    if pocet_1 != 0:
        print("1|", "*"*pocet_1, "|",pocet_1)
    if pocet_2 != 0:
        print("2|", "*"*pocet_2, "|",pocet_2)
    if pocet_3 != 0:
        print("3|", "*"*pocet_3, "|",pocet_3)
    if pocet_4 != 0:
        print("4|", "*"*pocet_4, "|",pocet_4)
    if pocet_5 != 0:
        print("5|", "*"*pocet_5, "|",pocet_5)
    if pocet_6 != 0:
        print("6|", "*"*pocet_6, "|",pocet_6)
    if pocet_7 != 0:
        print("7|", "*"*pocet_7, "|",pocet_7)
    if pocet_8 != 0:
        print("8|", "*"*pocet_8, "|",pocet_8)
    if pocet_9 != 0:
        print("9|", "*"*pocet_9, "|",pocet_9)
    if pocet_10 != 0:
        print("10|", "*"*pocet_10, "|",pocet_10)
    if pocet_11 != 0:
        print("11|", "*"*pocet_11, "|",pocet_11)
    if pocet_12 != 0:
        print("12|", "*"*pocet_12, "|",pocet_12)
    if pocet_13 != 0:
        print("13|", "*"*pocet_13, "|",pocet_13)
    if pocet_14 != 0:
        print("14|", "*"*pocet_14, "|",pocet_14)
    if pocet_15 != 0:
        print("15|", "*"*pocet_15, "|",pocet_15)
    
    
uzivatelska_jmena = users_registered.keys()
'''uložení uživatelských jmen do listu jménem uzivatelska_jmena pro následnou kontrolu,
že se nacházejí v dictionary users_registered'''



#KONTROLA REGISTROVANÉHO UŽIVATELE
user_name = str(input('Zadejte uživatelské jméno:'))
for x in uzivatelska_jmena: 
    if x == user_name:
        print(f'{user_name} je registrovaný uživatel!!!')
        break
else:
        print(f'{user_name} není registrovaný uživatel!!!')
        exit()

#KONTROLA HESLA
password = str(input('Zadejte prosím heslo:'))
if password == users_registered.get(user_name): #kontrola správnosti hesla
    print('Heslo zadáno správně!!!')
else:
    print('Heslo zadáno špatně!!!')
    exit()

print('-'* 50)
print(f'Aplikace Textový analizátor vítá uživatele {user_name}')
print('-'* 50)
user_choice = str(input('Máme 3 texty k analýze, máte na výběr z možností 1 až 3:'))
print('-'* 50)
if user_choice == '1':
    print('Analýza textu č.1:\n')
    word_counter(first_text)
    pocet_velkych_pismen(first_text)
    pocet_malych_pismen(first_text)
    pocet_num(first_text)
    suma_num(first_text)
    print('-'* 50)
    analyza_poctu_znaku(first_text)
    print('-'* 50)
    
    
    
elif user_choice == '2':
    print('Analýza textu č.2:\n')
    word_counter(second_text)
    pocet_velkych_pismen(second_text)
    pocet_malych_pismen(second_text)
    pocet_num(second_text)
    suma_num(second_text)
    print('-'* 50)
    analyza_poctu_znaku(second_text)
    print('-'* 50)
    
    
elif user_choice == '3':
    print('Analýza textu č.3:\n')
    word_counter(third_text)
    pocet_velkych_pismen(third_text)
    pocet_malych_pismen(third_text)
    pocet_num(third_text)
    suma_num(third_text)
    print('-'* 50)
    analyza_poctu_znaku(third_text)
    print('-'* 50)
    
    
else: 
    print('Tento text neexistuje!!!')
    exit()

