import pandas as pd

# Create sample sales data
data = {
    "Product": ["Product A", "Product B", "Product C", "Product D", "Product E"] * 3,
    "Sales": [1200, 750, 950, 1300, 800, 1100, 900, 1350, 700, 820, 1250, 730, 910, 1450, 650],
    "Profit": [300, 150, 200, 350, 180, 290, 210, 320, 160, 190, 330, 170, 220, 400, 140],
    "Region": ["North", "South", "East", "West", "North", "South", "East", "West", "North", "South", "East", "West", "North", "South", "East"]
}

# Save data to CSV file
df = pd.DataFrame(data)
df.to_csv("sales_data.csv", index=False)
