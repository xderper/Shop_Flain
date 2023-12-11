import json
from aiogram import Router, F
from aiogram.types import Message
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from aiogram.types import CallbackQuery

from utils.states import Form

br = FSInputFile("source/banner.jpg")
import main
with open("db/config.json", 'r', encoding='utf-8') as json_file:
    cfg = json.load(json_file)

from markups import inline

router = Router()



#Pubg Mobile
@router.message(Form.id_user)
async def Pubg_Mobile_get_id(message: Message, state: FSMContext):
    
    if message.text:
        if message.text.isdigit() and len(message.text)==11:
            await message.answer(f"<i><b>{cfg['games'][0]['get-photo']}</b></i>")
            await state.update_data(id_user = message.text)
            await state.set_state(Form.photo_user)
        else:
            await message.answer(f"<i><b>{cfg['games'][0]['id-incorrect']}</b></i>")
            await state.set_state(Form.id_user)
    else:
        await message.answer(f"<i><b>{cfg['games'][0]['id-incorrect']}</i></b>")
        await state.set_state(Form.id_user)
        

@router.message(Form.photo_user)
async def Pubg_Mobile_get_photo(message: Message, state: FSMContext):
    if message.photo:   
        data = await state.get_data()
        file_id = message.photo[-1].file_id
        photo = message.photo[-1]
        file_id = photo.file_id
        await main.bot.send_photo(chat_id=cfg['admin-panel'], caption=f'<b><i>User tag  -> {message.from_user.username} \nGame -> Pubg Mobile\nPubg ID -> {data["id_user"]}\nAmount UC -> {data["amount"]}\nPrice -> {data["price"]}р </i></b>',photo=file_id, reply_markup=inline.admin_solution(message.chat.id))
        await message.reply(f"<i><b>{cfg['payment-wait']}</b></i>")
        await state.set_state(Form.payment)
    else:
        await message.answer(f"<i><b>{cfg['games'][0]['photo-incorrect']}</b></i>")
        await state.set_state(Form.photo_user)
       
       