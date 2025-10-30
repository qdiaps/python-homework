numbers = [1, 5, 15]
to_add = [10, 20]

for num in to_add:
    numbers.append(num)
print(f"Список після додавання: {numbers}")

to_remove = 10

if to_remove in numbers:
    numbers.remove(to_remove)
    print(f"Список після видалення {to_remove}: {numbers}")
else:
    print(f"Елемент {to_remove} не знайдено для видалення.")
