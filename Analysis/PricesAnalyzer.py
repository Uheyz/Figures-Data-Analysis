import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yaml
from myenv.constants import *
from Analysis.AnalyzerInterface import AnalyzerInterface


class PricesAnalyzer(AnalyzerInterface):
    def __init__(self, config_file='appsettings.yml'):

        with open(config_file, 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)
            self.excel_file = config['Files']['excel_file']

        self.df = pd.read_excel(self.excel_file)
        self.clean_data()

    def clean_data(self):
        self.df = self.df.dropna(subset=['Змея_1_цена', 'Змея_2_цена', 'Итог в цене'])

    def plot_scatter_comparison(self):
        plt.figure(figsize=(12, 6))
        sns.scatterplot(x='Змея_1_цена', y='Итог в цене', data=self.df, label='Змея 1')
        sns.scatterplot(x='Змея_2_цена', y='Итог в цене', data=self.df, label='Змея 2')
        plt.title(CORRELATION_MATRIX_PRICES_TITLE)
        plt.xlabel(CORRELATION_MATRIX_PRICES_XLABEL)
        plt.ylabel(CORRELATION_MATRIX_PRICES_YLABEL)
        plt.legend()
        plt.show()

    def compute_correlation(self):
        correlation_matrix = self.df[['Змея_1_цена', 'Змея_2_цена', 'Итог в цене']].corr()
        print(CORRELATION_MATRIX_PRICES_HEADER)
        print(correlation_matrix)
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5)
        plt.title(CORRELATION_MATRIX_PRICES_TITLE)
        plt.show()

    def analyze_data(self):
        self.plot_scatter_comparison()
        self.compute_correlation()

        mean_growth_large_small_prices = self.compute_average_growth_large_small_prices()
        mean_growth_equal_prices = self.compute_average_growth_equal_prices()

        print(f"Средний прирост для комбинации большой и маленькой цен: {mean_growth_large_small_prices}")
        print(f"Средний прирост для комбинации цен на одном уровне: {mean_growth_equal_prices}")

    def compute_average_growth_large_small_prices(self):
        mean_growth = (self.df['Итог в цене'] - (self.df['Змея_1_цена'] + self.df['Змея_2_цена'])).mean()
        return mean_growth

    def compute_average_growth_equal_prices(self):
        mean_growth = (self.df['Итог в цене'] - self.df['Змея_1_цена']).mean()
        return mean_growth

if __name__ == "__main__":
    analyzer = PricesAnalyzer()
    analyzer.analyze_data()
