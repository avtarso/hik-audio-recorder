from __future__ import annotations

from .analyzer import AnalysisResult


class ConsoleReport:

    @staticmethod
    def print(result: AnalysisResult) -> None:

        print()

        print("=" * 60)
        print("DATASET")
        print("=" * 60)

        print(f"Frames       : {result.frames}")
        print(f"Duration     : {result.duration:.2f} sec")
        print(f"FPS          : {result.fps:.2f}")

        print()

        print(f"Sample Rate  : {result.sample_rate}")
        print(f"Frame Size   : {result.frame_size}")

        print()

        print("-" * 60)
        print("RMS")
        print("-" * 60)

        print(f"Mean         : {result.rms_mean:.6f}")
        print(f"Median       : {result.rms_median:.6f}")
        print(f"Std          : {result.rms_std:.6f}")
        print(f"Min          : {result.rms_min:.6f}")
        print(f"Max          : {result.rms_max:.6f}")
        print(f"P95          : {result.rms_p95:.6f}")
        print(f"P99          : {result.rms_p99:.6f}")

        print()

        print("-" * 60)
        print("PEAK")
        print("-" * 60)

        print(f"Mean         : {result.peak_mean:.6f}")
        print(f"Max          : {result.peak_max:.6f}")

        print()

        print("-" * 60)
        print("ZERO CROSSINGS")
        print("-" * 60)

        print(f"Mean         : {result.zero_crossings_mean:.2f}")
        print(f"Std          : {result.zero_crossings_std:.2f}")

        print()

        print("=" * 60)