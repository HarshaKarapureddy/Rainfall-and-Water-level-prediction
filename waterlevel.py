import matplotlib.pyplot as plt
import pandas as pd

csv_output = pd.read_csv("Allahabad.csv")

csv_output["Date"] = pd.to_datetime(csv_output["Date"])

data = {
    "waterlevel": csv_output["Waterlevel"].to_list(),
    "date": csv_output["Date"].to_list(),
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 6))
plt.scatter(df["date"], df["waterlevel"], color="blue", label="Waterlevel Data")
plt.title("Waterlevel vs Date")
plt.xlabel("Date (YYYY/MM/DD)")
plt.ylabel("Waterlevel (m)")
plt.legend()
plt.show()
