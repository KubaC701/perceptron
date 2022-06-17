import numpy as np

rg = np.random.default_rng()


class Perceptron:
    def __init__(self, activation_function):
        self.activation_function = activation_function

    def prepare_row(self, row):
        params = row[:-1]
        expected = row[-1]
        return [params[0] / 1000, params[1] / 1000], expected

    def __get_weighted_sum(self, params, weights, bias):
        return np.dot(params, weights) + bias

    def make_prediction(self, params, weights, bias):
        w_sum = self.__get_weighted_sum(params, weights, bias)
        prediction = self.activation_function(w_sum)
        return prediction
