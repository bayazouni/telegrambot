import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "5952554161:AAECvJNYpPrKxNP0ZUVIaVLKjQtU6zElkM4"
LANGUAGES = {
    "1": {"en": "English", "fa": "انگلیسی"},
    "2": {"en": "Persian", "fa": "فارسی"}
}
FORMULAS = {
    "1": {"en": "π×4×r^2", "fa": "شعاع × شعاع ×۴×π"},
    "2": {"en": "(Diameter×3)+(Diameter×3×(Diameter-1))", "fa": "( قطر×۳)+(قطر×۳×(۱-قطر))"}
}

def start(update, context):
    message = "Choose your language:\n"
    for key, value in LANGUAGES.items():
        message += f"{key}. {value[context.user_data['lang']]}\n"
    update.message.reply_text(message)

def set_language(update, context):
    lang_choice = update.message.text
    if lang_choice in LANGUAGES:
        context.user_data['lang'] = lang_choice
        message = f"Language set to {LANGUAGES[lang_choice][context.user_data['lang']]}."
        update.message.reply_text(message)
        ask_formula(update, context)
    else:
        update.message.reply_text("Invalid choice. Please try again.")

def ask_formula(update, context):
    message = "Choose a formula for calculating the area of a sphere:\n"
    for key, value in FORMULAS.items():
        message += f"{key}. {value[context.user_data['lang']]}\n"
    update.message.reply_text(message)

def set_formula(update, context):
    formula_choice = update.message.text
    if formula_choice in FORMULAS:
        context.user_data['formula'] = formula_choice
        radius_prompt = "Enter the radius of the sphere:"
        update.message.reply_text(radius_prompt)
    else:
        update.message.reply_text("Invalid choice. Please try again.")

def calculate_area(update, context):
    radius = float(update.message.text)
    formula = FORMULAS[context.user_data['formula']][context.user_data['lang']]
    if 'π' in formula:
        result = 4 * 3.14 * radius ** 2
    else:
        diameter = 2 * radius
        result = (diameter * 3) + (diameter * 3 * (diameter - 1))
    message = f"The area of the sphere with radius {radius} is: {result}"
    update.message.reply_text(message)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.regex(r"^[1-2]$"), set_language))
    dp.add_handler(MessageHandler(Filters.regex(r"^[1-2]$"), set_formula))
    dp.add_handler(MessageHandler(Filters.text, calculate_area))

    updater.start_polling()
    updater.idle()

if name == ' main ' : 
        main ()
