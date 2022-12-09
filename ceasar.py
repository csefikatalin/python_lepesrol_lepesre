eredeti=["A","Á","B","C","D","E","É","F","G","H","I","Í","J","K","L","M","N","O","Ó","Ö","Ő","P","Q","R","S","T","U","Ú","Ü","Ű","V","W","X","Y","Z"]
eltolt=["X","Y","Z","A","Á","B","C","D","E","É","F","G","H","I","Í","J","K","L","M","N","O","Ó","Ö","Ő","P","Q","R","S","T","U","Ú","Ü","Ű","V","W"]


def titkosit():
    eredeti_szoveg = input("kérek egy szöveget: ").upper()
    titkositott_szoveg=""
    i = 0
    while i<len(eredeti_szoveg):
        kodolt_betu = betukeres(eredeti_szoveg[i])
        titkositott_szoveg += kodolt_betu
        i+=1

    print(titkositott_szoveg)


def betukeres(x):
    i=0
    while i<len(eredeti) and eredeti[i]!=x:
        i += 1
    return (eltolt[i])

