import numpy as np

from classes.DataManager import DataManager
from classes.Perceptron import Perceptron
from classes.UserInterface import UserInterface

rg = np.random.default_rng()

perceptron = Perceptron()
data_manager = DataManager()


data = data_manager.read_file("data/data.csv")

def manual_mode():
    while(True):
        user_interface = UserInterface()
        user_interface.print_menu()
        choice = user_interface.get_user_choice()
        if choice == '1':
            car_horsepower, car_weight = user_interface.input_car_data()
            params = [car_horsepower, car_weight]
            prediction = perceptron.make_prediction(params)
            expected = user_interface.input_user_answer(prediction)
            data_manager.append(params, expected)
            perceptron.handle_single_row(params, expected, prediction)
        elif choice == '2':
            auto_mode()
        elif choice == '3':
            break
    data_manager.generate_data_chart()


def auto_mode():
    perceptron.train_model(data)

manual_mode()



