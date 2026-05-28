words = {
  "die Erfahrung": "досвід",
  "die Beziehung": "стосунки",
  "die Entscheidung": "рішення",
  "die Möglichkeit": "можливість",
  "die Verantwortung": "відповідальність",
  "die Voraussetzung": "передумова",
  "die Unterstützung": "підтримка",
  "die Entwicklung": "розвиток",
  "die Veränderung": "зміна",
  "die Herausforderung": "виклик",

  "der Eindruck": "враження",
  "der Vorschlag": "пропозиція",
  "der Vorteil": "перевага",
  "der Nachteil": "недолік",
  "der Unterschied": "різниця",
  "der Fortschritt": "прогрес",
  "der Zustand": "стан",
  "der Bereich": "сфера",
  "der Einfluss": "вплив",
  "der Zweck": "мета, призначення",

  "das Verhalten": "поведінка",
  "das Ergebnis": "результат",
  "das Verständnis": "розуміння",
  "das Verhältnis": "відношення",
  "das Einkommen": "дохід",
  "das Angebot": "пропозиція (комерційна)",
  "das Ereignis": "подія",
  "das Risiko": "ризик",
  "das Ziel": "ціль",
  "das Vertrauen": "довіра",

  "die Gesellschaft": "суспільство",
  "die Wirtschaft": "економіка",
  "die Umwelt": "довкілля",
  "die Gesundheit": "здоров’я",
  "die Ausbildung": "освіта/підготовка",
  "die Forschung": "дослідження",
  "die Sicherheit": "безпека",
  "die Zustimmung": "згода",
  "die Ablehnung": "відмова",
  "die Werbung": "реклама",

  "der Wettbewerb": "конкуренція",
  "der Verbraucher": "споживач",
  "der Beitrag": "внесок",
  "der Bericht": "звіт",
  "der Vorteil": "перевага",
  "der Zeitraum": "період",
  "der Zugang": "доступ",
  "der Inhalt": "зміст",
  "der Hinweis": "підказка, вказівка",
  "der Zweck": "призначення"
}


print("Введи три пари слів")
print("-------------------")


# for i in range(2):
#     german = input(f"Слово {i+1}(німецька)  ") 
#     ukr = input(f"Переклад {i+1}(українська)  ")
#     words[german]  = ukr

print("Твої слова")
for german, ukr in words.items():
    print(f"{german} - {ukr}")

print("\n---Практика---")
for german, ukr in words.items():
    answer = input(f"Який переклад слова {ukr} на німецьку?  ")

    if answer.lower() == german.lower():
        print("Правильно!")
    else:
        print(f"Неправильно! \n Правильна відповідь {german}") 