from analysis.dataset import CsvDataset
from analysis.analyzer import Analyzer

dataset = CsvDataset.load(
    "data/experiments/background.csv"
)

result = Analyzer().analyze(dataset)

print(result)