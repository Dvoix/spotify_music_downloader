import asyncio
import logging
from core.bot import bot, dp
from handlers import start, help, spotify

async def main():
    try:
        logging.info("Bot is starting...")
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Bot stopped by user")
