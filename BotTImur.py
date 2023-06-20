from aiogram import Bot, Dispatcher, types, executor
import logging
from config import dp
from handlers import commands, callback, extra, admin, fsm_anketa


commands.register_handlers_commands(dp)
callback.register_handlers_callback(dp)
fsm_anketa.register_mentor(dp)
admin.register_handlers_admin(dp)
extra.register_handlers_extra(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
