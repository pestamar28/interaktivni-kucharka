"""
Modul recept.py definuje třídu Recept, která propojuje jednotlivé suroviny
a postup vaření do jednoho celku. Demonstruje princip kompozice – objekt Recept
v sobě uchovává objekty tříd Maso, Priloha, Koreni a Omacka.
"""

from models.suroviny import Maso, Priloha, Koreni, Omacka


class Recept:
    """Reprezentuje jeden kompletní recept včetně surovin, postupu a XP odměny."""

    def __init__(self, nazev, maso, priloha, koreni, omacka, postup, xp_odmena=50):
        self.nazev = nazev
        self.maso = maso        # Objekt třídy Maso
        self.priloha = priloha  # Objekt třídy Priloha
        self.koreni = koreni    # Objekt třídy Koreni
        self.omacka = omacka    # Objekt třídy Omacka
        self.postup = postup    # Seznam kroků
        self.xp_odmena = xp_odmena  # Odměna XP


    def ma_maso(self, hledane_maso):
        """Vrátí True, pokud recept obsahuje zadané maso, jinak False."""

        return self.maso.nazev == hledane_maso.strip().lower()

    def ma_prilohu(self, hledana_priloha):
        """Vrátí True, pokud recept obsahuje zadanou přílohu, jinak False."""
        return self.priloha.nazev == hledana_priloha.strip().lower()

    def ma_dochuceni(self, hledane_dochuceni):
        """Vrátí True, pokud se hledaný text shoduje s kořením NEBO omáčkou receptu."""
        hledane = hledane_dochuceni.strip().lower()
        return self.koreni.nazev == hledane or self.omacka.nazev == hledane

    def vypis_recept(self):
        """Přehledně vypíše celý recept, jeho suroviny a očíslovaný postup."""
        print(f"\n=== {self.nazev.upper()} ===")
        print(f"Odměna za uvaření: {self.xp_odmena} XP")
        print("\nPotřebné suroviny:")
        # Zde se automaticky zavolá metoda __str__ ze souboru suroviny.py
        print(f"  - Maso: {self.maso}")
        print(f"  - Příloha: {self.priloha}")
        print(f"  - Koření: {self.koreni}")
        print(f"  - Omáčka: {self.omacka}")

        print("\nPostup přípravy:")
        for cislo, krok in enumerate(self.postup, start=1):
            print(f" {cislo}. {krok}")
      
    def __str__(self):
        """Krátký jednořádkový popis receptu (hodí se pro seznamy v menu)."""
        return f"{self.nazev} ({self.maso.nazev}, {self.priloha.nazev}) - {self.xp_odmena} XP"


if __name__ == "__main__":

    kureci = Maso("kuřecí", 20)
    ryze = Priloha("rýže", True)
    kari = Koreni("kari", 2)
    smetana = Omacka("smetanová", "smetanový")

    postup_kari = [
        "Kuřecí maso nakrájej na kostičky, osol a zlehka opepři.",
        "Dej vařit rýži v osolené vodě podle návodu.",
        "Na pánvi rozpal olej, orestuj maso dozlatova a zasyp kari kořením.",
        "Zalij smetanovou omáčkou, povař 5 minut a podávej s rýží."
    ]


    recept_kari = Recept(
        nazev="Kuřecí na kari s rýží",
        maso=kureci,
        priloha=ryze,
        koreni=kari,
        omacka=smetana,
        postup=postup_kari,
        xp_odmena=50
    )

    print("Krátký náhled:", recept_kari)
    recept_kari.vypis_recept()

    print("\nTest vyhledávání (mělo by vypsat True, True, False):")
    print("Má kuřecí?", recept_kari.ma_maso("  Kuřecí "))
    print("Má rýži?", recept_kari.ma_prilohu("RÝŽE"))
    print("Má hovězí?", recept_kari.ma_maso("hovězí"))