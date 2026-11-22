import pandas as pd

df = pd.read_csv(r"C:\Users\Nazar\OneDrive\Desktop\massive.txt", encoding="utf-8", sep=r"\s+", header=None)
series1 = df.iloc[:, 0]
series2 = df.iloc[:, 1]
series3 = df.iloc[:, 2]

result = set(series1) & set(series2) & set(series3)

with open(r"C:\Users\Nazar\OneDrive\Desktop\one.txt", "w", encoding="utf-8") as f:
    for number in sorted(result):
        f.write(str(number) + "\n")