def add(a, b):
    """Возвращает сумму двух чисел с выводом в консоль."""
    result = a + b
    print(f"Сумма {a} + {b} = {result}")
    return result

def subtract(a, b):
    """Возвращает разность двух чисел."""
    return a - b

def multiply(a, b):
    """Возвращает произведение двух чисел."""
    return a * b

def divide(a, b):
    """Возвращает частное двух чисел. Вызывает ошибку при делении на ноль."""
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b
def power(a, b):
    """
    Возвращает a в степени b.

    Args:
        a (int/float): Основание степени
        b (int/float): Показатель степени

    Returns:
        int/float: Результат возведения в степень

    Raises:
        TypeError: Если аргументы не числа
    """
    # Проверка типов
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Оба аргумента должны быть числами")
    
    return a ** b
