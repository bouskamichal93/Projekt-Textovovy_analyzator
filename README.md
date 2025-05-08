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
- z knihovny collections je importován Counter() - pro počítání četností délky slov
- z importuje knihovnu string kvůli přípravě textu a ostranění diakritiky
- nejprve je použita fce "text_preparation" jejíž vstupní argument je string (text) a výstupní hodnota list (tento list je dále vstupním argumentem všech dalších fcí)- ze stringu odstraní všechny interpunkční znaménka a následně text rozseká na slova pomocí .split(), výsledný list je uložen do proměnné 'text_clear', kterou vrací fce

- následně je použita fce "text_analyse", vstupní argument je list - tato fce postupně pomocí for cyklu prochází list slov a :
            -  počítá délku listu - pomocí len(), tedy počet slov, které ukládá do proměnné 'word_count'
            -  pracuje s pomocnými proměnnými typu int 'upper_count' a 'only_upper_count', jejichž počáteční hodnoty jsou 0, a pokud je počáteční pismeno prvku velké inkrementuje hodnotu 'upper_count' o +1, to samé v případě 'only_upper_count' pokud je prvek listu .isupper()
            - pracuje s pomocnou proměnnou typu int 'count_lower', jejíž počáteční hodnota je rovna 0,  pokud je první znak prvku .islower() inkrementuje hodnotu 'pocet_malych' o +1
            -  pracuje s pomocnou proměnnou typu int 'count_numbers', jejíž počáteční hodnota je rovna 0,  a pokud je první znak prvku ve stringu isdigit() inkrementuje hodnotu 'count_numbers' o +1
            - pracuje s pomocnou proměnnou typu int 'sum_number' a typu list 'numeric_list', jejíž počáteční hodnota je rovna 0 a prázdnému listu, pokud je prvek .isdigit(), přidává tento prvek do prázdného listu 'numeric_list' jako int, následně dalším for cyklem postupně sčítá všechny prvky listu 'numeric_list' a ukládá je do proměnné 'sum_number'
            - pracuje s pomocnou proměnnou typu list 'word_len', jejiž počáteční hodnota je prázdný list, pomocí for cyklu je procházen vstupní argument a u každého prvku zjistí jeho délku pomocí (len()), tato délka je přidána jako prvek do listu 'word_len', v dalším kroku je list 'word_len' sortován pomocí .sort(), následně je sortovaný list předán fci 'Counter()' a uložen do proměnné 'numbers', proměnná 'numbers' je následně převedena na dictionary pomocí .dict(), kde key je délka slova a value je její četnost v analyzovaném textu, slovník 'numbers_dict' je následně procházen for cyklem, který vždy vytiskne key (délku slova), počet hvězdiček '*' charakterizující četnost délky slova a četnost délky slova.
  

      
