class User:
    def __init__(self):
        self.__name = ""
        self.__email = ""
        self.__password = ""

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def set_name(self, name):
        if name and isinstance(name, str):
            self.__name = name
        else:
            print("Помилка: Ім'я не може бути порожнім.")

    def set_email(self, email):
        if email and "@" in email:
            self.__email = email
        else:
            print(f"Помилка: '{email}' не є валідною електронною поштою.")

    def set_password(self, password):
        if password and len(password) >= 8:
            self.__password = password
        else:
            print("Помилка: Пароль має містити щонайменше 8 символів.")

print("Створення нового користувача...")
user1 = User()

user1.set_name("Олена")
user1.set_email("olena@example.com")
user1.set_password("super_secret_pass_123")

print("\n--- Дані користувача ---")
print(f"Ім'я: {user1.get_name()}")
print(f"Email: {user1.get_email()}")
print(f"Пароль: {user1.get_password()}")

print("\n--- Спроба встановити невалідні дані ---")
user1.set_email("bad-email.com")
user1.set_password("short")

print(f"Email (не змінився): {user1.get_email()}")
print(f"Пароль (не змінився): {user1.get_password()}")
