from .dnevnik.dnevnik import get_dnevnik

import pendulum

from dotenv import dotenv_values

import jmespath

from datetime import datetime



config = dotenv_values(".env")


dn = get_d"nevnik(config["LOGIN], config["PASSWORD"])



def get_date():
    date = pendulum.tomorrow(tz="Asia/Vladivostok")
    if date.day_of_week == pendulum.SUNDAY:
        return date.next(pendulum.MONDAY)
    else:
        return date



async def get_homework(update, context):
    date = get_date()
    date = datetime.strptime(f"{date.year}, {date.month}, {date.day}", "%Y, %m, %d").date()

    data = dn.get_school_homework(config["SCHOOL_ID"], date, date)


    def parse_homework(data):
        subjects_ids = jmespath.search("subjects[*].id", data)
        homework = {}
        for i in subjects_ids:
            homework[i] = {
                "name": ' '.join(jmespath.search(f"subjects[?id==`{i}`].name", data)),
                "task": '; '.join(jmespath.search(f"works[?subjectId==`{i}`].text", data))
            }
        text = ""
        for i in homework.values():
            text += f"{i['name']}: {i['task']} \n\n"
        return text

    text = parse_homework(data)
    await update.message.reply_text(text)