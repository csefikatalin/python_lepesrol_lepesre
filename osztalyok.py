from Szemely import Szemely

def kezd():
    """ adott személyekről tároljuk a nevüket, a nemüket és a születési évüket
    Ezt eddig 3 lista segítségével oldottuk meg, és azt mondtuk, hogy a listaelemek i. eleme összetartozik

    Ez nem annyira szerencsés megoldás, mert így nekünk kell fejben tartani ezt az információt.
    Sokkal jobb lenne, ha az összetartozó adatokat tudnánk egyben kezelni, egy egységbe zárni.
    Tehát pl. ilyen adatokat tárolok a személyekről.:
    szemely1 :
        neve: Zoli
        neme: férfi
        szul_ev: 1969

    szemely2 :
        neve: Jenő
        neme: férfi
        szul_ev: 1999

    szemely3 :
        neve: Jolán
        neme: nő
        szul_ev: 2000

    Ehhez létre  fogunk hozni egy sablont (modellt), ami alapján a konkrét szeméyleket le tudjuk gyártani.
    A sablon neve OSZTÁLY, és tartalmazni fogja azokat a jellemzőket, amik leírják az adott dolgot.
    Az osztályból létrehozott konkrét példányt OBJEKTUMNAk nevezzük.
    """

    # Az osztály példányosításakor adjuk meg a konkrét értékeket.
    szemely1=Szemely("Zoli","férfi",1969)
    szemely2=Szemely("Jenő","férfi",1999)
    szemely3=Szemely("Jolán","nő",2000)

    # Az adattagokat az objektumneve.adattagneve szintaktikával érhetjük el.
    print(szemely1._nev)
    szemely1.nev = "Zoltán"
    print(szemely1._nev)
    print(szemely2.nem)
    print(szemely3.szul_ido)

    # a __str__ metódus  az objektumról ad  információkat.
    print(szemely1)
    # az osztályok tartalmazhatnak tagfüggvényeket is, melyek az osztály adattagjain végeznek műveletet.
    print(f"{szemely1._nev} {szemely1.kor()} éves")

