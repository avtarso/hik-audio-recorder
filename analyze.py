from pathlib import Path
import argparse

import matplotlib.pyplot as plt

from analysis.dataset import CsvDataset
from analysis.analyzer import Analyzer
from analysis.report import ConsoleReport


def plot_rms(dataset: CsvDataset, output: Path) -> None:

    plt.figure(figsize=(12, 4))

    plt.plot(
        dataset.timestamps,
        dataset.rms,
        linewidth=0.8,
    )

    plt.title("RMS over time")
    plt.xlabel("Time (sec)")
    plt.ylabel("RMS")
    plt.grid(True)

    plt.tight_layout()

    plt.savefig(output, dpi=150)

    print(f"\nGraph saved to: {output}")

    plt.close()


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "csv",
        type=Path,
        help="CSV file produced by CsvRecorder",
    )

    args = parser.parse_args()

    dataset = CsvDataset.load(args.csv)

    result = Analyzer().analyze(dataset)

    ConsoleReport.print(result)

    output = args.csv.with_suffix(".png")

    plot_rms(dataset, output)


if __name__ == "__main__":
    main()