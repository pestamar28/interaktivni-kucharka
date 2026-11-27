"""
Modul obsahuje třídy pro jednotlivé suroviny v aplikaci Interaktivní lednice.
Ukazuje princip dědičnosti: všechny konkrétní suroviny dědí ze třídy Surovina.
"""


class Surovina:
    """Základní (rodičovská) třída pro každou surovinu v lednici."""

    def __init__(self, nazev):
        # Název rovnou očistíme od mezer a převedeme na malá písmena,
        # aby při pozdějším hledání nevadil rozdíl mezi 'Kuřecí' a 'kuřecí'.
        self.nazev = nazev.strip().lower()

    def __str__(self):
        """Určuje, jak se surovina vypíše při použití funkce print()."""
        return self.nazev


class Maso(Surovina):
    """Dědí ze třídy Surovina a přidává dobu tepelné úpravy v minutách."""

    def __init__(self, nazev, doba_pripravy):
        super().__init__(nazev)          # Název předáme rodičovské třídě Surovina
        self.doba_pripravy = doba_pripravy

    def __str__(self):
        return f"{self.nazev} (příprava cca {self.doba_pripravy} min)"


class Priloha(Surovina):
    """Dědí ze třídy Surovina a přidává informaci, zda je bezlepková."""

    def __init__(self, nazev, bezlepkova=True):
        super().__init__(nazev)
        self.bezlepkova = bezlepkova

    def __str__(self):
        # Podmínka vybere text podle toho, jestli je self.bezlepkova True nebo False
        if self.bezlepkova:
            return f"{self.nazev} (bezlepková)"
        else:
            return f"{self.nazev} (obsahuje lepek)"


class Koreni(Surovina):
    """Dědí ze třídy Surovina a přidává míru pálivosti na škále 1 až 5."""

    def __init__(self, nazev, palivost=0):
       """Dědí ze třídy Surovina a přidává míru pálivosti na škále 1 až 5."""

    def __init__(self, nazev, palivost=0):
        super().__init__(nazev)
        self.palivost = palivost
    def __str__(self):
        return f"{self.nazev} (pálivost {self.palivost}/5)"

class Omacka(Surovina):
    """Dědí ze třídy Surovina a přidává základ omáčky."""

    def __init__(self, nazev, zaklad):
        super().__init__(nazev)
        self.zaklad = zaklad

    def __str__(self):
        return f"{self.nazev} (základ: {self.zaklad})"



# V __init__ přijme (self, nazev, zaklad) - např. zaklad="smetanový" nebo "sójový".
# V metodě __str__ vrať text ve tvaru: f"{self.nazev} (základ: {self.zaklad})"


# --- RYCHLÁ ZKOUŠKA TOHOTO SOUBORU ---
# Tento kód se spustí jen tehdy, když pustíš přímo soubor suroviny.py
if __name__ == "__main__":
    kureci = Maso("Kuřecí prsa", 20)
    ryze = Priloha("Rýže", True)
    testoviny = Priloha("Těstoviny", False)
    kari = Koreni("Kari", 1)
    smetana = Omacka("Smetanová omáčka", "smetanový")

    print("Test vytvořených surovin:")
    print("-", kureci)
    print("-", ryze)
    print("-", testoviny)
    print("-", kari)
    print("-", smetana)