import json
from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from aiogram.types import CallbackQuery


br = FSInputFile("source/banner.jpg")
import main
with open("db/config.json", 'r', encoding='utf-8') as json_file:
    cfg = json.load(json_file)

from markups import inline

router = Router()

@router.callback_query((inline.Pagination.filter(F.action.startswith('payment-true'))))
async def payment_true_handler(call: CallbackQuery, callback_data: inline.Pagination, state: FSMContext):
    id = callback_data.action[13:]

    await main.bot.send_message(chat_id=id, text=f'<i><b>{cfg["payment-true"]}</b></i>')
    await call.message.reply(text = f"<i><b>{cfg['payment-true-admin']}</b></i>")
    await call.message.delete_reply_markup(str(call.message.message_id))
    await state.clear()
    
    
@router.callback_query(inline.Pagination.filter(F.action.startswith('payment-false')))
async def payment_true_handler(call: CallbackQuery, callback_data: inline.Pagination, state: FSMContext):
    id = callback_data.action[13:]

    await main.bot.send_message(chat_id=id, text=f'<i><b>{cfg["payment-false"]}</b></i>')
    await call.message.reply(text = f"<i><b>{cfg['payment-false-admin']}</b></i>")
    await call.message.delete_reply_markup(str(call.message.message_id))
    await state.clear()


@router.message((F.from_user.id == int(cfg['admin-id'])) & (F.text == 'stop_admin'))
async def stop_bot(message: Message):
    await message.answer(text = f"<i><b>{cfg['stop-bot']}</b></i>")
    __import__("sys").exit(0)