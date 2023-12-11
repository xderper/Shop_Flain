import json
from aiogram.utils.keyboard import ReplyKeyboardBuilder

with open("db/config.json", 'r', encoding='utf-8') as json_file:
    cfg = json.load(json_file)

def start_markup():
    builder = ReplyKeyboardBuilder()
    for i in range(len(cfg['buttons'])):
        builder.button(text=cfg['buttons'][i])
    builder.adjust(2)
    return builder.as_markup()