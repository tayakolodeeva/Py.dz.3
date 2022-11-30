num = int(input("Введите число:\n"))
binary_number = ""
while num != 0:
    binary_number = str(num%2) + binary_number
    num //=2
print(f'Результат преобразования равен {binary_number}')