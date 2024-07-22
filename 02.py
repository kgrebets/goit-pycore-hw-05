from decimal import Decimal
import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r'\b(\d+(\.\d+)?)\b'
    numbers_list = re.findall(pattern, text)
    
    for n in numbers_list:
        yield Decimal(n[0])


def sum_profit(text: str, func: Callable):
    sum = Decimal(0.0)
    for next_number in func(text):
        sum += next_number
    return sum

#додатково додана умована числа без центів
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів, а також 10 ."

total_income = sum_profit(text, generator_numbers)

print(f"Загальний дохід: {total_income}")