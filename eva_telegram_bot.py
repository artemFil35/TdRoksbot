# eva_telegram_bot.py — Ева с эмоциями

import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputFile
from aiogram.dispatcher.filters import Text
import io
import os
import tempfile
from eva_ai_module import EvaAI
from PIL import Image
import pytesseract
import pandas as pd
from datetime import datetime

API_TOKEN = '7785286296:AAEC43a5BoAn4YAKnlKr8P5_f8gS_yWVQX0'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
eva = EvaAI()
eva.set_mode("юрист")
eva.set_emotion("радость")

HISTORY_FILE = "history.xlsx"

# ... [rest of the long code is already known to be in place]
