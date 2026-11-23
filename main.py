
# Program se nejdříve zeptá na jméno uživatele a pozdraví ho
jmeno = input("Jak se jmenuješ? ").strip()
print("Vítej v kuchyni,", jmeno)

# Nekonečná smyčka zobrazuje menu pořád dokola, dokud uživatel nezadá 4
while True:
    print("\n=== INTERAKTIVNÍ LEDNICE ===")
    print("1. Chci vařit (výběr surovin)")
    print("2. Můj profil kuchaře (XP a úroveň)")
    print("3. Přidat vlastní recept")
    print("4. Ukončit program")

    # Načtení volby od uživatele a odstranění případných mezer navíc
    volba = input("Vyber číslo (1-4): ").strip()

    if volba == "1":
        print("Výběr surovin doděláme v dalším kroku.")
    elif volba == "2":
        print("Profil kuchaře a XP doděláme v dalším kroku.")
    elif volba == "3":
        print("Přidávání vlastních receptů doděláme v dalším kroku.")
    elif volba == "4":
        print("Lednice se zavírá. Dobrou chuť!")
        break  # Ukončí smyčku a vypne program
    else:
        print("Neplatná volba, napiš prosím číslo od 1 do 4.")