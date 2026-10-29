import logging
import re
from aiogram import Bot, Dispatcher, executor, types

# BotFather bergan tokeningiz
API_TOKEN = '9281498858:AAHUnC-tPlY0oNwVfCyy6todNsgAV81LWs'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(content_types=types.ContentType.TEXT)
async def analyze_group_message(message: types.Message):
  text = message.text.lower()

  # Xabardagi raqamlarni ajratib olish
  numbers = re.findall(r'\d+', text.replace(' ', ''))

  if not numbers:
    return

  summa = numbers[-1]

  if 'berdi' in text:
    await message.reply(
        f"📥 **Kirim qayd etildi!**\n"
        f"💬 Xabar: {message.text}\n"
        f"💵 Aniqlangan summa: {summa} so'm"
    )

  elif 'olindi' in text:
    await message.reply(
        f"📤 **Chiqim/Pul olindi qayd etildi!**\n"
        f"💬 Xabar: {message.text}\n"
        f"💵 Aniqlangan summa: {summa} so'm"
    )

  elif 'yuk' in text or 'ketti' in text:
    await message.reply(
        f"📦 **Yuk ketishi qayd etildi!**\n"
        f"💬 Xabar: {message.text}\n"
        f"💵 Summa/Qiymat: {summa}"
    )


if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)
