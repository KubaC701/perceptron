import pandas as pd
import copy
from constants.data import CAR_HORSEPOWER_COLUMN, CAR_WEIGHT_COLUMN, EXPECTED_COLUMN

from constants.files import DATA_CHART_FILE_NAME, DATA_FILE_NAME, TRAINING_LOSS_FILE_NAME


class DataManager:
    def __init__(self):
        self.data = self.read_file(DATA_FILE_NAME)

    @staticmethod
    def map_colors(x):
        return 'red' if x == 1 else 'blue'

    @staticmethod
    def compress_number(number):
        return number / 1000

    @staticmethod
    def decompress_number(number):
        return number * 1000

    def generate_loss_chart(self, epoch_loss):
        df = pd.DataFrame(epoch_loss)
        df_plot = df.plot(kind='line', grid=True).get_figure()
        df_plot.savefig(TRAINING_LOSS_FILE_NAME)

    def prepare_to_view(self):
        df = copy.deepcopy(self.data)
        df[CAR_HORSEPOWER_COLUMN] *= 1000
        df[CAR_WEIGHT_COLUMN] *= 1000
        return df

    def compress_to_calculate(self, data):
        new_data = data
        new_data[CAR_HORSEPOWER_COLUMN] /= 1000
        new_data[CAR_WEIGHT_COLUMN] /= 1000
        return new_data

    def generate_data_chart(self):
        data = self.prepare_to_view()
        df = pd.DataFrame(data)
        df_plot = df.plot.scatter(
            x=CAR_HORSEPOWER_COLUMN, y=CAR_WEIGHT_COLUMN, c=df[EXPECTED_COLUMN].map(self.map_colors)
        )
        fig = df_plot.get_figure()
        self.save_to_file(DATA_FILE_NAME)
        fig.savefig(DATA_CHART_FILE_NAME)

    def read_file(self, file_name):
        data = pd.read_csv(file_name)
        compressed_data = self.compress_to_calculate(data)
        self.data = compressed_data
        return compressed_data

    def append(self, params, expected):
        new_row = pd.DataFrame({
            CAR_HORSEPOWER_COLUMN: params[0],
            CAR_WEIGHT_COLUMN: params[1],
            EXPECTED_COLUMN: expected
        }, index=[len(self.data) - 1])
        self.data = pd.concat([self.data, new_row], ignore_index=True)

    def save_to_file(self, file_name):
        data = self.prepare_to_view()
        df = pd.DataFrame(data)
        df.to_csv(file_name, index=False)
