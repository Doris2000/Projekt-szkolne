# - function to find youngest student from a set
students = [{"imie": "Tomek", "wiek": 20}, {"imie": "Karolina", "wiek": 18}]

def sort_item(item):
    return item["wiek"]

students.sort(key=sort_item)
print(students)
najmlodszy=list(filter(lambda item: item["wiek"]==18, students))
print(najmlodszy)

#zad 2
def ile_razy_zmiana(wartosc):
    ile=0
    for i in range(len(wartosc)-1):
        if wartosc[i]!=wartosc[i+1]:
            ile+=1
    return ile
with open("mecz.txt", "r") as file:
    results=file.readline()

print(ile_razy_zmiana(results))