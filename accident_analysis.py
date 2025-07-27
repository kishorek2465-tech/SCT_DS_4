import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ✅ Load lightweight sample CSV
df = pd.read_csv('accidents_sample_light.csv')

# ✅ Create folder for plots
os.makedirs('plots', exist_ok=True)

# -------------------------------
# 1. Top 10 States with Most Accidents
top_states = df['State'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_states.values, y=top_states.index, palette='Reds_r')
plt.title('Top 10 States by Accident Count')
plt.xlabel('Number of Accidents')
plt.ylabel('State')
plt.tight_layout()
plt.savefig('plots/top_10_states.png')
plt.close()

# -------------------------------
# 2. Accidents by Hour of Day
df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce')
df['Hour'] = df['Start_Time'].dt.hour
hourly = df['Hour'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
sns.lineplot(x=hourly.index, y=hourly.values, marker='o')
plt.title('Accidents by Hour of Day')
plt.xlabel('Hour')
plt.ylabel('Number of Accidents')
plt.xticks(range(0, 24))
plt.tight_layout()
plt.savefig('plots/accidents_by_hour.png')
plt.close()

# -------------------------------
# 3. Top 10 Weather Conditions in Accidents
weather = df['Weather_Condition'].value_counts().head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=weather.values, y=weather.index, palette='coolwarm')
plt.title('Top 10 Weather Conditions in Accidents')
plt.xlabel('Number of Accidents')
plt.ylabel('Weather Condition')
plt.tight_layout()
plt.savefig('plots/accidents_by_weather.png')
plt.close()

# ✅ Done
print("✅ All 3 plots saved in 'plots/' folder.")
