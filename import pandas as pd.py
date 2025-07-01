import pandas as pd
import numpy as np

# Generate 12 quarters (Q1 2022 to Q4 2024)
quarters = pd.date_range(start='2022-01-01', periods=12, freq='Q')

# Define products and their life cycle phases
products = {
    'Catalyst 9300': 'Growth',
    'Catalyst 2960-X/XR': 'Maturity/Decline',
    'Meraki MR56': 'Early Growth'
}

# Define geographic regions
regions = ['North America', 'EMEA', 'APAC']

# Initialize an empty list to store the data
data = []

# Generate data for each product, region, and quarter
for product, phase in products.items():
    for region in regions:
        for quarter in quarters:
            if phase == 'Growth':
                sales = np.random.randint(2000, 6000)
            elif phase == 'Maturity/Decline':
                sales = np.random.randint(1000, 4000)
            elif phase == 'Early Growth':
                sales = np.random.randint(1500, 4500)

            if product == 'Meraki MR56':
                price = np.random.randint(700, 900)
            else:
                price = np.random.randint(300, 500)

            promotion = np.random.choice([0, 1], p=[0.7, 0.3])

            if quarter.quarter == 4:
                sales = int(sales * 1.2)

            data.append([quarter, product, region, sales, price, promotion])

# Convert the data into a DataFrame
columns = ['Date', 'Product_Category', 'Region', 'Sales', 'Price', 'Promotion']
df = pd.DataFrame(data, columns=columns)

# Save the DataFrame to a CSV file
df.to_csv('dummy_sales_data.csv', index=False)

# Preview the first few rows
df.head()