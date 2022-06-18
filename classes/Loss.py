import numpy as np

from classes.DataManager import DataManager


class Loss:
    def __init__(self):
        self.individual_loss = []
        self.epoch_loss = []

    @staticmethod
    def __cross_entropy(expected, prediction):
        return -(expected*np.log10(prediction) + (1-expected)*np.log10(1-prediction))

    def __get_average_loss(self):
        return sum(self.individual_loss)/len(self.individual_loss)

    def add_individual_loss(self, expected, prediction):
        loss = self.__cross_entropy(expected, prediction)
        self.individual_loss.append(loss)

    def add_epoch_loss(self):
        average_loss = self.__get_average_loss()
        self.epoch_loss.append(average_loss)
        return average_loss

    def generate_loss_chart(self):
        DataManager.generate_loss_chart(self.epoch_loss)
