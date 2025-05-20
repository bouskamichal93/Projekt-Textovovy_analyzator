"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Michal Bouška
email: michal.bouska93@gmail.com
"""
import string
from collections import Counter
   
def text_preparation(text:str) -> list:   
    """Vrací list slov z textu bez diakritiky"""
    translator = str.maketrans('', '', string.punctuation)
    text_without_punctuation = text.translate(translator)
    text_clear = text_without_punctuation.split() #rozbije text na list slov
    return text_clear
 
def text_analyse(text:list) -> int:
    """Vrací celkový počet slov, počet slov začínajících velkým písmenem, počet slov pouze s velkými písmeny, počet slov s malými písmeny, počet numerických stringů, součet všech čísel v textu a jednoduchý graf zobrazující četnost délek slov."""
    #počet slov 
    word_count = len(text)
    #velká písmena
    upper_count = 0
    only_upper_count = 0
    #malá písmena
    count_lower = 0
    #čísla
    count_numbers = 0
    sum_number = 0
    numeric_list = []
    #analýza slov
    word_len = [] #prázdný list do kterého se bude ukládat délka jednotlivých slov
         
    for x in text: 
        b=x[0] # první znak stringu
        if b.isupper():
            upper_count += 1
        if x.isupper():
            only_upper_count += 1 
        if x.islower():
            count_lower+=1
        if x.isdigit():
            count_numbers+=1
            numeric_list.append(int(x)) 
        word_len.append(int((len(x)))) #zjistí délku slova a přidá jí do listu word_len
            
    for y in numeric_list:
        sum_number+= y
        
        word_len.sort() #seřadí naplněný list podle velikosti
        numbers = Counter(word_len)
        numbers_dict = dict(numbers)
        
    print(f'Ve vybraném textu je {word_count} slov')
    print(f'Počet slov začínajících velkým písmenem: {upper_count-only_upper_count}')
    print(f'Počet slov obsahujících pouze velká písmena: {only_upper_count}') 
    print(f'Počet slov začínajících malým písmenem: {count_lower}')
    print(f'Počet numerických stringů: {count_numbers}')
    print(f'Suma všech čísel obsažených v textu: {sum_number}')
    print('='* 50)
    print ('DÉLKA SLOVA', 'VÝSKYT', 'POČET', sep='   |   ')
    for x, y in numbers_dict.items():
        if x <10:
            print(x,format('*'* y, ' <25'), y, sep=' |')
        else:
            print(x,format('*'* y, ' <26'), y, sep='|')
    print('='* 50)

#DATA
# #registrovaní uživatelé
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


dict_of_texts = dict()
cisla_textu = [str(TEXTS.index(i)+1) for i in TEXTS]      
dict_of_texts = {k:TEXTS.index(v) for (k,v) in zip(cisla_textu, TEXTS)}

if __name__ == "__main__":
    #KONTROLA REGISTROVANÉHO UŽIVATELE   
    user_names = users_registered.keys()
    '''uložení uživatelských jmen do listu jménem user_names pro následnou kontrolu,
    že se nacházejí v dictionary users_registered'''
    user_name = str(input('Zadejte uživatelské jméno: '))
    for x in user_names: 
        if x in user_name:
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
    list_of_text_numbers = list(dict_of_texts.keys())
    user_choice = input(f'Počet textů, které lze analyzovat: {list_of_text_numbers[-1]}\n\n Vyberte prosím jednu z možností 1 až {list_of_text_numbers[-1]}: ')
    print('='* 50)
    if not user_choice.isdigit():
        print('Zadaná hodnota musí být číslo!!!')
        exit()
    elif user_choice.isdigit() and user_choice not in dict_of_texts.keys():
        print(f'Text číslo {user_choice} neexistuje!!!')
        exit()
    else:
        for x,y in dict_of_texts.items():
            if x == user_choice:
                print(f'Analýza textu č.{x}')
                text_analyse(text_preparation(TEXTS[y]))
                
       


        
        

