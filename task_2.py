class IncorrectVinNumber(Exception):

  def __init__(self, message):
    self.message = message


class IncorrectCarNumbers(Exception):

  def __init__(self, message):
    self.message = message


class Car():

  def __init__(self, model, vin, numbers):
    self.__vin_start_count = 1000000
    self.__vin_end_count = 9999999
    self.__numbers_len = 6
    self.model = model
    if self.__is_valid_vin(vin):
      self.__vin = vin
    if self.__is_valid_numbers(numbers):
      self.__numbers = numbers

  def __is_valid_vin(self, vin_number):
    if not isinstance(vin_number, int):
      raise IncorrectVinNumber(
          f'Некорректный тип vin номер. Должен быть "int", получен {type(vin_number)}'
      )
    elif self.__vin_start_count > vin_number or vin_number > self.__vin_end_count:
      raise IncorrectVinNumber(
          f'Неверный диапазон для vin номера. Должен быть в пределах от {self.__vin_start_count} до {self.__vin_end_count}. vin = {vin_number}'
      )
    else:
      return True

  def __is_valid_numbers(self, numbers):
    if not isinstance(numbers, str):
      raise IncorrectCarNumbers(
          f'Некорректный тип данных для номеров. Должен быть "str", получен {type(numbers)}'
      )
    elif len(numbers) != self.__numbers_len:
      raise IncorrectCarNumbers(
          f'Неверная длина номера. Должна быть ровно {self.__numbers_len} символов. Получено {len(numbers)} символов.'
      )
    else:
      return True


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
