from aiogram import Bot,Dispatcher,types
from aiogram.filters.command import Command
import asyncio
APY_TOKEN='7550595433:AAHL6bjueMDcpj4-7qQqmuKjysyW4IHTUxs'

bot=Bot(token=APY_TOKEN)
dp= Dispatcher()

@dp.massage(Command("start"))
async def welcome(message: types.Message):
    await message.reply("Привет.\nМеня зовут Даня\nЯ пишу ботов")

async def main():
    await dp.start_polling(bot)

if __name__=='__main__':
    asyncio.run(main())




