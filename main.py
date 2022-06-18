import numpy as np

from classes.DataManager import DataManager
from classes.Perceptron import Perceptron
from classes.UserInterface import UserInterface

rg = np.random.default_rng()

perceptron = Perceptron()
data_manager = DataManager()


def manual_mode(should_generate_data=False):
    while(True):
        user_interface = UserInterface()
        car_horsepower, car_weight = user_interface.input_car_data()
        if not car_horsepower or not car_weight:
            break

        params = [car_horsepower, car_weight]
        prediction = perceptron.make_prediction(params)
        expected = user_interface.input_user_answer(prediction)
        data_manager.append(params, expected)
        perceptron.handle_single_row(params, expected, prediction)
    if should_generate_data:
        data_manager.generate_data_chart()


def auto_mode():
    data = data_manager.read_file("data/data.csv")
    perceptron.train_model(data)


def main():
    manual_mode()
    auto_mode()
    manual_mode(True)


main()
