"""A felhasználótól addig kérje be a rendeléseket, amíg a @ jelet nem ütjük le!
Minden rendelés során a  program kérje be, hogy:
1.	sajtos, gombás, vagy sonkás pizzát kér-e?
2.	mekkora a pizza mérete:
        kicsi   -  ára az ár 90%-a
        normál  - ára az ár 100%-a
        nagy    – ára az ár 110%-a

3.	 kér e feltétet.

Alapárak:
A plusz feltét 50 Ft.
Normál sajtos pizza alapára 1000 Ft
Normál gombás pizza alapára 1100 Ft
Normál sonkás pizza alapára 1200 Ft


Tároljuk a felvett rendeléseket megfelelő listákba!  tipus, meret, feltet
Végezzük el minden rendelés esetében az ár kiszámítását is! esetleg ezt is tárolhatjuk egy listában! ar

A rendelések felvétele után készítsünk statisztikát!
1.	Melyik típusú (név alapján)  pizzából hány darab fogyott?
2.	Melyik pizzából fogyott a legtöbb?
3.	Mekkora volt a bevétel?
4.	Hányszor kértek extra feltétet?
5.	A kicsi, nagy , vagy a közepes pizzából rendeltek-e többet?
6.	… ami még eszetekbe jut.
"""
# listák a rendeléshez

tipus = []
meret = []
feltet = []
ar = []
# ár konstansok  beállítása
fajta=["","sajtos","gombás","sonkás"]
nagysag=["","kicsi","normál","nagy"]


#adatbekérés
def rendelesfelvetel():
    print("Add meg a pizza adatait!")
    tovabb=input("Akar új rendelést rögzíteni? i/n : ")
    while (tovabb=="i"):
        tip = beker("Válasszon pizzát: ", "1 - sajtos",  "2 - gombás", "3 - sonkás")
        tipus.append(fajta[tip])
        mer = beker("Válasszon méretet: ", "1 - kicsi", "2 - normál", "3 - nagy")
        meret.append(nagysag[tip])
        felt=feltetbeker()
        feltet.append(felt)
        ertek=arszamitas(tip, mer, felt)
        ar.append(ertek)
        tovabb = input("Akar új rendelést rögzíteni? i/n : ")
    #ciklus vége
    rendelesek_kiirasa()

def beker(cim, menu1, menu2, menu3):
    print("*"*20)
    print(f"*{menu1:<18}*")
    print(f"*{menu2:<18}*")
    print(f"*{menu3:<18}*")
    print("*"*20)

    adat = int(input(cim))
    while not (adat==1 or adat ==2 or adat ==3):
        adat = int(input("1, 2, 3 számokat adhat meg!"))
    return adat

def feltetbeker():
    felt= input("Kér extra feltétet? i/n :")
    return felt


def rendelesek_kiirasa():
    print("="*40)
    print(f"{'A felvett rendelések':^}")
    print("=" * 40)
    i=0
    while i < len(tipus):
        print(f"{i+1:>3}. {tipus[i]}, Méret: {meret[i]}, Extra feltét:  {feltet[i]}. Az ár: {ar[i]} Ft ")
        print("_"*40)
        i+=1
    statisztikak()

"""************************ STATISZTIKÁK **********************************"""
def statisztikak():
    fogyas_pizzatipus()
    fogyas_pizzatipus2()
    pizzafogyas()
    melyikbol_fogyott_legtobb()
    print(f"{osszbevetel()} Ft volt az összbevétel")
    print(f" {extrafeltet()} alkalommal kértek extra feltétet.")
    meretszerint()
def arszamitas(tip, mer, felt):
    sajtos_alap_ar = 1000
    gombas_alap_ar = 1100
    sonkas_alap_ar = 1200
    extraFeltet = 50
    kicsi = 0.9
    nagy = 1.1
    ar = 0
    if tip == "sajtos":
        ar = sajtos_alap_ar
    elif tip == "gombás":
        ar = gombas_alap_ar
    elif tip == "sonkás":
        ar = sonkas_alap_ar
    else:
        ar = sonkas_alap_ar

    #meret
    if mer == "kicsi":
        ar *= 0.9
    elif mer == "nagy":
        ar *= 1.1
    #extra feltét
    if felt=="i":
        ar+=extraFeltet
    return ar

