i=1
pomoc=""
pomoc2=""
while i!=0:
    numer=int(input("podaj numer :"))
    if numer==1:
        imie = input("podaj imie:")
        nazwisko = input("podaj nazwisko:")
        adres= input("podaj adres email:")
        wiek = input("podaj wiek uzytkownika:")
        pomoc2=pomoc2+" "+imie
    elif numer==2:
        imie1=input("podaj imie:")
        print(f"imie uzytokownika to {imie1}, wiek {wiek}, email {adres} \n")
        pomoc=pomoc+imie1+" "
    elif numer==3:
        print(f"Wszytkie imiona to {imie} {pomoc} \n")
    else:
        print("Program sie zakonczyl \n")
        i=0
