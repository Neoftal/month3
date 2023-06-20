from aiogram import types, Dispatcher
from config import bot
from random import choice


async def echo_text(message: types.Message) -> None:
    bad_words = ['дурак', 'html', 'js']
    for word in bad_words:
        if word in message.text.lower().replace(" ", ""):
            # await bot.delete_message(message.chat.id, message.message_id)
            await message.delete()
            await message.answer(
                f"Не матерись @{message.from_user.username}\n"
                f"сам ты {word}"
            )
    if message.text.isdigit():
        squared = int(message.text) ** 2
        await bot.send_message(message.chat.id, squared)


    if message.text.lower() == 'game':  # Игра работает для всех!
        a = ['⚽️', '🎰', '🏀', '🎯', '🎳', '🎲']
        random = choice(a)
        await bot.send_dice(message.chat.id, emoji=random)
    else:
        await bot.send_message(message.from_user.id, message.text)


# @dp.message_handler(content_types=['sticker'])
async def echo_sticker(message: types.Message) -> None:
    await bot.send_sticker(message.chat.id, message.sticker.file_id)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo_text, content_types=['text'])
    dp.register_message_handler(echo_sticker, content_types=['sticker'])
