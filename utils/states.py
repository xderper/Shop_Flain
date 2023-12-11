from aiogram.fsm.state import StatesGroup, State

class Form(StatesGroup, prefix='my'):
    #Pubg Mobile
    id_user = State()
    photo_user = State()
    payment = State()
    
    #ALL
    price = State()
    amount = State()