author: Michal Bouška
email: michal.bouska93@gmail.com

Toto je oficiální dokumentace k projektu č. 1 - Engeto - Textový analyzátor.

Co program umí:
- ověřit a přihlásit uživatele po zadání už. jména a hesla, pokud je registrovaný
- analyzovat konkrétní text(string), tedy:
      - spočítat slova v textu
      - spočítat slova začínající velkým písmenem
      - spočítat slova obsahující pouze velká písmena
      - spočítat slova začínající malým písmenem
      - spočítat numerické stringy
      - sečíst dohromadyvšechny numerické stringy
      - spočítat délku jednotlivých slov a vypsat jejich četnosti v jednoduchém grafu

Jak program pracuje při analýze textu:
- z knihovny collections je importován Counter - pro počítání četností délky slov
- z importuje knihovnu string kvůli přípravě textu
- nejprve je použita fce "text_priprava" jejíž vstupní argument je string (text) a výstupní hodnota list (tento list je dále vstupním argumentem všech dalších fcí)- ze stringu odstraní všechny
  interpunkční znaménka a následně text rozseká na slova pomocí .split(), výsledný list je uložen do proměnné 'cisty_text', kterou vrací fce
- další fce užité v programu:
- "pocitani_slov" - vstupní argument je list - počítá délku listu - pomocí len(), tedy počet slov, které ukládá do proměnné 'pocet_slov'
- "pocet_velkych_pismen" - vstupní argument je list - pracuje s pomocnými proměnnými typu int 'pocet_velkych' a 'pouze_velka_pismena', jejichž počáteční hodnoty jsou 0, pomocí for cyklu prochází list a pokud je počáteční pismeno prvku ve stringu 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' inkrementuje hodnotu 'pocet_velkych' o +1, to samé v případě 'pouze_velka_pismena' - zde ale pokud je prvek listu .isupper()
- "pocet_malych_pismen" - vstupní argument je list, pracuje s pomocnou proměnnou typu int 'pocet_malych', jejíž počáteční hodnota je rovna 0, pomocí for cyklu prochází list a pokud je první znak prvku ve stringu 'abcdefghijklmnopqrstuvwxyz' inkrementuje hodnotu 'pocet_malych' o +1
- "pocet_num" - vstupní argument je list, pracuje s pomocnou proměnnou typuu int 'pocet_num', jejíž počáteční hodnota je rovna 0, pomocí for cyklu prochází list a pokud je první znak prvku ve stringu '0123456789' inkrementuje hodnotu 'pocet_num' o +1
- "suma_num" - vstupní argument je list, pracuje s pomocnou proměnnou typu int 'suma_cisel' a typu list 'numeric_list', jejíž počáteční hodnota je rovna 0 a prázdnému listu, pomocí for cyklu prochází list a pokud je první znak prvku ve stringu '0123456789', přidává tento prvek do prázdného listu 'numeric_list' jako int, následně dalším for cyklem postupně sčítá všechny prvky listu 'numeric_list' a ukládá je do proměnné 'suma_cisel'
- "analyza_poctu_znaku" - vstupní argument je list, pracuje s pomocnou proměnnou typu list 'delka_slova', jejiž počáteční hodnota je prázdný list, pomocí for cyklu je procházen vstupní argument a u každého prvku zjistí jeho délku pomocí (len()), tato délka je přidána jako prvek do listu 'delka_slova', v dalším kroku je list 'delka_slova' sortován pomocí .sort(), následně je sortovaný list předán fci 'Counter()' a uložen do proměnné 'hodnoty', proměnná 'hodnoty' je následně převedena na dictionary pomocí .dict(), kde key je délka slova a value je její četnost v analyzovaném textu, slovník 'hodnoty_dict' je následně procházen for cyklem, který vždy vytiskne key (délku slova), počet hvězdiček '*' charakterizující četnost délky slova a četnost délky slova.
  

      
