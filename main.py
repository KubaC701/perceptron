import numpy as np

from classes.DataManager import DataManager
from classes.Perceptron import Perceptron
from classes.UserInterface import UserInterface

rg = np.random.default_rng()

perceptron = Perceptron()
data_manager = DataManager()
user_interface = UserInterface()

data = data_manager.read_file("data/data.csv")


def manual_mode():
    car_horsepower, car_weight = user_interface.input_car_data()
    params = [car_horsepower, car_weight]
    prediction = perceptron.make_prediction(params)
    expected = user_interface.input_user_answer(prediction)
    data_manager.append(params, expected)
    perceptron.handle_single_row(params, expected, prediction)


def auto_mode():
    perceptron.train_model(data)


def main():
    while(True):
        user_interface.print_menu()
        exit_code = user_interface.handle_user_choice(
            enter_data_function=manual_mode,
            train_model_function=auto_mode
        )
        if exit_code == 0:
            break
    data_manager.generate_data_chart()


main()
