day_number = 3

days_map = {
    1: "Понеділок",
    2: "Вівторок",
    3: "Середа",
    4: "Четвер",
    5: "П'ятниця",
    6: "Субота",
    7: "Неділя"
}

day_name = days_map.get(day_number)

if day_name:
    print(day_name)
else:
    print("Помилка: недійсний номер дня")
