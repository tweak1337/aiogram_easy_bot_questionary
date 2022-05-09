from aiogram import types, Dispatcher
from creation import dp, bot
from keyboards.client_keys import *
from inline import *
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import time, re, random

diagnoses = ['Тревожное расстройство', 'Hекуррентное депрессивное расстройство', 'Шизофрения']
class Fsm_storage(StatesGroup):
    numbers_1 = State()
    numbers_2 = State()
    numbers_3 = State()

# @dp.message_handler(commands=['start', 'help'])
async def main(message : types.Message):
    await bot.send_message(message.from_user.id,'Привет, я бот, который подскажет кто ты, ориентируясь на твое подсознание. Нажми начать.',
                           reply_markup=kb_client)

async def start(message : types.Message):
    await bot.send_message(message.from_user.id, 'Предлагаю пройти тест, нажми кнопку ниже, если готов', reply_markup=ready_to_test)

async def lost(message: types.Message):
    await bot.send_message(message.from_user.id, 'Для начала работы напиши /start', reply_markup=kb_client_start)

async def not_ready(message: types.Message):
    await bot.send_message(message.from_user.id, 'Возвращайся, когда будешь готов', reply_markup=ReplyKeyboardRemove())
    await bot.send_message(message.from_user.id, 'Для начала работы нажми --- /start')

async def ready(message: types.Message):
    photo1 = open('static/1/1.png', 'rb')
    photo2 = open('static/1/2.png', 'rb')
    photo3 = open('static/1/3.jpg', 'rb')
    photo4 = open('static/1/4.png', 'rb')
    photo5 = open('static/1/5.jpg', 'rb')
    photo6 = open('static/1/6.jpg', 'rb')
    photo7 = open('static/1/7.png', 'rb')
    photo8 = open('static/1/8.jpg', 'rb')
    photo9 = open('static/1/9.jpg', 'rb')
    photo10 = open('static/1/10.jpg', 'rb')
    await bot.send_message(message.from_user.id,
                           'Выбери от 1 до 5 понравившихся изображений')
    time.sleep(1)
    await bot.send_photo(message.from_user.id, photo=photo1)
    await bot.send_photo(message.from_user.id, photo=photo2)
    await bot.send_photo(message.from_user.id, photo=photo3)
    await bot.send_photo(message.from_user.id, photo=photo4)
    await bot.send_photo(message.from_user.id, photo=photo5)
    await bot.send_photo(message.from_user.id, photo=photo6)
    await bot.send_photo(message.from_user.id, photo=photo7)
    await bot.send_photo(message.from_user.id, photo=photo8)
    await bot.send_photo(message.from_user.id, photo=photo9)
    await bot.send_photo(message.from_user.id, photo=photo10)
    await Fsm_storage.numbers_1.set()
    await bot.send_message(message.from_user.id,
                           'Понравившиеся номера напиши ниже, например так: 1, 2, 3', reply_markup=ReplyKeyboardRemove())

#Задаем вопрос по первым картинкам
# @dp.message_handlers(commands = ['Готов'], state = None)
# async def first_numbers(message : types.Message):
#     await Fsm_storage.numbers_1.set()
#     await bot.send_message(message.from_user.id,
#                            'Понравившиеся номера напиши ниже, например так: 1, 2, 3')

# Ожидаем ответ по первым картинкам
# @dp.message_handlers(state = Fsm_storage.numbers_1)
async def load_numbers_1(message : types.Message, state:FSMContext):
    async with state.proxy() as data:
        nums = re.findall('\d+', message.text)
        result = [int(item) for item in nums]
        len_nums = len(result)
        if len_nums == 0:
            await message.reply('Пожалуйста, выбери хотя бы 1 картинку.')
            await Fsm_storage.numbers_1.set()
        elif len_nums >5:
            await message.reply('Ты можешь выбрать максимум 5 изображений, пожалуйста, повтори ввод.')
            await Fsm_storage.numbers_1.set()
        else:
            over10 = 0
            lower1 = 0
            for i in result:
                if i > 10:
                    over10 += 1
                if i == 0:
                    lower1 += 1
            if over10 >0:
                await message.reply(f'Ты ввел {over10} чисел со значением больше 10, пожалуйста, вводи только цифры от 1 до 10')
                await Fsm_storage.numbers_1.set()
            elif lower1 > 0:
                await message.reply(f'К сожалению нет варианта со значением 0, введи числа от 1 до 10')
                await Fsm_storage.numbers_1.set()
            else:
                await message.reply('Отлично, вот тебе еще 10 картинок!')
                data['numbers_1'] = result
                photo1 = open('static/2/1.jpg', 'rb')
                photo2 = open('static/2/2.jpeg', 'rb')
                photo3 = open('static/2/3.jpg', 'rb')
                photo4 = open('static/2/4.jpg', 'rb')
                photo5 = open('static/2/5.jpg', 'rb')
                photo6 = open('static/2/6.jpg', 'rb')
                photo7 = open('static/2/7.jpg', 'rb')
                photo8 = open('static/2/8.jpg', 'rb')
                photo9 = open('static/2/9.jpg', 'rb')
                photo10 = open('static/2/10.jpg', 'rb')
                time.sleep(1)
                await bot.send_photo(message.from_user.id, photo=photo1)
                await bot.send_photo(message.from_user.id, photo=photo2)
                await bot.send_photo(message.from_user.id, photo=photo3)
                await bot.send_photo(message.from_user.id, photo=photo4)
                await bot.send_photo(message.from_user.id, photo=photo5)
                await bot.send_photo(message.from_user.id, photo=photo6)
                await bot.send_photo(message.from_user.id, photo=photo7)
                await bot.send_photo(message.from_user.id, photo=photo8)
                await bot.send_photo(message.from_user.id, photo=photo9)
                await bot.send_photo(message.from_user.id, photo=photo10)
                await bot.send_message(message.from_user.id,
                                       'Понравившиеся номера напиши аналогичным образом, например так: 1, 2, 3')
                await Fsm_storage.next()
                # await state.finish()



