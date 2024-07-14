from Analysis.PricesAnalyzer import PricesAnalyzer
from Analysis.PercentagesAnalyzer import PercentagesAnalyzer

if __name__ == "__main__":
    config_file = 'C:/Users/leona/PycharmProjects/pythonProject1/appsettings.yml'

    prices_analyzer = PricesAnalyzer(config_file)
    prices_analyzer.analyze_data() 

    percentages_analyzer = PercentagesAnalyzer(config_file)
    percentages_analyzer.analyze_data() 