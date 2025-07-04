import pandas as pd

df = pd.read_csv("Dataset .csv")

print("Column names:", df.columns.tolist())

df['Has Table booking'] = df['Has Table booking'].astype(str).str.strip().str.lower()
df['Has Online delivery'] = df['Has Online delivery'].astype(str).str.strip().str.lower()

table_booking_percent = (df['Has Table booking'].value_counts().get('yes', 0) / len(df)) * 100
print(f"\n Percentage of restaurants that offer table booking: {table_booking_percent:.2f}%")

online_delivery_percent = (df['Has Online delivery'].value_counts().get('yes', 0) / len(df)) * 100
print(f" Percentage of restaurants that offer online delivery: {online_delivery_percent:.2f}%")

avg_with_booking = df[df['Has Table booking'] == 'yes']['Aggregate rating'].mean()
avg_without_booking = df[df['Has Table booking'] == 'no']['Aggregate rating'].mean()
print(f"\n Average rating (with table booking): {avg_with_booking:.2f}")
print(f" Average rating (without table booking): {avg_without_booking:.2f}")

delivery_by_price = df[df['Has Online delivery'] == 'yes'].groupby('Price range').size()
total_by_price = df.groupby('Price range').size()
delivery_percentage = (delivery_by_price / total_by_price) * 100
delivery_percentage = delivery_percentage.fillna(0).round(2)

print("\n Online delivery availability by Price range (%):")
print(delivery_percentage)