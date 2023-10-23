def egyszeru_elagazas():

    #adott egy szám, döntsük el róla, hogy páros, vagy páratlan?
    # Milyen számokkal tesztelnéd a programod?
    szam:int = 12
    # tesztesetek
    # szam -----  várt eredmény
    #  12      |      12 páros
    #  -12     |      -12 páros
    #  13      |      13 páratlan
    #  -13     |      -13 páratlan
    if szam % 2 == 0:
        print(f"{szam} páros.")

    else:
        print(f"{szam} páratlan.")
    #kérjünk be egy nevet és az illető nemét! Írjuk ki, hogy az adott nevű ember milyen nemű!
    nev:str = input("A neved:")
    neme:str = input("A nemed (f/n):")
    if neme == "f":
        print(f"{nev} férfi.")
    else:
        print(f"{nev} nő.")

def tobbszoros_elagazas_paritas():
    # adott egy szám, döntsük el róla, hogy pozitív, vagy negatív!
    # Milyen számokkal tesztelnéd a programod?
    # tesztesetek
    # szam -----  várt eredmény
    #  12      |      12 pozitív
    #  -13     |      -13 negatív
    #  0       |      A szám a nulla
    #  12.3    |      12.3 pozitív
    #  -13.45  |      -13.45 negatív

    szam:int = -12
    if szam > 0:
        print(f"{szam} pozitív.")
    elif szam==0:
        print(f"A szám  a  nulla.")
    else:
        print(f"{szam} negatív.")

def tobbszoros_elagazas_osztalyzat():
    """: A program olvasson be a konzolról egy egész számot!
    Ha a szám 0 és 100 közötti, akkor legyen a beolvasott szám egy százalékérték!
    A program írja ki a konzolra a százalékban megadott értékelést szövegesen
        0%–59%-ig elégtelen,
        60%–69%-ig elégséges,
        70%–79%-ig közepes,
        80%–89%-ig jó,
        90%–100%-ig jeles)!
    Ha a szám nem 0 és 100 közötti, akkor a program írja ki a konzolra, hogy „Hiba: érvénytelen százalék!”!
    """
    szam:int = int(input("Adj meg egy 0 ész 100 közötti számot! "))
    if szam <= 59 and szam >= 0:
        print(f"{szam} % - elégtelen")
    elif szam <= 69:
        print(f"{szam} % - elégséges")
    elif szam <= 79:
        print(f"{szam} % - közepes")
    elif szam <= 89:
        print(f"{szam} % - jó")
    elif szam <= 100:
        print(f"{szam} % - jeles")
    else:
        print(f"Hiba: érvénytelen százalék!")

def feltetelek_and():
    """13.	Adj meg három egész számot egy-egy változóba, melyek egy sorozat első három elemét jelentik.
    Írd ki a „növekvő” szót, ha a három szám növekvő sorrendben áll, és a „csökkenő” szót, ha csökkenőben!"""
    szam:int1 = 34
    szam2:int = 45
    szam3:int = 56
    # Milyen számokkal tesztelnéd a programod?
    # tesztesetek
    # szam1,szam2,szam3 -----  várt eredmény
    #  34,45,56      |      Növekvő sorrendv
    #  65,54,43      |      Csökkenő sorrend
    #  34,23,56      |      Rendezetlen sorozat
    if szam1 < szam2 and szam2 < szam3:
        print( f"{szam1}, {szam2}, {szam3} növekvő sorozat")
    elif szam3 < szam2 and szam2 < szam1:
        print(f"{szam1}, {szam2}, {szam3} csökkenő sorozat")
    else:
        print(f"{szam1}, {szam2}, {szam3} rendezetlen sorozat")

def feltetelek_or():
    """Kérj be egy egész számot, és írd ki, hogy osztható-e 3-mal vagy öttel!"""
    szam:int = int(input("Adj meg egy 0 ész 100 közötti számot! "))
    # Milyen számokkal tesztelnéd a programod?
    # tesztesetek
    # szam         -----  várt eredmény
    #  3             |      osztható 3-mal, vagy 5-tel
    #  5             |      osztható 3-mal, vagy 5-tel
    #  6             |      nem osztható sem 3-mal, sem 5-tel
    #  15            |      osztható 3-mal, vagy 5-tel
    if szam % 3 == 0 or  szam % 5 == 0:
        print( f"{szam}, osztható 3-mal, vagy 5-tel")
    else:
        print(f"{szam}, nem osztható sem 3-mal, sem 5-tel")


def egymasbaagyazott():
    """"
    Egy házaspárnak két gyereke van.
    A gyerek lehet édesgyerek, vagy mostoha, lány, vagy fiú. A program írja ki a négyféle lehetőséget a változók alapján:
     tipus : e - édes , m - mostoha
     nem : f - fiú, l - lány
    """
    tipus:str = "e"
    nem:str = "f"
    #tesztesetek
    #     tipus |  nem  |  várt eredmény
    #       e   |   f   |   Saját fiúgyermek.
    #       e   |   l   |   Saját leánygyermek.
    #       m   |   f   |   A házastárs fia.
    #       m   |   l   |   A házastárs lánya.
    #    bármi  |   f   |   A házastárs fia.
    #    bármi  |   l   |   A házastárs lánya.
    #       e   | bármi |   Saját leánygyermek.
    #       m   | bármi |   A házastárs lánya.
    if ( nem == "f"):
        if( tipus == "e"):
            print(" Saját fiúgyermek.")
        else:
            print(" A házastárs fia.")
    else:
        if (tipus == "e"):
            print(" Saját leánygyermek.")
        else:
            print(" A házastárs lánya.")


