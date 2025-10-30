capitals = {
    "Україна": "Київ",
    "Польща": "Варшава",
    "Німеччина": "Берлін",
    "Франція": "Париж"
}

country_to_find = "Німеччина"
print(f"Шукаємо столицю для: {country_to_find}")

if country_to_find in capitals:
    print(f"Столиця країни {country_to_find} - це {capitals[country_to_find]}.")
else:
    print(f"Країну {country_to_find} не знайдено у словнику.")
