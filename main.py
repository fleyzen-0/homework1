print("Ведіть 3 будь-яких числа")
chislo1 = int(input())
chislo2 = int(input())
chislo3 = int(input())
age = input("Що потрібно?(Максимум, Мінімум, Середньоарифметичне )")
if age == "Максимум":
    ma = max(chislo1, chislo2, chislo3)
    print(ma)
if age == "Мінімум":
    mi = min(chislo1, chislo2, chislo3)
    print(mi)
if age == "Середньоарифметичне":
    sered = float((chislo1 + chislo2 + chislo3) / 3)
    print(sered)