def pizza():
    """Készíts Pizza rendelő alkalmazást:
    A program kérje be, hogy sajtos, gombás, vagy sonkás pizzát kér-e?
    Kérje be a pizza méretét:
        kicsi   - az ára az ár 90%-a
        normál  - az ára az ár 100%-a
        nagy    – az ára az ár 110%-a

    Kérje be, hogy feltét kell-e?

    1.	Normál sajtos pizza alapára 1000 Ft
    2.	Normál gombás pizza alapára 1100Ft
    3.	Normál sonkás pizza alapára 1200 Ft

    Az extra feltét plusz 50 Ft-ba kerül. """

    """GONDOLD ÁT A TEZSTESETEKET! """
    # A változók kezdőértékének megadása - inicializálás *********************
    sajtos_alap_ar:int = 1000
    gombas_alap_ar:int = 1100
    sonkas_alap_ar:int = 1200
    # Adatok bekérése ********************************************************
    tipus:str = input("Válasszon pizzát 1 - sajtos / 2 - gombás / 3 - sonkás: ")

    meret:str = input("A pizza mérete (k)icsi/(n)normál/(o)óriás k/n/o: ")
    meret:str = meret[0:1].lower()
    feltet_kelle:str =  input("Kér extra feltétet? i/n: ")
    feltet_kelle:str = feltet_kelle[0:1].lower()

    szoveg= "A rendelt pizza: "
    ar = 0
    if tipus == "1":
        ar = sajtos_alap_ar
        szoveg += "sajtos pizza."
    elif tipus == "2":
        ar = gombas_alap_ar
        szoveg += "gombás pizza."
    elif tipus == "3":
        ar = sonkas_alap_ar
        szoveg += "sonkás pizza."
    else:
        ar = sonkas_alap_ar
        szoveg += "hibásan adta meg, ezért a legfinomabbat kapja!"

    if meret == "k":
        ar *= 0.9
        szoveg += " Kicsi méretben, "
    elif meret =="o":
        ar *= 1.1
        szoveg += "Óriás méretben, "
    else:
        szoveg += "Normál méretben, "

    if feltet_kelle == "i":
        ar += 50
        szoveg += "extra feltéttel."

    print(szoveg + " Fizetendő: " + str(ar) + " Ft." )


### bontsuk metódusokra!
def pizza2():
    """Készíts Pizza rendelő alkalmazást:
    A program kérje be, hogy sajtos, gombás, vagy sonkás pizzát kér-e?
    Kérje be a pizza méretét:
        kicsi   - az ára az ár 90%-a
        normál  - az ára az ár 100%-a
        nagy    – az ára az ár 110%-a

    Kérje be, hogy feltét kell-e?

    1.	Normál sajtos pizza alapára 1000 Ft
    2.	Normál gombás pizza alapára 1100Ft
    3.	Normál sonkás pizza alapára 1200 Ft

    Az extra feltét plusz 50 Ft-ba kerül. """

    # Adatok bekérése ********************************************************
    tipus:str = beker("Válasszon pizzát 1 - sajtos / 2 - gombás / 3 - sonkás: ")
    meret:str = beker("A pizza mérete (k)icsi/(n)normál/(o)óriás k/n/o: ")
    feltet_kelle:str = beker("Kér extra feltétet? i/n: ")

    # Ár számítása ********************************************************
    ar:int = tipus_ar(tipus)
    ar:int = meret_ar(meret, ar) + feltet_ar(feltet_kelle)
    # Kiírandó szöveg kialakítása ********************************************************
    minta("=", 100)
    szoveg:str = "A rendelt pizza: " + tipus_szoveg(tipus) + meret_szoveg(meret) + feltet_szoveg(feltet_kelle)
    print(szoveg + "fizetendő: " + str(ar))
    minta("=", 100)


def minta(jel:str, db:int):
    print(jel * db)

def beker(szoveg:str):
    minta("*", 100)
    sz = input(szoveg)

    return sz[0:1].lower()

def tipus_ar(tipus:str):
    # A változók kezdőértékének megadása - inicializálás *********************
    sajtos_alap_ar:int = 1000
    gombas_alap_ar:int = 1100
    sonkas_alap_ar:int = 1200
    ar = 0
    if tipus == "1":
        ar = sajtos_alap_ar
    elif tipus == "2":
        ar = gombas_alap_ar
    elif tipus == "3":
        ar = sonkas_alap_ar
    else:
        ar = sonkas_alap_ar
    return ar

def tipus_szoveg(tipus.str):
    szoveg = ""
    if tipus == "1":
        szoveg += "sajtos pizza."
    elif tipus == "2":
        szoveg += "gombás pizza."
    elif tipus == "3":
        szoveg += "sonkás pizza."
    else:
        szoveg += "hibásan adta meg, ezért a legfinomabbat kapja!"
    return szoveg


def meret_ar(meret:str, ar:int):
    if meret == "k":
        ar *= 0.9
    elif meret == "o":
        ar *= 1.1
    return ar

def meret_szoveg(meret:str):
    szoveg = ""
    if meret == "k":
        szoveg += " Kicsi méretben,  "
    elif meret == "o":
        szoveg += " Óriás méretben, "
    else:
        szoveg += " Normál méretben, "

    return szoveg

def feltet_szoveg(feltet_kelle:str):
    szoveg:str = ""
    if feltet_kelle == "i":
        szoveg += "extra feltéttel. "
    return szoveg

def feltet_ar(feltet_kelle:str):
    pluszar:int = 0
    if feltet_kelle == "i":
        pluszar = 50
    return pluszar