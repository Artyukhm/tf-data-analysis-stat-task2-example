import pandas as pd
import numpy as np

from scipy.stats import chi2


chat_id = 1695235986 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    length = len(x)
    return np.sqrt(sum(x ** 2) / (13 * chi2.ppf((1 + p) / 2, df = 2 * length))), \
           np.sqrt(sum(x ** 2) / (13 * chi2.ppf((1 - p) / 2, df = 2 * length)))
