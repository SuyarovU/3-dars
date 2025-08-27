from aiogram.filters import  CommandStart
from aiogram import Router
from aiogram.types import Message

router=Router()

@router.message(CommandStart())
async def start_hanlde(message:Message):
    await message.answer("Botga xush kelibsiz!")



