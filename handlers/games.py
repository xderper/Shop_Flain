import json
from aiogram import Router, F
from aiogram.types import Message
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
@router.callback_query(inline.Pagination.filter(F.action == 'Pubg Mobile'))
async def Pubg_Mobile_handler_choose_option(call: CallbackQuery, callback_data: inline.Pagination):
    await call.message.answer_photo(photo=br, caption=f"<i><b>{cfg['choose-option-text']}</b></i>", reply_markup=inline.option_markup(callback_data.option))
    await call.message.delete()

@router.callback_query(inline.Pagination.filter(F.action == 'Unknown Cash'))
async def Pubg_Mobile_handler_price_list(call: CallbackQuery, callback_data: inline.Pagination, state: FSMContext):
    await call.message.answer_photo(photo=br, caption=f"<i><b>{cfg['choose-price-list']}</b></i>", reply_markup=inline.price_list_markup(callback_data.option, currency=cfg['games'][callback_data.option]['currency']))  
    await call.message.delete()
    
   
@router.callback_query(inline.Pagination.filter((F.action == 'props-true') & (F.option == 0)))
async def Pubg_Mobile_handler_get_id(call: CallbackQuery, callback_data: inline.Pagination, state: FSMContext):
    await call.message.answer(f"<i><b>{cfg['games'][callback_data.option]['get-id']}</b></i>")
    await call.message.delete()
    await state.set_state(Form.id_user)

#ALL    
@router.callback_query(inline.Pagination.filter(F.action.startswith('props_')))
async def props_handler(call: CallbackQuery, callback_data: inline.Pagination, state: FSMContext):
    t = cfg['games'][int(callback_data.action[6:])]
    await call.message.answer_photo(photo=br, 
                                    caption=f"<i><b>{cfg['games'][int(callback_data.action[6:])]['props-text-start']} {cfg['games'][int(callback_data.action[6:])]['price-list'][callback_data.option][1]}р\n{cfg['games'][int(callback_data.action[6:])]['props-text-end']}</b></i>", 
                                    reply_markup=inline.props_true(int(callback_data.action[6:])))
    
    await state.update_data(price = t['price-list'][callback_data.option][1], amount = t['price-list'][callback_data.option][1])
    await call.message.delete()