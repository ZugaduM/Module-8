import os.path


class UnAvailableFileName(Exception):
  def __init__(self, message, info):
    self.message = message
    self.info = info


class NotNatureNumber(Exception):
  def __init__(self, message, info):
    self.message = message
    self.info = info


def test_func(args):
  for key, value in args.items():
    if key == 'file_name':
      if os.path.isfile(value):
        with open(value, 'r') as file:
          print(file.read())
      else:
        raise UnAvailableFileName(f'File with name {value} is unavaililable', f'{key}:{value}')
    else:
      if isinstance(value, int):
        if value < 0:
          raise NotNatureNumber(f'Number {value} is not nature number', f'error because number have "{str(value)[0]}"')
        else:
          print(f'Number {round(value, 0)} is nature number')          

def main():
  try:
    test_func({'file_name':'test.txt'})
  except UnAvailableFileName as e:
    print(e.message)
    print(e.info)

  try:
    test_func({'value':-2})
  except NotNatureNumber as e:
    print(e.message)
    print(e.info)
  finally:
    print('Congratulation. We succesfully finished practice.')

main()
