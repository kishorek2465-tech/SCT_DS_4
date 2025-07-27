import pandas as pd

# Load only necessary columns and fewer rows
cols = ['State', 'Start_Time', 'Weather_Condition']
df = pd.read_csv('US_Accidents_March23.csv', usecols=cols, nrows=50000)

# Save the slimmed-down sample
df.to_csv('accidents_sample_light.csv', index=False)
print("✅ Light sample created: accidents_sample_light.csv")
