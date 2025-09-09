import pandas as pd

# Create sample data
data = {
    'Date': ['2025-03-01', '2025-03-01', '2025-03-02', '2025-03-02', 
             '2025-03-03', '2025-03-03', '2025-03-04'],
    'Product': ['Laptop', 'Mouse', 'Laptop', 'Keyboard', 
                'Mouse', 'Monitor', 'Laptop'],
    'Quantity Sold': [5, 15, 3, 8, 12, 4, 6],
    'Revenue ($)': [5000, 300, 3000, 800, 240, 1200, 6000]
}

# Create DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv('sales_data.csv', index=False)
print("sales_data.csv created successfully!")