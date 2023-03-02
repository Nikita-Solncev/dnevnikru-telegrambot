from .start import start
from .get_homeworks.get_homework_tomorrow import get_homework_tomorrow
from .get_homeworks.get_homework_today import get_homework_today


commands = {
    "start": start,
    "get_homework_tmr": get_homework_tomorrow,
    "get_homework_today": get_homework_today
}

def index():
    return commands