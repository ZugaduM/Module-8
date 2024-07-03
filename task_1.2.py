def personal_sum(numbers):
  result = 0
  incorrect_data = 0
  for value in numbers:
    try:
      isinstance(value, int)
      result += value
    except TypeError:
      incorrect_data += 1
      print(f'Некорректный тип данных для подсчёта суммы - {value}')
  return (result, incorrect_data)


def calculate_average(numbers):
  count = 0
  try:
    isinstance(numbers, tuple or list)
    values = personal_sum(numbers)
    for i in numbers:
      if isinstance(i, int):
        count += 1
    return values[0] / count
  except ZeroDivisionError:
    return 0
  except TypeError:
    print('В numbers записан некорректный тип данных.')
    return None


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
