import datetime
class Szemely: #Az osztály neve. Szokás nagybetűvel kezdeni
    _nev = ""
    def __init__(self, nev, nem, szul_ido):
        # konstruktor. Feladata, hogy beállítsa az adattagok alapértékét
        # az osztály példányosításakor hívódik meg.
        # self a konkrét sztálypéldányra mutat, azaz az objektumra
        self._nev = nev #adattag
        self.nem = nem #adattag
        self.szul_ido = szul_ido #adattag

    #tagfüggvény - az osztály adattagjain végez műveleteket.
    """metódusok lekérdezik és beállítják az adattagokat. 
    Az objektum viselkedését definiálják, mindezt ellenőrzött körülmények között, 
    azaz az osztály kívülről zárt marad, kívülről csak a meghatározott módokon férünk hozzá. """
    def kor(self):
        x = datetime.datetime.now()
        #Visszaadja a személy korát
        return x.year - self.szul_ido

    # ez a metódus hívódik meg a print utasításra. Itt írhatunk ki infókat az osztálypéldányról.
    def __str__(self):
        return f"{self._nev}({self.nem}, {self.szul_ido})"