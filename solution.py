import pandas as pd
import numpy as np


chat_id = 5780444792 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: 
    df = pd.DataFrame({'x':x,'y':y})   # make dataframe
    df_describe = df.describe().T
    mean_lst = list(df_describe['mean'])  # список со значением средних
    std_lst = list(df_describe['std'])  # список со значиниями дисперсий
    flag = True
    level_mean = 0.258  # пороговое значение отклонения среднего на исторических данных
    level_std = 0.1506 # пороговое значение отклонения дисперсии на исторических данных
    for i in range(len(mean_lst)):
      # если есть отклонения больше пороговых значений, то мы бракуем выборку
      if abs(mean_lst[i]) > level_mean or abs(std_lst[i] - 1) > level_std:
        flag = False
        break
    return flag
