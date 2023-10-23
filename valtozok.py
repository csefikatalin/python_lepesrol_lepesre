def kiiras():
    print("Az én nevem: Katalin")


def kiiras_nev():
    nev:  str = "Katalin"     # szöveges típus - str
    nev = nev + "valami"
    kor: int = 53.5          # szám típus - float
    magassag = 173      # szám - int
    ferfi = False       # logikai - bool
    print(f"Az én nevem: {nev} \n {kor} éves vagyok.")
    print(f"\t Magasságom: {magassag}")
    print(f"\t Férfi vagyok? : {ferfi}")

def muveletek_szovegekkel():
    szoveg="Az élet szép!"
    szoveg2="Főleg, ha programozunk!"
    szam = 2
    szov= szoveg + szoveg2
    print (szov)
    ujszov= szov + str(szam) +" - ban."
    print(ujszov)
    print(szoveg[0:7])
    print(szoveg.upper())
    print(szoveg.title())
    szam1 = "2"       #szövegként tárolt szám
    szam2 = 3         # számként tárolt szám
    #print(szam1 + szam2)        # hiba, mert két különböző típussal akarunk műveletet végrehajtani
    print(szam1 + str(szam2))   # szövegként fűzzük össze,  eredmény: "23"
    print(int(szam1) + szam2)   # számként adjuk össze,     eredmény: 5


def muveletekszovegekkel2():
    szoveg = "gipsz jakab"
    print(f"A szöveg hossza: {len(szoveg)}")
    print(f"Az első 'a' betű helye: {(szoveg.index('a'))}")
    keresztnev_elsobetu_helye = szoveg.index(" ")
    vezeteknev = szoveg[0:keresztnev_elsobetu_helye].title()
    keresztnev = szoveg[keresztnev_elsobetu_helye+1:len(szoveg)].title()
    monogram1 = vezeteknev[0:1].upper()
    monogram2 = keresztnev[0:1].upper()
    print(vezeteknev)
    print(keresztnev)
    print(monogram1 + monogram2)

import math
def muveletek_szamokkal():
    a = 12              #int
    b = 24              #int
    osszeg = a + b      #eredmény int
    kulonbség = a-b     #eredmény int
    hanyados = a / b    #eredmény float
    szorzat = a * b     #eredmény int
    hatvany = a ** 2    #eredmeny int
    gyok = a ** 0.5     #eredmény float
    gyok = math.sqrt(a) #eredmény float


    a = 12.456
    egeszresz = a // 1  # // hányszor van meg benne egész számszor az osztó - int
    maradek = a % 1     # az adott számmal osztva mennyi a maradék  float
    parose = a % 2      # Ha a kettővel való osztási maradék 0, akkor ps, különben ptlan a szám
    print(f"{a} szám egészrésze: {egeszresz}, a tört rész 2 tizedesre kerekítve: {maradek:.2f}")
    print(f"{a} szám kettővel való osztási maradéka 3 tizedesre kerekítve: {parose:.3f}")
    print(f"{13 } szám kettővel való osztási maradéka: {13 % 2}")


def adatbekeres():
    nev = input("Add meg a neved!")
    kor = input("Add meg a korod!")
    kor = int(kor) / 2
    print(f"A neved: {nev} \n {kor} éves vagy.")
