from config import bot_token
from aiogram import Bot, Dispatcher
from aiogram.types import Message
import asyncio
import logging
from aiogram.filters import Command
import wikipedia

wikipedia.set_lang("uz")
API_TOKEN = bot_token

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


# /start va /help komandalariga javob
@dp.message(Command(commands=["start"]))
async def send_welcome(message: Message):
    welcome_message = (
        "👋 Salom, xush kelibsiz!\n\n"
        "Quyidagi komandalar mavjud:\n\n"
        "🆘 /help - Yordam olish\n\n"
        "ℹ️ /info - Bot haqida ma'lumot"
    )

    await message.reply(welcome_message)


@dp.message()
async def wiki(message: Message):
    try:
        await message.reply(wikipedia.summary(message.text))
    except wikipedia.exceptions.DisambiguationError as exc:
        options = "\n".join(f"• {opt}" for opt in exc.options[:5])
        await message.answer(
            f"'{message.text}' nomi bir nechta maqolaga mos keladi. Aniqlashtiring:\n{options}"
        )
    except wikipedia.exceptions.PageError:
        await message.answer(f"'{message.text}' nomli maqola topilmadi.")
    except Exception as exc:
        logging.exception("Wikipedia so'rovida xato: %s", exc)
        await message.answer("Xatolik yuz berdi. Keyinroq qayta urinib ko'ring.")


if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
