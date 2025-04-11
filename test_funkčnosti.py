
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

first_text_to_sentences = TEXTS[0]
print("_"*200)
text_bez_tecek = first_text_to_sentences.replace(".","")
print("_"*200)
text_bez_carek = text_bez_tecek.replace(",","")
print("_"*200)

cisty_text = text_bez_carek.split()
print(cisty_text)

delka_slova = []
for i in cisty_text:
    delka_slova.append(int((len(i))))

delka_slova.sort()
print(delka_slova)

pocet_1 = 0
pocet_2 = 0
pocet_3 = 0
pocet_4 = 0
pocet_5 = 0
pocet_6 = 0
pocet_7 = 0
pocet_8 = 0
pocet_9 = 0
pocet_10 = 0
pocet_11 = 0
pocet_12 = 0
pocet_13 = 0
pocet_14 = 0
pocet_15 = 0


for i in delka_slova:
    if i == 1:
        pocet_1 +=1       
    elif i == 2:
        pocet_2 +=1
    elif i == 3:
        pocet_3 +=1
    elif i == 4:
        pocet_4 +=1
    elif i == 5:
        pocet_5 +=1
    elif i == 6:
        pocet_6 +=1
    elif i == 7:
        pocet_7 +=1
    elif i == 8:
        pocet_8 +=1
    elif i == 9:
        pocet_9 +=1
    elif i == 10:
        pocet_10 +=1
    elif i == 11:
        pocet_11 +=1
    elif i == 12:
        pocet_12 +=1
    elif i == 13:
        pocet_13 +=1
    elif i == 14:
        pocet_14 +=1
    elif i == 15:
        pocet_15 +=1
    else:
        break
    
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



    
  










        
        

    
    
    
    
       
        

    
    
    
    
        
       

