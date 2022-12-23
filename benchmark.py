import importlib
import pkgutil
import time
from tqdm import tqdm

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import aoc


def benchmark(func: callable, file_path: str, seconds=3) -> list:

    times = []

    start = time.time()

    while time.time() - start < seconds:
        times.append(time_function(func, file_path))

    return times


def time_function(func: callable, file_path: str) -> float:

    start = time.time()
    func(file_path)
    return time.time() - start


def get_modules():
    modules = [name for _, name, _ in pkgutil.iter_modules(["aoc"])]
    module_dict = {}
    for module_str in modules:
        module = importlib.import_module(f"aoc.{module_str}", package=aoc)
        func_1 = getattr(module, "part_one")
        func_2 = getattr(module, "part_two")
        file_path = f"aoc/inputs/{module_str}.txt"
        module_dict[f"{module_str}-pt1"] = (func_1, file_path)
        module_dict[f"{module_str}-pt2"] = (func_2, file_path)
    return module_dict


def run_benchmarks(seconds=3):

    module_dict = get_modules()

    for key, value in tqdm(module_dict.items()):
        module_dict[key] = benchmark(*value, seconds=seconds)

    return pd.DataFrame.from_dict(module_dict, orient="index")


def save_figure(df):

    df = df.T.melt(var_name="function", value_name="runtime").dropna()
    df["day"] = df["function"].str.slice(4, 6).apply(int)
    df["part"] = df["function"].str.slice(-1).apply(int)

    plt.clf()
    plt.figure(figsize=(15, 10))

    s = sns.boxplot(
        df, palette="hls", x="day", y="runtime", hue="part", showfliers=False
    )
    s.set_ylabel("Run time (s)")
    s.set_yscale("log")
    s.set_title("Solution run times")

    return plt.savefig("benchmark.png")


if __name__ == "__main__":
    df = run_benchmarks(seconds=3)
    save_figure(df)
