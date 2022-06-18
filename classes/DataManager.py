import pandas as pd
import copy


class DataManager:
    data = []

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
        df_plot = df.plot(kind="line", grid=True).get_figure()
        df_plot.savefig("charts/Training_Loss.png")

    def prepare_to_view(self):
        df = copy.deepcopy(pd.DataFrame(self.data))
        df['car_horsepower'] *= 1000
        df['car_weight'] *= 1000
        return df

    def compress_to_calculate(self, data):
        new_data = data
        new_data['car_horsepower'] /= 1000
        new_data['car_weight'] /= 1000
        return new_data

    def generate_data_chart(self):
        data = self.prepare_to_view()
        df = pd.DataFrame(data)
        df_plot = df.plot.scatter(
            x='car_horsepower', y='car_weight', c=df['expected'].map(self.map_colors)
        )
        fig = df_plot.get_figure()
        self.save_to_file("data/data.csv")
        fig.savefig("charts/chart.png")

    def read_file(self, file_name):
        data = pd.read_csv(file_name)
        compressed_data = self.compress_to_calculate(data)
        self.data = compressed_data
        return compressed_data

    def append(self, params, expected):
        new_row = pd.DataFrame({
            'car_horsepower': params[0],
            'car_weight': params[1],
            'expected': expected
        }, index=[len(self.data) - 1])
        self.data = pd.concat([self.data, new_row], ignore_index=True)

    def save_to_file(self, file_name):
        data = self.prepare_to_view()
        df = pd.DataFrame(data)
        df.to_csv(file_name, index=False)
