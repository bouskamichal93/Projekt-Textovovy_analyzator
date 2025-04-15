"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Michal Bouška
email: michal.bouska93@gmail.com
"""
from collections import Counter
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

#ANALÝZA FCE
#počítání slov
def word_counter(text): 
    text_splited = text.split() #rozsekání textu na jednotlivá slova a uložení do listu text_splited
    pocet_slov = len(text_splited)
    print(f'Ve vybraném textu je {pocet_slov} slov')


#počítání velkých písmen   
def pocet_velkych_pismen(text):
    text_splited = text.split()  
    pocet_velkych = 0
    pouze_velka_pismena = 0 
    
    for x in text_splited: 
        b=x[0] # první znak stringu
        if b in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            pocet_velkych += 1
    
    for x in text_splited:
        if x.isupper():
            pouze_velka_pismena += 1
    
    print(f'Počet slov začínajících velkým písmenem: {pocet_velkych-pouze_velka_pismena}')
    print(f'Počet slov obsahujících pouze velká písmena: {pouze_velka_pismena}')
    
    
#počítání malých písmen   
def pocet_malych_pismen(text):
    text_splited = text.split()   
    pocet_malych = 0
    for x in text_splited: 
        b=x[0]
        if b in 'abcdefghijklmnopqrstuvwxyz':
            pocet_malych+=1
    print(f'Počet slov začínajících malým písmenem: {pocet_malych}')
    
    
def pocet_num(text):
    text_splited = text.split()   
    pocet_num = 0
    for x in text_splited: 
        b=x[0]
        if b in '0123456789':
            pocet_num+=1
    print(f'Počet numerických stringů: {pocet_num}') 
    
def suma_num(text):
    text_splited = text.split()   
    suma_cisel = 0
    numeric_list = []
    for x in text_splited: 
        b=x[0]
        if b in '0123456789':
            numeric_list.append(int(x))        
    for y in numeric_list:
        suma_cisel += y
    print(f'Suma všech čísel obsažených v textu: {suma_cisel}') 


def analyza_poctu_znaku(text):
    text_bez_tecek = text.replace(".","") #odstraní z textu tečky
    text_bez_carek = text_bez_tecek.replace(",","") #odstraní z textu čárky
    cisty_text = text_bez_carek.split() #rozbije text na slova
    delka_slova = [] #prázdný list do kterého se bude ukládat délka jednotlivých slov
    for x in cisty_text: 
        delka_slova.append(int((len(x)))) #zjistí délku slova a přidá jí do listu delka_slova
    delka_slova.sort() #seřadí naplněný list podle velikosti
    hodnoty = Counter(delka_slova)
    hodnoty_dict = dict(hodnoty)        
    print ("DÉLKA SLOVA|VÝSKYT|POČET")
    for x, y in hodnoty_dict.items():
        if x <10:
            print(x,format('*'* y, ' <25'), y, sep=' |')
        else:
            print(x,format('*'* y, ' <26'), y, sep='|')
        
        
    
#KONTROLA REGISTROVANÉHO UŽIVATELE   
uzivatelska_jmena = users_registered.keys()
'''uložení uživatelských jmen do listu jménem uzivatelska_jmena pro následnou kontrolu,
že se nacházejí v dictionary users_registered'''

user_name = str(input('Zadejte uživatelské jméno: '))
for x in uzivatelska_jmena: 
    if x == user_name:
        print(f'{user_name} je registrovaný uživatel!!!')
        break
else:
        print(f'{user_name} není registrovaný uživatel!!!')
        exit()

#KONTROLA HESLA
password = str(input('Zadejte prosím heslo: '))
if password == users_registered.get(user_name): #kontrola správnosti hesla
    print('Heslo je správně!!!')
else:
    print('Heslo je špatně!!!')
    exit()

print('='* 50, '\n')
print(f'Aplikace Textový analizátor vítá uživatele {user_name} \n')
print('='* 50, '\n')

user_choice = str(input('Existují 3 texty, které lze analyzovat.\n\nVyberte prosím jednu z možostí 1 až 3: '))
print('='* 50, '\n')
if user_choice not in '0123456789':
    print('Zadaná hodnota musí být číslo!!!')
    exit()
    
elif user_choice == '1':
    print('Analýza textu č.1:')
    word_counter(TEXTS[0])
    pocet_velkych_pismen(TEXTS[0])
    pocet_malych_pismen(TEXTS[0])
    pocet_num(TEXTS[0])
    suma_num(TEXTS[0])
    print('='* 50)
    analyza_poctu_znaku(TEXTS[0])
    print('='* 50)
    
    
    
elif user_choice == '2':
    print('Analýza textu č.2:')
    word_counter(TEXTS[1])
    pocet_velkych_pismen(TEXTS[1])
    pocet_malych_pismen(TEXTS[1])
    pocet_num(TEXTS[1])
    suma_num(TEXTS[1])
    print('='* 50)
    analyza_poctu_znaku(TEXTS[1])
    print('='* 50)
    
    
elif user_choice == '3':
    print('Analýza textu č.3:')
    word_counter(TEXTS[2])
    pocet_velkych_pismen(TEXTS[2])
    pocet_malych_pismen(TEXTS[2])
    pocet_num(TEXTS[2])
    suma_num(TEXTS[2])
    print('='* 50)
    analyza_poctu_znaku(TEXTS[2])
    print('='* 50)
    
    
else: 
    print('Tento text neexistuje!!!')
    exit()
    

