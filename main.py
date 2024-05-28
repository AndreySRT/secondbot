from aiogram import Dispatcher, Bot, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

token_api = '7070668396:AAFtcWm31cjzRha_zRw40ihczbk7EcNQUpI'
bot = Bot(token=token_api)
dp = Dispatcher(bot)

keyboard = InlineKeyboardMarkup(row_width=1)
first_inline = InlineKeyboardButton('Переключиться на вторую клавиатуру', callback_data= 'go_to_2')
keyboard.add(first_inline)

keyboard2 = InlineKeyboardMarkup(row_width=1)
second_inline = InlineKeyboardButton('Переключиться на первую клавиатуру', callback_data= 'go_to_1')
keyboard2.add(second_inline)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Ты на первой клавиатуре, нажми кнопку чтобы перейти на вторую клавиатуру.', reply_markup=keyboard)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)