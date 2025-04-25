"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Michal Bouška
email: michal.bouska93@gmail.com
"""
import string
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

#FCE
#příprava textu
def text_preparation(text:str) -> list:
    translator = str.maketrans('', '', string.punctuation)
    text_without_punctuation = text.translate(translator)
    text_clear = text_without_punctuation.split() #rozbije text na list slov
    return text_clear

#počítání slov
def word_counting(text:list) -> int: 
    word_count = len(text)
    print(f'Ve vybraném textu je {word_count} slov')
     
#počítání slov s velkým písmenem   
def count_of_uppercase_word(text:list) -> int:
    upper_count = 0
    only_upper_count = 0 
    for x in text: 
        b=x[0] # první znak stringu
        if b.isupper():
            upper_count += 1
        if x.isupper():
            only_upper_count += 1  
    print(f'Počet slov začínajících velkým písmenem: {upper_count-only_upper_count}')
    print(f'Počet slov obsahujících pouze velká písmena: {only_upper_count}') 
      
#počítání slov s malým písmenem   
def count_of_lowercase_word(text: list) -> int:  
    count_lower = 0
    for x in text: 
        if x.islower():
            count_lower+=1
    print(f'Počet slov začínajících malým písmenem: {count_lower}')
    
#analýza čísel
def digits_analyse(text:list) -> int:  
    count_numbers = 0
    sum_number = 0
    numeric_list = []
    for x in text: 
        if x.isdigit():
            count_numbers+=1
            numeric_list.append(int(x)) 
    for y in numeric_list:
        sum_number+= y
    print(f'Počet numerických stringů: {count_numbers}')
    print(f'Suma všech čísel obsažených v textu: {sum_number}')
    
#analýza slov
def word_analyse(text:list) -> dict:
    word_len = [] #prázdný list do kterého se bude ukládat délka jednotlivých slov
    for x in text: 
        word_len.append(int((len(x)))) #zjistí délku slova a přidá jí do listu word_len
    word_len.sort() #seřadí naplněný list podle velikosti
    numbers = Counter(word_len)
    numbers_dict = dict(numbers)        
    print ('DÉLKA SLOVA', 'VÝSKYT', 'POČET', sep='   |   ')
    for x, y in numbers_dict.items():
        if x <10:
            print(x,format('*'* y, ' <25'), y, sep=' |')
        else:
            print(x,format('*'* y, ' <26'), y, sep='|')
            
#kompletní analýza    
def analyse(text:list) -> string:
    word_counting(text_preparation(text))
    count_of_uppercase_word(text_preparation(text))
    count_of_lowercase_word(text_preparation(text))
    digits_analyse(text_preparation(text))
    print('='* 50)
    word_analyse(text_preparation(text))
    print('='* 50)

#KONTROLA REGISTROVANÉHO UŽIVATELE   
user_names = users_registered.keys()
'''uložení uživatelských jmen do listu jménem user_names pro následnou kontrolu,
že se nacházejí v dictionary users_registered'''
user_name = str(input('Zadejte uživatelské jméno: '))
for x in user_names: 
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

print('='* 50)
print(f'Aplikace Textový analizátor vítá uživatele {user_name}')
print('='* 50)

#KONTROLA UŽIVATELSKÉ VOLBY
user_choice = str(input('Existují 3 texty, které lze analyzovat.\n\nVyberte prosím jednu z možností 1 až 3: '))
print('='* 50)

if not user_choice.isdigit():
    print('Zadaná hodnota musí být číslo!!!')
    exit()
    
elif user_choice.isdigit() and user_choice not in '123':
    print(f'Text číslo {user_choice} neexistuje!!!')
    exit()
        
elif user_choice == '1':
    print('Analýza textu č.1:')
    analyse(TEXTS[0])
        
elif user_choice == '2':
    print('Analýza textu č.2:')
    analyse(TEXTS[1])
    
elif user_choice == '3':
    print('Analýza textu č.3:')
    analyse(TEXTS[2])
    

    
    

