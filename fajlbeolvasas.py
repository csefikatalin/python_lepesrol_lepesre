nevek=[]
korok = []
nemek = []

def beolvas():
    print(f_beolvas("teszt.txt"))


def f_beolvas(fajlnev):
    fajlom = open(fajlnev, "r", encoding='utf-8')
    """ez a fejléc"""
    fajlom.readline()
    fajl_tartalom=fajlom.readlines()
    fajlom.close()
    feldolgoz(fajl_tartalom)

def feldolgoz(fajl_tartalom):
    i=0
    while i<len(fajl_tartalom):
        sor=fajl_tartalom[i].strip().split(',')
        nevek.append(sor[0])
        nemek.append(sor[1])
        korok.append(sor[2])

        i+=1
    #ciklus vége
    print(nevek)
    print(korok)
    print(nemek)





