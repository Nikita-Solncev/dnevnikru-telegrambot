import pendulum
from datetime import datetime

def get_date_tomorrow():
    date = pendulum.tomorrow(tz="Asia/Vladivostok")
    if date.day_of_week == pendulum.SUNDAY:
        date.next(pendulum.MONDAY)
        date = datetime.strptime(f"{date.year}, {date.month}, {date.day}", "%Y, %m, %d")
        return date
    else:
        date = datetime.strptime(f"{date.year}, {date.month}, {date.day}", "%Y, %m, %d")
        return date
        


def get_date_today():
    date = pendulum.today()
    if date.day_of_week == pendulum.SUNDAY:
        return False
    else:
      date = datetime.strptime(f"{date.year}, {date.month}, {date.day}", "%Y, %m, %d")
      return date  
    