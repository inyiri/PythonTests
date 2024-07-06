"""Demo"""
from typing import Dict, Optional
from nyilvantarto.model import Termek

termekek: Dict[str, Termek] = {}


def termek_listazas() -> None:
    """A termékeket listázó menüpont"""
    if len(termekek) == 0:
        print('Nincs termék még megadva')
    for kod, termek in termekek.items():
        print(f'{kod}: {termek}')


def termek_hozzaadas() -> None:
    """A terméket hozzáadó menüpont"""
    termek = termek_beolvas()
    if termek is not None:
        modositas = termek.kod in termekek
        termekek[termek.kod] = termek
        print('Új termék hozzáadva.'
              if not modositas
              else 'Termék módosítva.')
    else:
        print('Termék adatai hibásak!')


def termek_torles() -> None:
    """A terméket törlő menüpont"""
    termek_kod = input('Kérem a törlendő kódot: ')
    if termek_kod in termekek:
        del termekek[termek_kod]
        print('Sikeresen törölve')
    else:
        print('Nem létező kód!')


def termek_beolvas() -> Optional[Termek]:
    """Beolvas a billentyűzetről egy
    terméket"""
    while True:
        kod: str = input('Termék kódja: ')
        nev: str = input('Termék neve: ')
        try:
            ar: int = int(
                input('Ára: ')
            )  # pylint: disable=invalid-name
        except ValueError:
            print('Ár csak egész szám lehet!')
            return None
        return Termek(kod, nev, ar)


def main_menu():
    """A főmenü"""
    kilepes = False
    while not kilepes:
        print(
            'A: listázás',
            'B: hozzáadás',
            'C: törlés',
            'Q: kilépés',
            sep=', ',
        )
        menu = input(
            'Kérem adja meg a menűpont betűjét majd üssön enter-t: '
        )
        menu_kod = menu.strip().upper()
        if menu_kod == 'A':
            termek_listazas()
        elif menu_kod == 'B':
            termek_hozzaadas()
        elif menu_kod == 'C':
            termek_torles()
        elif menu_kod == 'Q':
            return
        else:
            print('Nem értelmezhető választás')


if __name__ == '__main__':
    main_menu()
