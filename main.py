print("Ведіть 3 будь-яких числа")
chislo1 = int(input())
chislo2 = int(input())
chislo3 = int(input())
age = input("Що робимо?(+/*)")
if age == "+":
    chislo4 = chislo1 + chislo2 + chislo3
    print("Результат:" + str(chislo4));
if age == "*":
    chislo4 = chislo1 * chislo2 * chislo3
    print("Результат:" + str(chislo4));
