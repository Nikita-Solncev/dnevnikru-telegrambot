from handlers.dnevnik.dnevnik import get_dnevnik
from .utils.get_date import get_date_today as get_date
from .utils.parse_homework import parse_homework

import pendulum

from dotenv import dotenv_values

import jmespath



config = dotenv_values(".env")


dn = get_dnevnik(config["LOGIN"], config["PASSWORD"])


async def get_homework_today(update, context):
    date = get_date()
    if date == False:
        await update.message.reply_text("Сегодня Воскресенье! На сегодня домашнего задания нет!")
    else:

        data = dn.get_school_homework(config["SCHOOL_ID"], date, date)

        text = parse_homework(data)
        await update.message.reply_text(text)