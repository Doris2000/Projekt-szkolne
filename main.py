numbers=[3,7,9,12]
sum=0
first,second,thrid,fourth=numbers
sum=first+second+thrid+fourth

print(sum)


def smallest_numin_list (list):
    min=list[0]
    for i in list:
        if i<min:
            min=i
    return min

print(smallest_numin_list([1,9,8888]))

print(sorted(numbers,reverse=True))

items=[("b",1),
       ("c",7),
       ("b",134)]


items.sort(key=lambda item:item[1])
print(items)


students=[
    {"imie":"Jan","wiek":29},
    {"imie":"Janik","wiek":28},
    {"imie":"Jola","wiek":27}
]
students.sort(key=lambda student:student["wiek"])
print(students[0])

#mapa-zmiana elementu

items1=[
    ("Produkt1",10)

]
