import matplotlib.pyplot as plt
import pandas as pd

csv_output = pd.read_csv("Mirzapur.csv")

csv_output["Date"] = pd.to_datetime(csv_output["Date"])

data = {
    "rainfall": csv_output["Rainfall"].to_list(),
    "date": csv_output["Date"].to_list(),
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 6))
plt.scatter(df["date"], df["rainfall"], color="blue", label="Rainfall Data")
plt.title("Rainfall vs Date")
plt.xlabel("Date (YYYY/MM/DD)")
plt.ylabel("Rainfall (mm)")
plt.legend()
plt.show()
