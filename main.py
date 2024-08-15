import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

csv_output = pd.read_csv("C:/Users/harsh/Downloads/Rain&Water/Allahabad.csv")
data = {"rainfall": [], "waterlevel": []}

data["rainfall"] = csv_output["Rainfall"].to_list()
data["waterlevel"] = csv_output["Waterlevel"].to_list()

df = pd.DataFrame(data)

rain = df[["rainfall"]]  # Double Brackets for 2D structure
water = df["waterlevel"]  # Single brackets for 1D structure

rain_train, rain_test, water_train, water_test = train_test_split(
    rain, water, test_size=0.2, random_state=1
)

model = LinearRegression()
model.fit(rain_train, water_train)

water_prediction = model.predict(rain_test)
err_mean = mean_squared_error(water_test, water_prediction)

print(f"The mean squared error is {err_mean}")
print(f"Coefficient: {model.coef_[0]}")
print(f"Intercept: {model.intercept_}")

plt.scatter(rain, water, color="blue", label="Collected Data")
plt.plot(rain, model.predict(rain), color="red", label="Regression Line")
plt.title("Rainfall vs Water Level")
plt.xlabel("Rainfall (mm)")
plt.ylabel("Water Level (m)")
plt.legend()
plt.show()
