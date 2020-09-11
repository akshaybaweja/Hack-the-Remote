import os
import logging
from aiogram import Bot, Dispatcher, executor, types
from memeGenerator import getMeme

# Telegram Credentials
API_TOKEN = os.environ['telegram_bot_api_token']
telegramImageURL = 'https://api.telegram.org/file/bot'+API_TOKEN+'/'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Welcome to Elastic Spaces.\nLet's chat in memes 🙂")

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def image_handler(message: types.Message):
    # Generate image URL
    # file = await bot.get_file(message.photo[-1].file_id)
    # imageUrl = telegramImageURL + file.file_path

    # Send image for processing here.
    # print(imageUrl)
    await message.reply('Only I send images 👿')

@dp.message_handler()
async def echo(message: types.Message):
    name = message["from"]["first_name"] + " " + message["from"]["last_name"]
    text = message.text
    chatID = message.chat.id

    # print(name,"said",text)
    await bot.delete_message(chatID, message.message_id)
    meme = getMeme(text)
    # print('>Meme', 'URL', meme, '\n')
    await types.ChatActions.upload_photo()
    await bot.send_photo(chatID, meme, name)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)