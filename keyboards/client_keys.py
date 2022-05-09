from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start = KeyboardButton('/start')
nachat = KeyboardButton('/Начать')
gotov = KeyboardButton('/Готов')
negotov = KeyboardButton('/Не_готов')


kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_start = ReplyKeyboardMarkup(resize_keyboard=True)
ready_to_test = ReplyKeyboardMarkup(resize_keyboard=True)


kb_client_start.add(start)
kb_client.add(nachat)
ready_to_test.row(gotov, negotov)


