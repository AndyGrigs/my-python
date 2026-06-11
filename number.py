from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters

import random
import time


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🟢 Легкий (1-300)",   callback_data="level_1")],
        [InlineKeyboardButton("🟡 Середній (1-500)", callback_data="level_2")],
        [InlineKeyboardButton("🔴 ХАРДКОР (1-700)",  callback_data="level_3")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "=== 🤖 СИСТЕМА ЗЛАМУ ЯДРА ШІ ===\n\n"
        "Оберіть рівень складності:",
        reply_markup=reply_markup
    )

async def level_chosen(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "level_1":
        max_number = 300
        level_text = "🟢 Легкий"
    elif query.data == "level_2":
        max_number = 500
        level_text = "🟡 Середній"
    else:
        max_number = 700
        level_text = "🔴 ХАРДКОР"

    context.user_data["max_number"] = max_number
    context.user_data["secret_number"] = random.randint(1, max_number)
    context.user_data["attempts"] = 0
    context.user_data["start_time"] = time.time()
    context.user_data["playing"] = True

    await query.edit_message_text(
        f"Рівень: {level_text}\n\n"
        f"[СИСТЕМА]: Я загадав число від 1 до {max_number}.\n"
        f"У тебе є 45 секунд на злам. ЧАС ПІШОВ! ⏱"
    )

async def handle_guess(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.user_data.get("playing"):
        await update.message.reply_text(
            "Напиши /start щоб почати гру! 🎮"
        )
        return

    text = update.message.text

    if not text.isdigit():
        await update.message.reply_text(
            "[ПОМИЛКА]: Вводь тільки ЦИФРИ! 🔢"
        )
        return

    elapsed = time.time() - context.user_data["start_time"]
    remaining = int(45 - elapsed)

    if elapsed > 45:
        secret = context.user_data["secret_number"]
        context.user_data["playing"] = False
        await update.message.reply_text(
            f"⏰ СИСТЕМА БЕЗПЕКИ ЗАБЛОКОВАНА! Час вийшов.\n"
            f"Загадане число було: {secret}\n\n"
            f"Напиши /start щоб спробувати знову."
        )
        return

    guess = int(text)
    secret = context.user_data["secret_number"]
    max_number = context.user_data["max_number"]
    context.user_data["attempts"] += 1
    attempts = context.user_data["attempts"]

    if guess == secret:
        context.user_data["playing"] = False
        await update.message.reply_text(
            f"🎉 ДОСТУП НАДАНО! Ти зламав ядро!\n"
            f"Спроб: {attempts} | Час: {int(elapsed)} сек\n\n"
            f"Напиши /start щоб грати знову. 🚀"
        )
    elif guess < 1 or guess > max_number:
        await update.message.reply_text(
            f"[ПОМИЛКА]: Вводь число від 1 до {max_number}! ⚠️"
        )
    elif guess < secret:
        await update.message.reply_text(
            f"🤖 [ШІ]: Моє число БІЛЬШЕ.\n"
            f"Спроба #{attempts} | Залишилось: {remaining} сек ⏱"
        )
    else:
        await update.message.reply_text(
            f"🤖 [ШІ]: Моє число МЕНШЕ.\n"
            f"Спроба #{attempts} | Залишилось: {remaining} сек ⏱"
        )


app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(level_chosen, pattern="^level_"))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_guess))

print("Бот запущено...")
app.run_polling()