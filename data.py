ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
veta = "Michal je skvělý a úžasný."

mala_pismena_list = tuple(ascii_lowercase)
print(mala_pismena_list)

velka_pismena_list = tuple(ascii_uppercase)
print(velka_pismena_list)

veta_rozsekana = veta.replace(".", "")
veta_rozsekana_bez_tecek = veta_rozsekana.split()

velka = 0
mala = 0

for x in veta_rozsekana_bez_tecek:
    if x[0] in velka_pismena_list:
        velka += 1
    elif x[0] in mala_pismena_list:
        mala += 1

statistika = {
    'Počet slov s velkým písmenem:': velka,
    'Počet slov s malým písmenem:': mala,
    'Počet slov celkově:': len(veta_rozsekana_bez_tecek)
}

print(statistika)
