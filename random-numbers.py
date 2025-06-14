import random

def get_numbers_ticket(min, max, quantity):
    """
    Функція генерує відсортований список випадкових чисел 
    в заданому діапазоні.
    Параметри:
    min (int): мінімальне можливе число (не менше 1).
    max (int): максимальне можливе число (не більше 1000).
    quantity (int): кількість чисел в наборі (має бути 
    не більше max - min + 1).
    Повертає:
    list: Це відсортований список випадкових чисел.
          Якщо параметри не будуть некоректні — він поверне 
          порожній список.
    """
    if (
        not isinstance(min, int) or not isinstance(max, int) or not isinstance(quantity, int)
        or min < 1 or max > 1000
        or min > max
        or quantity <= 0 or quantity > (max - min + 1)
    ):
        return []
    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)
# Використання функції
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

