import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1695235986 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    mean = np.mean(x)
    std = np.std(x, ddof=1)
    n = len(x)
    alpha = 1 - p
    t_value = t.ppf(1 - alpha/2, n-1)
    ci_left = mean - t_value * std / np.sqrt(n)
    ci_right = mean + t_value * std / np.sqrt(n)
    return ci_left, ci_right
