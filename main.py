from aiogram import Dispatcher, Bot, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

token_api = '7070668396:AAFtcWm31cjzRha_zRw40ihczbk7EcNQUpI'
bot = Bot(token=token_api)
dp = Dispatcher(bot)

keyboard = InlineKeyboardMarkup(row_width=1)
first_inline = InlineKeyboardButton('Переключиться на вторую клавиатуру', callback_data= 'go_to_2')
second_inline =InlineKeyboardButton('Отправь случайное число', callback_data='send_random')
keyboard.add(first_inline, second_inline)

keyboard2 = InlineKeyboardMarkup(row_width=1)
third_inline = InlineKeyboardButton('Переключиться на первую клавиатуру', callback_data= 'go_to_1')
fourth_inline = InlineKeyboardButton('Текущее время', callback_data='send_date_time')
keyboard2.add(third_inline, fourth_inline)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Ты на первой клавиатуре, нажми кнопку чтобы перейти на вторую клавиатуру', reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data == 'go_to_2')
async def go_to_2(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('Ты перешел на вторую клавиатуру, нажми на кнопку, чтобы вернуться на первую клавиатуру', reply_markup=keyboard2)

@dp.callback_query_handler(lambda c: c.data == 'go_to_1')
async def go_to_2(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('Ты перешел на первую клавиатуру, нажми на кнопку, чтобы вернуться на вторую клавиатуру', reply_markup=keyboard)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)