favorite_books = {
    "1984": 1949,
    "Дюна": 1965
}
print(f"Старий словник: {favorite_books}")

favorite_books["Майстер і Маргарита"] = 1967

print("Оновлений словник:")
for title, year in favorite_books.items():
    print(f" - {title} (рік: {year})")
