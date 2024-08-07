# Визначення початкових даних
cat = {}
info = {"status": "vaccinated", "breed": True}

# Додавання інформації про кота
cat["nick"] = "Simon"
cat["age"] = 7
cat["characteristics"] = ["лагідний", "кусається"]

# Використання методу update для додавання до словника cat всіх пар ключ-значення зі словника info
cat.update(info)

# Оголошення змінної age та використання методу get для отримання віку кота
age = cat.get("age")

print(f"Вік кота: {age}")
print(cat)