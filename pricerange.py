import pandas as pd

df = pd.read_csv("Dataset .csv")

print("\nUnique Price Ranges in the dataset:")
print(df['Price range'].unique())

most_common_range = df['Price range'].value_counts().idxmax()
print(f"\nMost common price range is: {most_common_range}")

price_range_ratings = {}

for price in sorted(df['Price range'].unique()):
    ratings = df[df['Price range'] == price]['Aggregate rating']
    avg = ratings.mean()
    price_range_ratings[price] = avg
    print(f"Average rating for Price Range {price}: {avg:.2f}")

best_range = max(price_range_ratings, key=price_range_ratings.get)
best_rating = price_range_ratings[best_range]
print(f"\nPrice Range with highest average rating is {best_range} ({best_rating:.2f})")

highest_row = df[df['Price range'] == best_range].sort_values(by='Aggregate rating', ascending=False).head(1)
rating_color = highest_row['Rating color'].values[0]

print(f"Color representing the highest average rating: {rating_color}")