def even_odd_generator():
    """
    Генератор, який поперемінно повертає слова
    'Парне' і 'Непарне'.
    """
    while True:
        yield "Парне"
        yield "Непарне"


def test_generator_output(gen, count=6):
    """
    Допоміжна функція для перевірки роботи генератора.
    gen — має бути генератором.
    count — скільки разів отримати значення.
    """

    if not hasattr(gen, "__next__"):
        return "Помилка: очікується генератор."

    result = []
    for _ in range(count):
        result.append(next(gen))

    return result
