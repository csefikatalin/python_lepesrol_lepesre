def szamlalos():
    print("Írjuk ki a páros számokat 0 és 30 között! [0,30)")
    i:int = 0 # kell egy ciklusváltozó
    while i < 30: # eddig fut a ciklus
        print(i)
        i += 2 # a ciklusváltozó értékét meg kell változtatni

    print("Írjuk ki a számokat 30-tól 0-ig visszafelé! [30,0)")
    i:int = 30  # kell egy ciklusváltozó
    while i > 0:  # eddig fut a ciklus
        print(i)
        i -= 1  # a ciklusváltozó értékét meg kell változtatni



def ellenorzott_adatbekeres():
    # Kérjük be a felhasználótól az életkorát. Hibás érték esetén kérjük újra!
    #Az életkor 1 és 100 év között lehet.
    #Nem számlálós ciklus, ezért nem kell ciklusváltozó
    # Figyelni kell arra, hogy biztos kilépjünk a ciklusból helyes adat esetén.
    # A while feltételébe írt érték igaz, akkor végrehajtja a ciklusmag utasításait
    # Ha a feltétel hamis, akkor a ciklus után folytatja a program a futását.
    kor:int = int(input("Kérem adja meg a korát! [0,100]"))
    # while (kor < 1) or ( kor > 100):
    while not (kor >= 1  and  kor <= 100):
        kor = int(input("Nem jó adat, kérem adja meg újra! [0,100]"))
    # ciklus vége - akkor jutunk ide, ha a feltétel hamis lesz
    print(f"Az Ön kora: {kor} év!")

def adatbekeres():
    # Kérjük be a felhasználótól szavakat, addig, amíg a @ jelet nem üti le!
    #Nem számlálós ciklus, ezért nem kell ciklusváltozó
    # Figyelni kell arra, hogy biztos kilépjünk a ciklusból a megfelelő  adat esetén.
    # A while feltételébe írt érték igaz, akkor végrehajtja a ciklusmag utasításait
    # Ha a feltétel hamis, akkor a ciklus után folytatja a program a futását.
    szavak:str = (input("Kérem a szavakat! @-cal kilép..."))

    while not (szavak == "@"):
        print(szavak)
        szavak = (input("Kérem a szavakat! @-cal kilép..."))
    # ciklus vége - akkor jutunk ide, ha a feltétel hamis lesz



def megszamlalas():
    # Egy sorozatban adott tulajdonságú elemek száma
    # Számoljuk meg, hány 7-tel osztható szám van [0, 100] intervallumban!
    i:int = 0 # ciklusváltozó
    db:int = 0 # gyűjtóváltozó
    while i <= 100:
        if ( i % 7 == 0):
            db += 1 # gyűjtőváltozó értékét változtatom
        # elágazás vége
        i += 1 # ciklusváltozó értékét növelem
    # ciklus vége
    print(f"[0, 100] intervallumban {db } db 7-tel osztható szám van!")


def osszegzes():
    # Egy sorozatban adott tulajdonságú elemek számát, átlagát szorzatát, stb.. határozzuk meg
    # Mekkora a számok összege a [0, 100] intervallumban!
    i:int = 0 # ciklusváltozó
    ossz:int = 0 # gyűjtóváltozó
    while i <= 100:
        ossz += i # gyűjtőváltozó értékét változtatom a ciklusváltozó értékével
        i += 1 # ciklusváltozó értékét növelem
    # ciklus vége
    print(f"[0, 100] intervallumban  a számok összege: {ossz } ")

import random
def maximumkivalasztas():
    # Egy sorozatban a legnagyobb/legkisebb értékű elemet, vagy annak helyét határozzuk meg
    # Generáljunk 10 db véletlen számot a [1,90] intervallumban. Mekkora volt a legnagyobb szám?
    # Hányadik lépésben generáltuk a legnagyobb számot?
    i = 1 # ciklusváltozó
    max_ertek:int = 0 # gyűjtóváltozó
    max_hely:int = 0
    while i <= 10:
        vel:int = int(random.random() * 89) + 1
        print(vel)
        if (vel >max_ertek):
           max_ertek = vel
           max_hely = i
        #elágazás vége
        i += 1 # ciklusváltozó értékét növelem
    # ciklus vége
    print(f"[1, 90] intervallumban  a generált legnagyobb szám: {max_ertek }, a helye: {max_hely}")

def eldontes():
    # Van- e a sorozatban adott tulajdonságú elem?
    # Generáljunk 5 db véletlen számot a [1,90] intervallumban. Van-e köztük páros?
    # Pontosabban: Most addig generáljuk a számokat, amíg párost nem kapunk, d legfeljebb öt számot generáljunk!
    i:int = 1 # ciklusváltozó
    vel:int = int(random.random() * 89) + 1
    while i <= 5 and vel % 2 == 1: #fontos, hogy először a ciklusváltozót vizsgáljuk és csak utána a paritást
        print(vel)
        vel = int(random.random() * 89) + 1
        i += 1 # ciklusváltozó értékét növelem
    # ciklus vége
    if ( i<5 ):
        print(f"Van páros szám, az { i}. helyen.")
    else:
        print("Nincs páros szám!")



def szorzotabla():
    #Írjuk ki a szorzótáblát a képernyőre!
    i:int = 1  # külső ciklusváltozó
    while i <= 10:
        j = 1 # belső  ciklusváltozó
        sor = "" # Itt fogom tárolni egy sor számait!
        while j <= 10:
            sor += f"{i*j:>4}"
            j += 1 # belső ciklusváltozó növelése
        # belső ciklus vége
        print(sor)
        i += 1 # külső ciklusváltpzó növelése
    #külső ciklus vége




