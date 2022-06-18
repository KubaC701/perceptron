class UserInterface:
    def __input_data(self, label):
        data = input(label)

        return float(data) / 1000

    def input_car_data(self):
        car_horsepower = self.__input_data('Enter horsepower: ')
        car_weight = self.__input_data('Enter weight: ')

        return car_horsepower, car_weight

    def __print_probability(self, prediction, manufacturer):
        print(f"Probability of {manufacturer}: {round(prediction * 100)}%")

    def input_user_answer(self, prediction):
        if prediction > 0.5:
            self.__print_probability(prediction, 'Ferrari')
            expected = 1
        else:
            self.__print_probability(1 - prediction, 'Fiat')
            expected = 0
        answer = input("Was that true? y/n\n")
        return expected if answer == 'y' else 1 - expected

    def print_menu(self):
        print("==================================")
        print("1. Enter car data")
        print("2. Let me learn")
        print("3. Quit")

    def get_user_choice(self):
        choice = input("Enter your choice: ")
        return choice
