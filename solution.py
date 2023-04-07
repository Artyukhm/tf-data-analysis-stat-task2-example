import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1695235986 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    t = x.mean() / (np.std(x) / np.sqrt(n))
    alpha = 1 - p
    df = n - 1
    lower = scipy.stats.t.ppf(alpha / 2, df)
    upper = scipy.stats.t.ppf(1 - alpha / 2, df)
    return (lower, upper)
