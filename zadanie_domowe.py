baza_uzytkownikow=[]
isrunning=True
while isrunning==True:
    number=int(input("Menu: \n1. Dodaj użytkownika\n2. Zobacz dane użytkownika\n3. Wyświetl wszyskie imiona użytkowników\n"))
    if number==1:
        imie=input("podaj imie:\n")
        adres=input("podaj adres email:\n")
        wiek=input("podaj wiek uzytkownika:\n")
        user={"imie":imie,"adres":adres,"wiek":wiek}
        baza_uzytkownikow.append(user)
    elif number==2:
        imie2=input("podaj imie:\n")
        for osoba in baza_uzytkownikow:
            if osoba["imie"]==imie2:
                print(osoba)
            else:
                print("nie ma takiego uzytkownika")
    elif number==3:
        if len(baza_uzytkownikow)==0:
            print("brak uzytkownikow")
        for osoba in baza_uzytkownikow:
            print(osoba["imie"])
    elif number==4:
        isrunning=False
print(baza_uzytkownikow)
