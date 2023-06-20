from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from config import ADMINs


class fsmAdminMentor(StatesGroup):
    Name = State()
    Direction = State()
    Age = State()
    Group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.from_user.id not in ADMINs:
        await message.answer('Ты не админ!')

    else:
        await fsmAdminMentor.Name.set()
        await message.answer('Name ментора ?')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Name'] = message.text
    await fsmAdminMentor.next()
    await message.answer('Направление ментора ?')


async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Direction'] = message.text
    await fsmAdminMentor.next()
    await message.answer('Возраст ментора ?')


async def load_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Age'] = message.text
    await fsmAdminMentor.next()
    await message.answer('Группа ментора ?')


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Group'] = message.text
        await message.answer(f"Информация о менторе: \n"
                             f"Имя ментора: {data['Name']} \n"
                             f"Направление ментора: {data['Direction']} \n"
                             f"Возраст ментора: {data['Age']} \n"
                             f"Группа ментора: {data['Group']} \n")

    await fsmAdminMentor.next()
    await message.answer('Всё верно ?')


async def load_submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        # Запись в базу данных
        await message.answer('Готово!')
        await state.finish()
    elif message.text.lower() == 'нет':
        await message.answer('Ну ты и чорт конечно -_-')
        await state.finish()



def register_mentor(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=['reg_mentor'])
    dp.register_message_handler(load_name, state=fsmAdminMentor.Name)
    dp.register_message_handler(load_direction, state=fsmAdminMentor.Direction)
    dp.register_message_handler(load_age, state=fsmAdminMentor.Age)
    dp.register_message_handler(load_group, state=fsmAdminMentor.Group)
    dp.register_message_handler(load_submit, state=fsmAdminMentor.submit)
