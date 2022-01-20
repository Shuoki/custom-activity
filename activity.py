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
    details = "Команда разработчиков Open-Source проектов",
    state = "me@shuoki.top",
    large_image = "shuokiteam",
    buttons = config.BUTTON
)
input()