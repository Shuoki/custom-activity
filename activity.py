# https://github.com/Shuoki
# Developer @TheMisterSenpai

from pypresence import Presence

import os
import shutil
from time import time
import config

RPC = Presence(config.CLIENT_ID)
print("[LOG] Активность запустилась")

#Очистка папки модуля
path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'pypresence/__pycache__')
shutil.rmtree(path)

#Запуск активности
RPC.connect()
RPC.update(
    details = config.DETAILS,
    state = config.STATE,
    large_image = config.LARGE_IMAGE,
    buttons = config.BUTTON
)
input()
