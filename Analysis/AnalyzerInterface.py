from abc import ABC, abstractmethod

class AnalyzerInterface(ABC):
    @abstractmethod
    def plot_scatter_comparison(self):
        pass

    @abstractmethod
    def compute_correlation(self):
        pass

    @abstractmethod
    def analyze_data(self):
        pass

    @abstractmethod
    def clean_data(self):
        pass
