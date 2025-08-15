from aiogram.utils.keyboard import ReplyKeyboardBuilder


def kb_main_menu():
    buttons = [
        '/start',
        '/random',
        '/gpt',
        '/talk',
        '/quiz',
    ]
    keyboard = ReplyKeyboardBuilder()
    for button in buttons:
        keyboard.button(
            text=button,
        )
    keyboard.adjust(1, 2, 2)
    return keyboard.as_markup(
        resize_keyboard=True,
        one_time_keyboard=True,
    )
