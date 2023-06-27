import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from config import ADMINs, bot
from database.bot_db import sql_command_all_ids
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.date import DateTrigger

async def happy_birthday():
    video = open("media/video/video1.mp4", "rb")
    for user in ADMINs:
        await bot.send_video(
            chat_id=user,
            video=video,
            caption=f"C днем рождения меня!!!"
       )

async def set_scheduler():
        scheduler = AsyncIOScheduler(timezone="Asia/Bishkek")
        scheduler.add_job(
             happy_birthday,
             CronTrigger(
                 year=2023,
                 month=9,
                 day=9,
                 day_of_week=5,
                 hour=0,
                 minute=0



            ),
        )
        scheduler.start()
