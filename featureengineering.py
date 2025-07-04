import pandas as pd

df = pd.read_csv("Dataset .csv")

df['Name Length'] = df['Restaurant Name'].astype(str).apply(len)

df['Address Length'] = df['Address'].astype(str).apply(len)

df['Has Table Booking'] = df['Has Table booking'].astype(str).str.strip().str.lower().map({'yes': 1, 'no': 0})

df['Has Online Delivery'] = df['Has Online delivery'].astype(str).str.strip().str.lower().map({'yes': 1, 'no': 0})

print("\n🔍 Feature Engineered Sample Data:")
print(df[['Restaurant Name', 'Name Length', 'Address Length', 'Has Table Booking', 'Has Online Delivery']].head())