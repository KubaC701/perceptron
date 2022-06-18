import numpy as np

from classes.Loss import Loss

rg = np.random.default_rng()


def sigmoid(w_sum):
    return 1/(1+np.exp(-w_sum))


class Perceptron:
    def __init__(self, epochs=1000, learning_rate=0.1, activation_function=sigmoid):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = self.__generate_weights(2)
        self.bias = 0.5
        self.activation_function = activation_function
        self.loss = Loss()

    @staticmethod
    def __generate_weights(n_values):
        weights = rg.random((1, n_values))[0]
        return weights

    @staticmethod
    def __prepare_row(row):
        params = row[:-1]
        expected = row[-1]
        return [params[0], params[1]], expected

    @staticmethod
    def __print_epoch(current_epoch, average_loss):
        print('==================================')
        print('epoch', current_epoch)
        print('error rate: ', average_loss)

    def __get_weighted_sum(self, params):
        return np.dot(params, self.weights) + self.bias

    def __update_bias(self, expected, prediction):
        return self.bias + self.learning_rate*(expected-prediction)

    def __update_weights(self, expected, prediction, params):
        new_weights = []
        for x, w in zip(params, self.weights):
            new_w = w + self.learning_rate*(expected-prediction)*x
            new_weights.append(new_w)
        return new_weights

    def __make_post_prediction_update(self, expected, prediction, params):
        self.weights = self.__update_weights(expected, prediction, params)
        self.bias = self.__update_bias(expected, prediction)

    def make_prediction(self, params):
        w_sum = self.__get_weighted_sum(params)
        prediction = self.activation_function(w_sum)
        return prediction

    def handle_single_row(self, params, expected, prediction):
        self.loss.add_individual_loss(expected, prediction)
        self.__make_post_prediction_update(expected, prediction, params)

    def train_model(self, data):
        for epoch in range(self.epochs):
            for i in range(len(data)):
                params, expected = self.__prepare_row(data.loc[i])
                prediction = self.make_prediction(params)
                self.handle_single_row(params, expected, prediction)
            average_loss = self.loss.add_epoch_loss()
            self.__print_epoch(epoch + 1, average_loss)
        self.loss.generate_loss_chart()
