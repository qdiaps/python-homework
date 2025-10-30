correct_password = "password123"
user_password = "password123"

message = "Ви увійшли в систему" if user_password == correct_password else "Неправильний пароль"
print(message)
