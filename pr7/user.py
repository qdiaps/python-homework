class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def update_info(self, new_email):
        self.email = new_email
        print(f"Дані для {self.username} оновлено в об'єкті.")

class UserManager:
    def __init__(self):
        self._users = {}

    def create_user(self, username, email):
        if username in self._users:
            print(f"Користувач {username} вже існує!")
            return None
        
        user = User(username, email)
        self._users[username] = user
        print(f"Користувача {username} створено та збережено.")
        return user

    def update_user_email(self, username, new_email):
        user = self._users.get(username)
        if user:
            user.update_info(new_email)
            print(f"Email для {username} оновлено в 'базі даних'.")
        else:
            print(f"Користувача {username} не знайдено.")

    def delete_user(self, username):
        if username in self._users:
            del self._users[username]
            print(f"Користувача {username} видалено з 'бази даних'.")
        else:
            print(f"Користувача {username} не знайдено.")

manager = UserManager()
user1 = manager.create_user("user1", "user1@example.com")
manager.update_user_email("user1", "new_user1@example.com")
manager.delete_user("user1")