async def load_numbers_2(message : types.Message, state:FSMContext):
    async with state.proxy() as data:

        nums = re.findall('\d+', message.text)
        result = [int(item) for item in nums]
        len_nums = len(result)

        if len_nums == 0:
            await message.reply('Пожалуйста, выбери хотя бы 1 картинку.')
            await Fsm_storage.numbers_2.set()
        elif len_nums >5:
            await message.reply('Ты можешь выбрать максимум 5 изображений, пожалуйста, повтори ввод.')
            await Fsm_storage.numbers_2.set()
        else:
            over10 = 0
            lower1 = 0
            for i in result:
                if i > 10:
                    over10 += 1
                if i == 0:
                    lower1 += 1
            if over10 >0:
                await message.reply(f'Ты ввел {over10} чисел со значением больше 10, пожалуйста, вводи только цифры от 1 до 10')
                await Fsm_storage.numbers_2.set()
            elif lower1 > 0:
                await message.reply(f'К сожалению нет варианта со значением 0, введи числа от 1 до 10')
                await Fsm_storage.numbers_2.set()
            else:
                data['numbers_2'] = result
                await message.reply('Отлично, лови последние 10 картинок!')

                photo1 = open('static/3/1.jpg', 'rb')
                photo2 = open('static/3/2.jpg', 'rb')
                photo3 = open('static/3/3.jpg', 'rb')
                photo4 = open('static/3/4.jpg', 'rb')
                photo5 = open('static/3/5.jpg', 'rb')
                photo6 = open('static/3/6.jpg', 'rb')
                photo7 = open('static/3/7.jpg', 'rb')
                photo8 = open('static/3/8.jpg', 'rb')
                photo9 = open('static/3/9.jpg', 'rb')
                photo10 = open('static/3/10.jpg', 'rb')
                time.sleep(1)
                await bot.send_photo(message.from_user.id, photo=photo1)
                await bot.send_photo(message.from_user.id, photo=photo2)
                await bot.send_photo(message.from_user.id, photo=photo3)
                await bot.send_photo(message.from_user.id, photo=photo4)
                await bot.send_photo(message.from_user.id, photo=photo5)
                await bot.send_photo(message.from_user.id, photo=photo6)
                await bot.send_photo(message.from_user.id, photo=photo7)
                await bot.send_photo(message.from_user.id, photo=photo8)
                await bot.send_photo(message.from_user.id, photo=photo9)
                await bot.send_photo(message.from_user.id, photo=photo10)
                await bot.send_message(message.from_user.id,
                                       'Понравившиеся номера напиши аналогичным образом, например так: 1, 2, 3')
                await Fsm_storage.next()

async def load_numbers_3(message : types.Message, state:FSMContext):
    async with state.proxy() as data:
        nums = re.findall('\d+', message.text)
        result = [int(item) for item in nums]
        len_nums = len(result)

        if len_nums == 0:
            await message.reply('Пожалуйста, выбери хотя бы 1 картинку.')
            await Fsm_storage.numbers_3.set()
        elif len_nums > 5:
            await message.reply('Ты можешь выбрать максимум 5 изображений, пожалуйста, повтори ввод.')
            await Fsm_storage.numbers_3.set()
        else:
            over10 = 0
            lower1 = 0
            for i in result:
                if i > 10:
                    over10 += 1
                if i == 0:
                    lower1 += 1
            if over10 > 0:
                await message.reply(
                    f'Ты ввел {over10} чисел со значением больше 10, пожалуйста, вводи только цифры от 1 до 10')
                await Fsm_storage.numbers_3.set()
            elif lower1 > 0:
                await message.reply(f'К сожалению нет варианта со значением 0, введи числа от 1 до 10')
                await Fsm_storage.numbers_3.set()
            else:
                data['numbers_3'] = result
                await bot.send_message(message.from_user.id, f"Молодец, ты справился, вот значения, которые ты ввел:"
                                                             f"\n{data['numbers_1']}\n"
                                                             f"{data['numbers_2']}\n"
                                                             f"{data['numbers_3']}")
                await state.finish()
                time.sleep(1)

                await bot.send_message(message.from_user.id, f"Твой предварительный диагноз: {random.choice(diagnoses)}")
                time.sleep(1)
                await bot.send_message(message.from_user.id,
                                       f"Не расстраивайся, мы поможем тебе, держи ссылочку", reply_markup=urlkb)
                time.sleep(2)
                await bot.send_message(message.from_user.id,
                                       f"Для повторного прохождения тета нажми /start", reply_markup=kb_client)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(main, commands=['start', 'help'])
    dp.register_message_handler(start, commands=['Начать'])
    dp.register_message_handler(not_ready, commands=['Не_готов'])
    dp.register_message_handler(ready, commands=['Готов'], state=None)
    dp.register_message_handler(load_numbers_1, state = Fsm_storage.numbers_1)
    dp.register_message_handler(load_numbers_2, state=Fsm_storage.numbers_2)
    dp.register_message_handler(load_numbers_3, state=Fsm_storage.numbers_3)
    dp.register_message_handler(lost)
