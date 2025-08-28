def is_year_lear(year):
    return (year % 4 == 0)
year = int(input("Введите год: "))
if is_year_lear(year):
    print("Год" , year, "виокосный")
else:
    print("Год" , year, "не виокосный")