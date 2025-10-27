dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print(f"car = {dict_test['car']}, where = {dict_test['where']}")

print(f"Keys: {dict_test.keys()}")
print(f"Values: {dict_test.values()}")

items_view = dict_test.items()
print(items_view)