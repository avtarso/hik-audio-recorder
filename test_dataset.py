from analysis.dataset import CsvDataset

dataset = CsvDataset.load(
    "data/experiments/background.csv"
)

print(f"Frames      : {dataset.frames}")
print(f"Duration    : {dataset.duration:.2f}")
print(f"FPS         : {dataset.fps:.2f}")
print(f"Sample Rate : {dataset.sample_rate}")
print(f"Frame Size  : {dataset.frame_size}")

print()
print(dataset.rms[:5])