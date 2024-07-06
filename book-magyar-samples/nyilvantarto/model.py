"""A nyilvántartó modelje

Ezek az osztályok képzik az üzleti modeljét a nyilvántartónak, 
amiből fel tudunk építeni egy rendelés leírását.

  Tipikus használati példa:

  termek = Termek('T1', 'Egy termék', 100)
  termek.learaz(10)
"""
from typing import List
from dataclasses import dataclass, field


@dataclass
class Termek:
    """Terméket reprezentáló osztály

    Attributes:
        kod: a terméket azonósító kód
        nev: a termék neve
        ar: a termék ára
        regi_ar: a termék korábbi ára
    """

    kod: str
    nev: str
    ar: int  # pylint: disable=invalid-name
    regi_ar: int

    def __init__(self, kod: str, nev: str, ar: int) -> None:
        self.kod = kod
        self.nev = nev
        self.ar = ar
        self.regi_ar = ar

    def learaz(self, szazalek: int) -> None:
        """A termék árát csökkenti a megdott százalékkal

        Params:
            szazalek: a csökkentés mértéke
        """
        self.regi_ar = self.ar
        uj_ar = self.ar * (1 - szazalek / 100)
        self.ar = round(uj_ar)

    def __str__(self):
        return (
            f'{self.nev} ({self.kod}): '
            + f'{self.regi_ar}=>{self.ar}'
        )

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.kod == other.kod
        raise NotImplementedError()
@dataclass(frozen=True)
class Cim:
    """Címet reprezentáló osztály

    Attributes:
        irszam: irányítószám
        varos: város
        cim: cím (utca, házszám stb.)
        orszag: ország
    """

    irszam: int
    varos: str
    cim: str
    orszag: str = field(default='HUNGARY')

    @property
    def teljes_cim(self):
        """ A cím nyomtatható módon formázva"""
        return (
            f'{self.irszam} {self.varos}, '
            + f'{self.cim}, {self.orszag}'
        )


@dataclass
class Megrendelo:
    """ A megrendelőt reprezentélja
    
    A szállítási és számlázási cím megegyezhet.

    Attributes:
        nev: név
        email: e-mail
        telefon: telefonszám
        szamlazasi_cim: számlázási cím
        szallitasi_cim: szállítási cím       
    """

    nev: str
    email: str
    telefon: str
    szamlazasi_cim: Cim
    szallitasi_cim: Cim

    def __init__(self, nev, email, telefon,
        szamlazasi_cim, szallitasi_cim=None):
        self.nev = nev
        self.email = email
        self.telefon = telefon
        self.szamlazasi_cim = szamlazasi_cim
        self.szallitasi_cim = (
            szallitasi_cim
            if szallitasi_cim is not None
            else szamlazasi_cim
        )
class Rendeles:
    """Rendelés adatai és állapota 
    
    A termékek listában a termékek ismétlődhetnek a tételekben
    """

    @dataclass
    class Tetel:
        """Terméket és darabszámot együtt tároló osztály"""
        termek: str
        darab: int

    _termekek: List[Tetel]
    _megrendelo: Megrendelo
    _allapot: str
    LETREHOZVA = 'LETREHOZVA'
    POSTAZHATO = 'POSTAZHATO'
    ELKULDVE = 'ELKULDVE'

    def __init__(self, termekek: List[Tetel], 
                 megrendelo: Megrendelo) -> None:
        """Létrehozva állapotba kerül a rendelés"""
        self._termekek = termekek
        self._megrendelo = megrendelo
        self._allapot = self.LETREHOZVA

    @property
    def megrendelo(self) -> Megrendelo:
        """A megrendelő"""
        return self._megrendelo

    @megrendelo.setter
    def megrendelo(self, val):
        if self._allapot == self.LETREHOZVA:
            self._megrendelo = val
        else:
            raise ValueError('Már nem módosítható')

    @property
    def termekek(self) -> List['Rendeles.Tetel']:
        """A megrendelővel"""
        return self._termekek.copy()

    @termekek.setter
    def termekek(self, val: List['Rendeles.Tetel']) -> None:
        if self._allapot == self.LETREHOZVA:
            self._termekek = val
        else:
            raise ValueError('Már nem módosítható')

    def veglegesit(self) -> None:
        """A megrendelést leadja a megrendelő"""
        if self._allapot == self.LETREHOZVA:
            self._allapot = self.POSTAZHATO
        else:
            raise ValueError('Nem megfelelő állapot')
    def elpostazva(self) -> None:
        """A megrendelés postázásra került"""
        if self._allapot == self.POSTAZHATO:
            self._allapot = self.ELKULDVE
        else:
            raise ValueError('Nem megfelelő állapot')
