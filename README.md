# Interaktivní lednice

## Základní popis projektu
Tento projekt je jednoduchá konzolová aplikace v Pythonu zaměřená na objektově orientované programování (OOP). Uživatel postupně zadává suroviny, které má doma (maso, přílohu, koření a omáčku), a program mu podle nich vybere vhodný recept. Za každé uvařené jídlo navíc získává body zkušeností (XP) a zvyšuje si úroveň kuchaře.

## Navigace v projektu
* `main.py` – Hlavní soubor, kterým se program spouští (obsahuje textové menu).
* `models/` – Složka pro třídy surovin, receptů a profilu uživatele.
* `engine/` – Složka pro logiku filtrování receptů a ukládání dat.
* `data/` – Složka pro uložené recepty a postup hráče.
* `tests/` – Složka pro základní automatické testy programu.

## Instalace
1. Nainstalujte si Python (verze 3.10 nebo novější) a Git.
2. Stáhněte si projekt z GitHubu příkazem v terminálu:
   ```bash
   git clone [https://github.com/pestamar28/interaktivni-kucharka.git](https://github.com/pestamar28/interaktivni-kucharka.git)
   ```
3. Otevřete staženou složku projektu:
   ```bash
   cd interaktivni-kucharka
   ```

## Spuštění
Program spustíte v terminálu ve složce projektu příkazem:
```bash
python main.py
```

Základní testy spustíte příkazem:
```bash
python -m unittest discover tests
```