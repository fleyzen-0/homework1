print("Введіть кількість метрів")
metr = float(input())
vmetr = input("В що конвертуемо?(Милі, Дюйми, Ярди.)")
if vmetr == "Милі":
    print(metr * 0.000621371);
if vmetr == "Дюйми":
    print(metr *39.370);
if vmetr == "Ярди":
    print(metr * 1.0936);