import numpy as np
import pandas as pd
from classes.NeuralNetwork import NeuralNetwork

rg = np.random.default_rng()


neural_network = NeuralNetwork()


def input_user_data():
    car_horsepower = input("Enter horsepowers: ")
    if(car_horsepower == 'q'):
        return None, None

    car_horsepower = float(car_horsepower) / 1000

    car_weight = input("Enter weight: ")
    if(car_weight == 'q'):
        return None, None

    car_weight = float(car_weight) / 1000

    return car_horsepower, car_weight


def manual_mode(epoch):
    while(True):

        car_horsepower, car_weight = input_user_data()

        if(not car_horsepower or not car_weight):
            break

        feature = [car_horsepower, car_weight]

        prediction = make_prediction(feature)
        if prediction == 1:
            print("Ferrari")
        else:
            print("Fiat")
        answer = input("Was that Ferrari? y/n")
        if answer == "y":
            expected = 1
        else:
            expected = 0

        perceptron.make_post_prediction_update(expected, prediction, feature)
        error_rate = errors / (len(df) * epoch)
        print_epoch(epoch, error_rate)
        update_arrays(car_horsepower, car_weight, expected, prediction)

        epoch += 1


def main():
    neural_network = NeuralNetwork()
    df = pd.read_csv("data/data.csv")
    neural_network.train_model(df)


main()
