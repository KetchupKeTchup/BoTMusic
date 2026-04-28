import asyncio
import os
from aiogram import Bot, Dispatcher, types
from downloader import download_audio

TOKEN = "ТУТ_ТВОЙ_TOKEN"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def handle_message(message: types.Message):
    url = message.text

    if "youtube.com" not in url and "youtu.be" not in url:
        await message.answer("Скинь YouTube ссылку")
        return

    await message.answer("⏳ Скачиваю...")

    try:
        file_path = download_audio(url)

        await message.answer_audio(types.FSInputFile(file_path))

        os.remove(file_path)

    except Exception as e:
        await message.answer(f"Ошибка: {str(e)}")

async def main():
    os.makedirs("temp", exist_ok=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())