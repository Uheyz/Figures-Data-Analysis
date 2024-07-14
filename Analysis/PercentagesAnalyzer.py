import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yaml
from myenv.constants import *
from Analysis.AnalyzerInterface import AnalyzerInterface
class PercentagesAnalyzer(AnalyzerInterface):
    def __init__(self, config_file='appsettings.yml'):
        with open(config_file, 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)
            self.excel_file = config['Files']['excel_file']

        self.df = pd.read_excel(self.excel_file)
        self.clean_data()

    def clean_data(self):
        self.df = self.df.dropna(subset=['Змея_1_процент', 'Змея_2_процент', 'Итог в %'])

    def plot_scatter_comparison(self):
        plt.figure(figsize=(12, 6))
        sns.scatterplot(x='Змея_1_процент', y='Итог в %', data=self.df, label='Змея 1')
        sns.scatterplot(x='Змея_2_процент', y='Итог в %', data=self.df, label='Змея 2')
        plt.title(CORRELATION_MATRIX_PERCENTAGES_TITLE)
        plt.xlabel(CORRELATION_MATRIX_PERCENTAGES_XLABEL)
        plt.ylabel(CORRELATION_MATRIX_PERCENTAGES_YLABEL)
        plt.legend()
        plt.show()

    def compute_correlation(self):
        correlation_matrix = self.df[['Змея_1_процент', 'Змея_2_процент', 'Итог в %']].corr()
        print(CORRELATION_MATRIX_PERCENTAGES_HEADER)
        print(correlation_matrix)
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5)
        plt.title(CORRELATION_MATRIX_PERCENTAGES_TITLE)
        plt.show()

    def analyze_data(self):
        self.plot_scatter_comparison()
        self.compute_correlation()

        mean_growth_large_small_percentages = self.compute_average_growth_large_small_percentages()
        mean_growth_equal_percentages = self.compute_average_growth_equal_percentages()

        print(f"{MEAN_GROWTH_LARGE_SMALL_PERCENTAGES}: {mean_growth_large_small_percentages}")
        print(f"{MEAN_GROWTH_EQUAL_PERCENTAGES}: {mean_growth_equal_percentages}")

    def compute_average_growth_large_small_percentages(self):
        mean_growth = (self.df['Итог в %'] - (self.df['Змея_1_процент'] + self.df['Змея_2_процент'])).mean()
        return mean_growth

    def compute_average_growth_equal_percentages(self):
        mean_growth = (self.df['Итог в %'] - self.df['Змея_1_процент']).mean()
        return mean_growth

if __name__ == "__main__":
    analyzer = PercentagesAnalyzer()
    analyzer.analyze_data()
