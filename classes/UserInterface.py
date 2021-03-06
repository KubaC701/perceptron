from math import floor


class UserInterface:
  def input_car_data(self):
    car_horsepower = self.__input_data('Enter horsepower: ')
    car_weight = self.__input_data('Enter weight: ')

    return car_horsepower, car_weight

  def input_user_answer(self, prediction):
    if prediction > 0.5:
      self.__print_probability(prediction, 'Ferrari')
      expected = 1
    else:
      self.__print_probability(1 - prediction, 'Fiat')
      expected = 0
    answer = input('Was that true? y/n\n')
    return expected if answer == 'y' else 1 - expected

  @staticmethod
  def __input_data(label):
    data = input(label)

    return float(data) / 1000

  @staticmethod
  def __print_probability(prediction, manufacturer):
    percent = floor(prediction * 100)
    if percent < 70:
      print(
          f'I\'m not sure ({percent}%), but if I had to guess, I would say it\'s a {manufacturer}'
      )
    elif percent > 70 and percent < 90:
      print(f'I\'m pretty sure ({percent}%) it\'s a {manufacturer}')
    else:
      print(f'I\'m absolutely sure ({percent}%) it\'s a {manufacturer}')

  @staticmethod
  def print_menu():
    print('==================================')
    print('1. Enter car data')
    print('2. Let me learn')
    print('3. Quit')

  @staticmethod
  def handle_user_choice(enter_data_function, train_model_function):
    choice = input('Enter your choice: ')
    if choice == '1':
      enter_data_function()
      return 1
    if choice == '2':
      train_model_function()
      return 1
    if choice == '3':
      return 0
    return 1
