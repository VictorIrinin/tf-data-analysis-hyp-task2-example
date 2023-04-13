import pandas as pd
import numpy as np


chat_id = 5780444792 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    res = False
    if x[0] == y[0] and x[1] == y[1] and x[2] == y[2]:
        res = False
    else:
        res = True
    return res # Ваш ответ, True или False
