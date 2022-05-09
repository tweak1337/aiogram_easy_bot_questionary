from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

#Кнопки
urlkb = InlineKeyboardMarkup(row_width=1)
urlbutton = InlineKeyboardButton(text='Переходи',url='https://mosgorzdrav.ru/pkb1')
urlkb.add(urlbutton)