from handlers.index import index
from telegram.ext import ApplicationBuilder, ContextTypes,  CommandHandler

from dotenv import dotenv_values

import logging

if __name__ == "__main__":
    config = dotenv_values(".env")

    logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

    application = ApplicationBuilder().token(config["TG_BOT_TOKEN"]).build()
 
    for k,v in index().items():
        application.add_handler(CommandHandler(k, v))
    
    application.run_polling()