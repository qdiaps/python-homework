number = 5
factorial = 1

if number < 0:
    print("Факторіал не визначений для негативних чисел")
elif number == 0:
    print("Факторіал 0 = 1")
else:
    for i in range(1, number + 1):
        factorial *= i
    print(f"Факторіал {number} = {factorial}")
