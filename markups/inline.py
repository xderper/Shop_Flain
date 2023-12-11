import json
import asyncio
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.context import FSMContext

with open("db/config.json", 'r', encoding='utf-8') as json_file:
    cfg = json.load(json_file)



class Pagination(CallbackData, prefix='pag'):
    action: str
    option: int

def catalog_markup():
    builder = InlineKeyboardBuilder()
    for i in range(len(cfg['games'])):
        builder.button(text=cfg['games'][i]['name'], callback_data=Pagination(action=cfg['games'][i]['name'], option=i).pack())
    builder.adjust(2)
    return builder.as_markup()


def option_markup(game):
    builder = InlineKeyboardBuilder()
    for i in range(len(cfg['games'][game]['option'])):
        t = cfg['games'][game]['option'][i]
        builder.button(text=t, callback_data=Pagination(action=t, option=game).pack())
    builder.adjust(2)
    return builder.as_markup()
    
def price_list_markup(game, currency):
    
    builder = InlineKeyboardBuilder()
    t = cfg['games'][game]['price-list']
    for i in range(len(t)):
        builder.button(text=f'{t[i][0]}{currency}', callback_data=Pagination(action=f'props_{game}', option=i).pack())
    builder.adjust(2)
    return builder.as_markup()



def props_true(game):
    builder = InlineKeyboardBuilder()
    builder.button(text=cfg['props-true-text'], callback_data=Pagination(action='props-true', option=game).pack())
    builder.adjust(2)
    return builder.as_markup()

#Admin


def admin_solution(id):
    builder = InlineKeyboardBuilder()
    builder.button(text='Принять', callback_data=Pagination(action=f'payment-true-{id}', option=0).pack())
    builder.button(text='Отклонить', callback_data=Pagination(action=f'payment-false-{id}', option=0).pack())
    builder.adjust(2)
    return builder.as_markup()
    
    
def none():
    builder = InlineKeyboardBuilder()
    return builder.as_markup()