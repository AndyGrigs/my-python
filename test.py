words = {}

print("Введи три пари слів")
print("-------------------")


for i in range(3):
    german = input(f"Слово {i+1}(німецька)") 
    ukr = input(f"Переклад {i+1}(українська)")
    words[german]  = ukr

print("Твої слова")
for german, ukr in words.items():
    print(f"{german} - {ukr}")