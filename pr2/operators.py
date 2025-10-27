a = 10
b = 5.0
print(f"Числа: {a} і {b}")
print(f"{a} > {b}: {a > b}")
print(f"{a} < {b}: {a < b}")
print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")
print(f"{a} >= 10: {a >= 10}")
print(f"{b} <= 5: {b <= 5}")

str1 = "apple"
str2 = "banana"
str3 = "apple"
print(f"\nРядки: '{str1}' і '{str2}'")
print(f"'{str1}' == '{str3}': {str1 == str3}")
print(f"'{str1}' == '{str2}': {str1 == str2}")
print(f"'{str1}' < '{str2}': {str1 < str2}")

print(f"\nБулеві: True і False")
print(f"True == True: {True == True}")
print(f"True == False: {True == False}")
print(f"True > False: {True > False}")
print(f"True == 1: {True == 1}")
print(f"False == 0: {False == 0}")

list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = [1, 2, 4]
print(f"\nСписки: {list_a}, {list_b}, {list_c}")
print(f"{list_a} == {list_b}: {list_a == list_b}")
print(f"{list_a} == {list_c}: {list_a == list_c}")
print(f"{list_a} is {list_b}: {list_a is list_b}")
print(f"{list_a} is {list_c}: {list_a is list_c}")
print(f"{list_a} < {list_c}: {list_a < list_c}")

tuple_a = (1, 2)
tuple_b = (1, 2)
tuple_c = (1, 3)
print(f"\nКортежі: {tuple_a}, {tuple_b}, {tuple_c}")
print(f"{tuple_a} == {tuple_b}: {tuple_a == tuple_b}")
print(f"{tuple_a} < {tuple_c}: {tuple_a < tuple_c}")

dict_a = {'x': 1, 'y': 2}
dict_b = {'y': 2, 'x': 1}
dict_c = {'x': 1, 'y': 9}
print(f"\nСловники: {dict_a}, {dict_b}, {dict_c}")
print(f"{dict_a} == {dict_b}: {dict_a == dict_b}")
print(f"{dict_a} == {dict_c}: {dict_a == dict_c}")