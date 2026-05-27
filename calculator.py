def add(a, b):
    """Возвращает сумму двух чисел."""
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
    """
    return a ** b