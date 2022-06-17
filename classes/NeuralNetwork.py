import numpy as np
from .Chart import Chart
from .Loss import Loss
from .Perceptron import Perceptron

rg = np.random.default_rng()


class NeuralNetwork:
    def __init__(self, epochs=1000, learning_rate=0.1):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = self.generate_weights(2)
        self.bias = 0.5

    loss = Loss()

    def __update_bias(self, target, prediction):
        self.bias = self.bias + self.learning_rate*(target-prediction)

    def __sigmoid(self, w_sum):
        return 1/(1+np.exp(-w_sum))

    def generate_weights(self, n_values):
        weights = rg.random((1, n_values))[0]
        return weights

    def __update_weights(self, target, prediction, params):
        new_weights = []
        for x, w in zip(params, self.weights):
            new_w = w + self.learning_rate*(target-prediction)*x
            new_weights.append(new_w)
        self.weights = new_weights

    def make_post_prediction_update(self, expected, prediction, params):
        self.__update_weights(expected, prediction, params)
        self.__update_bias(expected, prediction)

    def __print_epoch(self, epoch, average_loss):
        print("==================================")
        print("epoch", epoch)
        print("error rate: ", average_loss)

    def train_model(self, data):
        perceptron = Perceptron(self.__sigmoid)

        for epoch in range(self.epochs):

            for i in range(len(data)):
                params, expected = perceptron.prepare_row(data.loc[i])
                prediction = perceptron.make_prediction(
                    params, self.weights, self.bias)
                self.loss.add_individual_loss(expected, prediction)

                self.make_post_prediction_update(expected, prediction, params)

            average_loss = self.loss.add_epoch_loss()
            self.__print_epoch(epoch + 1, average_loss)
        self.generate_loss_chart()

    def generate_loss_chart(self):
        chart = Chart()

        chart.generate_loss_chart(self.loss.epoch_loss)
