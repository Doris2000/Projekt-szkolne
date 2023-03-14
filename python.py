ile=0
for i in range(1,11):
    if i%2==0:
        ile += 1
        print(i)
print(f"Jest tyle tych parzystych {ile} \n")


def fiz():
    liczby=""
    for i in range(0,101):
        if i%3==0 and i%5==0:
            liczby+="fizzbuzz \n"
        elif i%3==0:
            liczby+="buzz \n"
        elif i%5==0:
            liczby+="fizz \n"
        else:
            liczby+=str(i)
            liczby+="\n"
    return liczby
print(fiz())




