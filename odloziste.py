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

#znaky = dict()

#for index, symbol in enumerate(first_text):
#    znaky[index]= symbol

#print(znaky)

#pismena = [pismeno for pismeno in "Michal"] #comprehension
#print(pismena)

# dictionary comprehension
#druhe_mocniny = {cislo: cislo**2 for cislo in range(11)}
#print(f"Dict: {druhe_mocniny}")

# set comprehension
#jmena = {jmeno.title() for jmeno in "matous matous marek lukas jan jan".split()}
#print(f"Set: {jmena}")


mesta = {
    "Praha": 1_335_084, 
    "Brno": 382_405, 
    "Ostrava": 284_982,
    "Plzen": 175_219, 
    "Liberec": 104_261
}

# klasická smyčka 'for'
nad_sto_tisic_obyv = dict()

for mesto in mesta:
    if mesta[mesto] > 200_000:
        nad_sto_tisic_obyv[mesto] = mesta[mesto]
else:
    print(f"Klasicka smycka: {nad_sto_tisic_obyv}")

# dict comprehensions
nad_sto_tisic_obyv_compr = {
    mesto: mesta[mesto]
    for mesto in mesta
    if mesta[mesto] > 200_000
}
print(f"Dict comprehension: {nad_sto_tisic_obyv_compr}")