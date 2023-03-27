from pridam_pojisteneho_seznam_pojistencu import PridamVratimPojisteneho
from menu_seznam_pojistencu import Menu
from pojisteny_seznam_pojistencu import Pojisteny

pridam_pojisteneho = PridamVratimPojisteneho()

# cyklus pro menu
while True:
    print()
    print("--------------------")
    print("Evidence pojištěných")
    print("--------------------")
    print()
    print("Vyberte si akci:")
    print("1 - Přidat nového pojištěného")
    print("2 - Vypsat všechny pojištěné")
    print("3 - Vyhledat pojištěného")
    print("4 - Konec")

    
    while True:
        # vnitřní cyklus pro zapsání nového pojištěnce
        print()
        cislo_operace = input("Zadejte číslo operace: ")
        try:
            # zajištění, aby vstup byl číslo v rozmezí 1-4
            cislo_operace = int(cislo_operace)
        except ValueError:
            print("Číslo operace musí být číslo 1, 2, 3 nebo 4.")
            continue
        if cislo_operace not in range(1,5):
            print("Číslo operace musí být číslo 1, 2, 3 nebo 4.")
            continue
        print()
        break

    
    menu = Menu(cislo_operace)
    menu.rozcestnik()
   

    if menu.cislo_operace == 1:
        # akce pro načtení nového pojištěnce
        while True:
            # cyklus, aby bylo možné načíst více pojištěnců
            jmeno = input("Zadejte jméno klienta: ")
            prijmeni = input("Zadejte prijmeni klienta: ")
            vek = input("Zadejte věk klienta: ") 
            try:
                # zajištění, že věk bude celé číslo + systém se nezasekne, když tomu tak nebude
                vek = int(vek)
            except ValueError:
                print("Použij celé číslo.")
                continue              
            telefon = input("Zadejte telefon klienta: ")

            pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
            pridam_pojisteneho.pridej(pojisteny)
            print(pridam_pojisteneho)
            pokracovani = input("Přejete si pokračovat? (ano/ne): ")
            print()
            if pokracovani.lower() == "ne":
                # zastaví cyklus
                break
    
    if menu.cislo_operace == 2:
        # operace vypíše všechny pojištěné + číslování od 1                                                           
        vypis = [[p._jmeno, p._prijmeni, p._vek, p._telefonni_cislo] for p in pridam_pojisteneho.seznam_pojistencu]                 # seznam klientů
        for cislo, i in enumerate(pridam_pojisteneho.seznam_pojistencu, start=1):                           
            vypis_jmeno_prijmeni = "{0}. Jméno a příjmení: {1} {2}, {3} roků, tel.: {4}".format(cislo, i._jmeno, i._prijmeni, i._vek, i._telefonni_cislo)
            print(vypis_jmeno_prijmeni)
                    
    if menu.cislo_operace == 3:
        # systém najde pojištěnce podle jména a příjmení a vypíše ho
        zadej_jmeno = input("Zadej jméno vyhledávané osoby: ")
        zadej_prijmeni = input("Zadej příjmení vyhledávané osoby: ")
        print(pridam_pojisteneho)
        for pojisteny in pridam_pojisteneho.vrat():
            if pojisteny._jmeno == zadej_jmeno and pojisteny._prijmeni == zadej_prijmeni:
                vypis_jmeno_prijmeni = "{0} {1} {2}, {3}".format(pojisteny._jmeno, pojisteny._prijmeni, pojisteny._vek, pojisteny._telefonni_cislo)
                print(vypis_jmeno_prijmeni)
                break
        else:
            print("Klient nenalezen.")