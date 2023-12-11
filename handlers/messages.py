from aiogram import Router, F
import json
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile

import main
br = FSInputFile("source/banner.jpg")

with open("db/config.json", 'r', encoding='utf-8') as json_file:
    cfg = json.load(json_file)

from markups import inline, reply



router = Router()

@router.message()
async def main_handler(message: Message):
    
    if message.text == cfg['buttons'][0]:
        await message.answer_photo(photo=br, caption=f"<i><b>{cfg['catalog-text']}</b></i>", reply_markup=inline.catalog_markup())
        await main.bot.delete_message(message.chat.id, message.message_id-1)
        await message.delete()
        
        
        
    #Help    
    elif message.text == cfg['buttons'][1]:
        await message.answer(f"<i><b>{cfg['help-url']}</b></i>", reply_markup=reply.start_markup())
        await message.delete()
        await main.bot.delete_message(message.chat.id, message.message_id-1)
        
    #News
    elif message.text == cfg['buttons'][2]:
        await message.answer(f"<i><b>{cfg['news-url']}</b></i>", reply_markup=reply.start_markup())
        await message.delete()
        await main.bot.delete_message(message.chat.id, message.message_id-1)
    
    #Reviews    
    elif message.text == cfg['buttons'][3]:
        await message.answer(f"<i><b>{cfg['reviews-url']}</b></i>", reply_markup=reply.start_markup())
        await message.delete()
        await main.bot.delete_message(message.chat.id, message.message_id-1)
    
    else:
        await message.answer(f"<i><b>{cfg['incorrect-update']}</b></i>")