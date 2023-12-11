import json
from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart


with open("db/config.json", 'r', encoding='utf-8') as json_file:
    cfg = json.load(json_file)

from markups import reply


router = Router()

@router.message(CommandStart())
async def start_command(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(text = f'<i><b>{cfg["Start-message"]}</b></i>', reply_markup=reply.start_markup())
    
    
@router.message(F.text == 'start')
async def start_command(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(text = f'<i><b>{cfg["Start-message"]}</b></i>', reply_markup=reply.start_markup())