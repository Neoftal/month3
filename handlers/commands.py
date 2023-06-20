from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp



async def start_command(message: types.Message) -> None:
    await bot.send_message(message.chat.id,
                           f"Приветствую Воин {message.from_user.full_name}")


async def quiz_1(message: types.Message) -> None:
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton("NEXT", callback_data="next_button_1")
    markup.add(next_button)

    quiestion = "Кто  создал персонажей доты?"
    answers = [
        "Барак Обама",
        "Клоун",
        "Айсфрог",
        "Путин",
        "Кличко",
        "Тимур",
    ]

    await message.answer_poll(
        question=quiestion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Стыдно не знать!",
        open_period=10,
        reply_markup=markup
    )


async def cat_handler(message: types.Message) -> None:
    await message.answer_photo(
        photo="https://cs14.pikabu.ru/post_img/2022/01/31/10/1643649892185869323.jpg"
    )

    photo = open("media/img.png", "rb")
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=photo
    )


def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(cat_handler, Text(equals="mem", ignore_case=True))