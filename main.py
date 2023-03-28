numbers=[1,2,3,4]
suma=0
for number in range(len(numbers)):
    suma+=numbers[number]
    numbers[number]=suma
print(numbers)