"""
1.	Melyik típusú (név alapján)  pizzából hány darab fogyott?
"""
#####  1. megoldás
def fogyas_pizzatipus():
    sonkasDb=0
    sajtosDb=0
    gombasDb=0
    i=0

    while (i < len(tipus)):
        if (tipus[i] == "sajtos"):
            sajtosDb += 1
        elif (tipus[i] == "gombás"):
            gombasDb += 1
        else:
            sonkasDb += 1
        i+=1
    print(f"A fogyasztás: sajtos: {sajtosDb} sonkás: {sonkasDb} gombás: {gombasDb} ")


#####  2. megoldás
def fogyas_pizzatipus2():
    # Dictionarie-vel https://www.w3schools.com/python/python_dictionaries.asp
    # ez az adatszerkezet kulcs-érték párokból áll
    pizzarendelesek_osszegzese = {
        # 'kulcs': érték,
        # jelen esetben a kucsl a pizza neve, az érték, a belőle rendelt darabszám
        "sonkás": 0,
        "sajtos": 0,
        "gombás": 0
    }
    i = 0

    while (i < len(tipus)):
        kulcs=tipus[i] # ez mondja meg, hogy melyik típusú pizza , és a dic-ben ez melyik kulcs
        x = pizzarendelesek_osszegzese.get(kulcs) # lekérjük az adott típusú pizzához tartozó értéket
        pizzarendelesek_osszegzese.update({kulcs : x+1})  # hozzáadunk egyet a megfelelő kucslhoz tartozó értékhez
        i += 1
    print(f"A fogyasztás: sajtos: {pizzarendelesek_osszegzese.get('sajtos')} sonkás: {pizzarendelesek_osszegzese.get('sonkás')} gombás: {pizzarendelesek_osszegzese.get('gombás')} ")
#####  3. megoldás
def fogyas(tip):
    db = 0
    i = 0
    while (i < len(tipus)):
        if (tipus[i] == tip):
            db += 1
        i+=1
    return db

def pizzafogyas():
    sajtosDb= fogyas("sajtos")
    sonkasDb= fogyas("sonkás")
    gombasDb= fogyas("gombás")
    print(f"A fogyasztás: sajtos: {sajtosDb} sonkás: {sonkasDb} gombás: {gombasDb} ")
"""
2.	Melyik pizzából fogyott a legtöbb?
"""
"""felhasználjuk az előző feladat fogyas függvényét"""
def melyikbol_fogyott_legtobb():
    sajtosDb = fogyas("sajtos")
    sonkasDb = fogyas("sonkás")
    gombasDb = fogyas("gombás")
    max=sajtosDb
    max_nev="sajtos"
    if (sonkasDb > max):
        max=sonkasDb
        max_nev = "sonkás"
    if (gombasDb > max):
        max = gombasDb
        max_nev = "gombás"
    print(f"{max_nev} típusú pizzából fogyott a legtöbb.")

"""3.	Mekkora volt a bevétel?"""
def osszbevetel():
    ossz_ar = 0
    i = 0
    while (i < len(ar)):
        ossz_ar += ar[i]
        i += 1
    return ossz_ar
""" 4.	Hányszor kértek extra feltétet?"""
def extrafeltet():
    extraDb = 0
    i = 0
    while (i < len(feltet)):
        if (feltet[i] == "i"):
            extraDb += 1
        i += 1
    return extraDb
"""5.	A kicsi, nagy , vagy a közepes pizzából rendeltek-e többet?"""
def meret_fogyas(m):
    db = 0
    i = 0
    while (i < len(meret)):
        if (meret[i] == m):
            db += 1
        i+=1
    return db
def meretszerint():
        kicsiDb = meret_fogyas("kicsi")
        kozepesDb = meret_fogyas("normál")
        nagyDb = meret_fogyas("nagy")
        max = kicsiDb
        max_nev = "kicsi"
        if (kozepesDb > max):
            max = kozepesDb
            max_nev = "normál"
        if (nagyDb > max):
            max = nagyDb
            max_nev = "nagy"
        print(f"{max_nev} méretű pizzából fogyott a legtöbb.")
        #return max_nev

