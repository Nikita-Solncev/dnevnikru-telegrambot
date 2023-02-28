from .start import start
from .get_homework import get_homework

commands = {
    "start": start,
    "get_homework": get_homework
}

def index():
    return commands