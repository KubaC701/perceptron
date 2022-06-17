import pandas as pd


class Chart:

    def generate_loss_chart(self, epoch_loss):
        df = pd.DataFrame(epoch_loss)
        df_plot = df.plot(kind="line", grid=True).get_figure()
        df_plot.savefig("charts/Training_Loss.png")

    def __map_colors(x):
        return 'red ' if x == 1 else 'blue'

    def generate_data_chart(self, data):
        df = pd.DataFrame(data)

        df_plot = df.plot.scatter(
            x='car_horsepower', y='car_weight', c=df['expected'].map(self.__map_colors))
        fig = df_plot.get_figure()

        fig.savefig("charts/chart.png")

    # def generate_file():
    #     df.to_csv("data/results.csv")
