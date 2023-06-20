from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def quiz_2(callback: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton("NEXT", callback_data="next_button_2")
    markup.add(next_button)

    quiestion = "Что такое Пайчарм?"
    answers = [
        "Имя кота",
        "Программа",
        "Телефон",
        "Мем",
        "Компьютер",
    ]

    # await bot.send_poll()
    await callback.message.answer_poll(
        question=quiestion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Стыдно не знать!",
        open_period=10,
        reply_markup=markup
    )





async def quiz_3(callback: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton("NEXT", callback_data="next_button_3")
    markup.add(next_button)

    quiestion = "Что такое красота?"
    answers = [
        "Любовь",
        "Или поступки",
        "Убойная трава",
        "Или вино и ",
        "Про##итутки",
    ]

    # await bot.send_poll()
    await callback.message.answer_poll(
        question=quiestion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Стыдно не знать!",
        open_period=10,
        reply_markup=markup
    )
async def quiz_4(callback: types.CallbackQuery):

    quiestion = "Как зовут первого космонавта?"
    answers = [
        "Гагарин",
        "Москевич",
        "Уроброс",
        "Скриптонит",
        "Баста",
    ]

    # await bot.send_poll()
    await callback.message.answer_poll(
        question=quiestion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Стыдно не знать!",
        open_period=10
    )



def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="next_button_1")
    dp.register_callback_query_handler(quiz_3, text="next_button_2")
    dp.register_callback_query_handler(quiz_4, text="next_button_3")


