from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from . import keyboards
from database.bot_db import sql_command_insert



class FSMAdmin(StatesGroup):
    name = State()
    age = State()
    gender = State()
    region = State()
    photo = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        await FSMAdmin.name.set()
        await message.answer("Имя Ментора?")
    else:
        await message.reply("Пиши в лс!")


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.from_user.id
        data['username'] = f"@{message.from_user.username}" \
            if message.from_user.username else None
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("Возраст ментора?")


async def load_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пиши числа!")
    elif not 14 < int(message.text) < 50:
        await message.answer("Доступ воспрещен!")
    else:
        async with state.proxy() as data:
            data['age'] = message.text
        await FSMAdmin.next()
        await message.answer("Какой пол?")


async def load_gender(message: types.Message, state: FSMContext):
    if message.text.lower() not in ['женщина', 'мужчина', 'незнаю', 'муж',
    'жен']:

        await message.answer("Пользуйся кнопками!")
    else:
        async with state.proxy() as data:
            data['gender'] = message.text
        await FSMAdmin.next()
        await message.answer("Регион Ментора?")


async def load_region(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['region'] = message.text
    await FSMAdmin.next()
    await message.answer("Фото Ментора)")


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
        await message.answer_photo(data['photo'],
                                   caption=f"{data['name']} {data['age']} "
                                   f"{data['gender']} {data['region']}")
    await FSMAdmin.next()
    await message.answer("Все верно?")


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        await sql_command_insert(state)
        await state.finish()
        await message.answer("Ментор зареган!")
    elif message.text.lower() == 'заново':
        await FSMAdmin.name.set()
        await message.answer("Как звать?")
    else:
        await message.answer("Используй кнопки!")





def register_hanlers_fsm_anketa(dp: Dispatcher):


    dp.register_message_handler(fsm_start, commands=['reg_mentor'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_gender, state=FSMAdmin.gender)
    dp.register_message_handler(load_region, state=FSMAdmin.region)
    dp.register_message_handler(load_photo, state=FSMAdmin.photo,
                                content_types=['photo'])
    dp.register_message_handler(submit, state=FSMAdmin.submit)

