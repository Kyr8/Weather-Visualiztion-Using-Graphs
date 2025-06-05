import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from mpl_toolkits.mplot3d import Axes3D


df = pd.read_csv('weather_data.csv')

df['Date'] = pd.to_datetime(df['Date'])

df.fillna(df.mean(), inplace=True)

print(df.info())
print(df.head())


plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Temperature'], marker='o', linestyle='-', color='b')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Trends Over Time')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


plt.figure(figsize=(8,5))
sns.scatterplot(x=df['Temperature'], y=df['Humidity'], hue=df['WindSpeed'], palette='coolwarm')
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity (%)')
plt.title('Humidity vs Temperature')
plt.show()


fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['Temperature'], df['Humidity'], df['WindSpeed'], c=df['Temperature'], cmap='coolwarm')
ax.set_xlabel('Temperature (°C)')
ax.set_ylabel('Humidity (%)')
ax.set_zlabel('WindSpeed (km/h)')
ax.set_title('3D Weather Data Visualization')
plt.show()

fig = px.scatter_3d(df, x='Temperature', y='Humidity', z='WindSpeed', color='Temperature', title="Interactive 3D Weather Visualization")
fig.show()
