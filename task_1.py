def add_everything_up(a, b):
  try:
    if isinstance(a, str) or isinstance(b, str):
      return a + b
    else:
      return round(a + b, 3)
  except TypeError:
    return f'{a}{b}'


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
