import pandas as pd

df=pd.read_csv(r"C:\Users\Nazar\OneDrive\Desktop\masiv.csv", encoding="utf-8")

name = input("Введіть ім'я користувача: ")
df["Ім'я"] = df["Ім'я"].str.lower()
name = name.lower()
result = df[df["Ім'я"] == name]
if result.empty:
    print("Користувача з таким ім'ям не знайдено.")
else:
    print(result)