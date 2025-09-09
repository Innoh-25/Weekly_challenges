import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from pathlib import Path

def create_sample_csv():
    """Create a sample sales_data.csv file in the root directory if it doesn't exist"""
    script_dir = Path(__file__).parent
    root_dir = script_dir.parent
    csv_path = root_dir / 'sales_data.csv'
    
    if not csv_path.exists():
        print("Creating sample sales_data.csv file...")
        sample_data = {
            'Date': ['2025-03-01', '2025-03-01', '2025-03-02', '2025-03-02', 
                     '2025-03-03', '2025-03-03', '2025-03-04', '2025-03-04',
                     '2025-03-05', '2025-03-05'],
            'Product': ['Laptop', 'Mouse', 'Laptop', 'Keyboard', 
                       'Mouse', 'Monitor', 'Laptop', 'Mouse',
                       'Keyboard', 'Monitor'],
            'Quantity Sold': [5, 15, 3, 8, 12, 4, 6, 10, 7, 3],
            'Revenue ($)': [5000, 300, 3000, 800, 240, 1200, 6000, 200, 700, 900]
        }
        
        df = pd.DataFrame(sample_data)
        df.to_csv(csv_path, index=False)
        print(f"✅ Sample {csv_path} created successfully!")
    else:
        print(f"✅ {csv_path} already exists.")

def perform_data_analysis():
    try:
        # Get the path to the CSV file in the root directory
        script_dir = Path(__file__).parent
        root_dir = script_dir.parent
        csv_path = root_dir / 'sales_data.csv'
        
        # Load the CSV file
        print(f"Loading {csv_path}...")
        df = pd.read_csv(csv_path)
        
        # Display basic information about the data
        print("\nData Overview:")
        print(f"Total records: {len(df)}")
        print(f"Columns: {list(df.columns)}")
        print("\nFirst 5 rows:")
        print(df.head())
        
        # Calculate total revenue
        total_revenue = df['Revenue ($)'].sum()
        
        # Find best-selling product (based on Quantity Sold)
        product_sales = df.groupby('Product')['Quantity Sold'].sum()
        best_selling_product = product_sales.idxmax()
        best_selling_quantity = product_sales.max()
        
        # Find day with highest sales (total revenue per day)
        daily_sales = df.groupby('Date')['Revenue ($)'].sum()
        highest_sales_day = daily_sales.idxmax()
        highest_sales_amount = daily_sales.max()
        
        # Prepare insights for output
        insights = {
            'Total Revenue': f"${total_revenue:,.2f}",
            'Best-Selling Product': f"{best_selling_product} ({best_selling_quantity} units sold)",
            'Highest Sales Day': f"{highest_sales_day} (${highest_sales_amount:,.2f})"
        }
        
        # Save results to text file in the same directory as script
        output_path = script_dir / 'sales_summary.txt'
        with open(output_path, 'w') as file:
            file.write("SALES ANALYSIS SUMMARY\n")
            file.write("=" * 25 + "\n\n")
            file.write(f"Total Revenue: ${total_revenue:,.2f}\n")
            file.write(f"Best-Selling Product: {best_selling_product} ({best_selling_quantity} units sold)\n")
            file.write(f"Highest Sales Day: {highest_sales_day} (${highest_sales_amount:,.2f})\n\n")
            
            # Additional insights
            file.write("ADDITIONAL INSIGHTS\n")
            file.write("=" * 20 + "\n")
            file.write(f"Total Products Sold: {df['Quantity Sold'].sum()} units\n")
            file.write(f"Average Revenue per Sale: ${df['Revenue ($)'].mean():.2f}\n")
            file.write(f"Number of Unique Products: {df['Product'].nunique()}\n")
        
        # Print insights in user-friendly format
        print("\n" + "=" * 50)
        print("SALES ANALYSIS INSIGHTS")
        print("=" * 50)
        print(f"📊 Total Revenue: ${total_revenue:,.2f}")
        print(f"🏆 Best-Selling Product: {best_selling_product} ({best_selling_quantity} units)")
        print(f"📈 Highest Sales Day: {highest_sales_day} (${highest_sales_amount:,.2f})")
        print(f"📦 Total Units Sold: {df['Quantity Sold'].sum():,}")
        print(f"💰 Average Revenue per Sale: ${df['Revenue ($)'].mean():.2f}")
        print("=" * 50)
        
        print(f"\n✅ Results saved to '{output_path}'")
        
        # BONUS: Visualizations
        create_visualizations(df, daily_sales, product_sales, script_dir)
        
    except FileNotFoundError:
        print("❌ Error: sales_data.csv file not found!")
        print("Please make sure the file exists in the root directory.")
    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")

def create_visualizations(df, daily_sales, product_sales, output_dir):
    """Create visualizations for sales trends"""
    print("\n📊 Creating visualizations...")
    
    # Set up the plotting style
    plt.style.use('seaborn-v0_8')
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Sales Data Analysis Dashboard', fontsize=16, fontweight='bold')
    
    # 1. Daily Revenue Trend
    daily_sales.plot(kind='line', marker='o', ax=ax1, color='royalblue')
    ax1.set_title('Daily Revenue Trend', fontweight='bold')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Revenue ($)')
    ax1.tick_params(axis='x', rotation=45)
    ax1.grid(True, alpha=0.3)
    
    # 2. Product Sales Distribution
    product_sales.plot(kind='bar', ax=ax2, color='lightcoral')
    ax2.set_title('Total Units Sold by Product', fontweight='bold')
    ax2.set_xlabel('Product')
    ax2.set_ylabel('Quantity Sold')
    ax2.tick_params(axis='x', rotation=45)
    
    # 3. Revenue by Product
    revenue_by_product = df.groupby('Product')['Revenue ($)'].sum()
    revenue_by_product.plot(kind='bar', ax=ax3, color='mediumseagreen')
    ax3.set_title('Total Revenue by Product', fontweight='bold')
    ax3.set_xlabel('Product')
    ax3.set_ylabel('Revenue ($)')
    ax3.tick_params(axis='x', rotation=45)
    
    # 4. Pie chart of revenue distribution
    ax4.pie(revenue_by_product.values, labels=revenue_by_product.index, 
            autopct='%1.1f%%', startangle=90, colors=plt.cm.Set3.colors)
    ax4.set_title('Revenue Distribution by Product', fontweight='bold')
    
    plt.tight_layout()
    
    # Save visualization in the script directory
    viz_path = output_dir / 'sales_analysis_dashboard.png'
    plt.savefig(viz_path, dpi=300, bbox_inches='tight')
    plt.show()
    
    print(f"✅ Visualizations saved as '{viz_path}'")

# Additional analysis functions
def generate_detailed_report():
    """Generate a more detailed analysis report"""
    try:
        script_dir = Path(__file__).parent
        root_dir = script_dir.parent
        csv_path = root_dir / 'sales_data.csv'
        
        df = pd.read_csv(csv_path)
        
        # Convert Date to datetime for better analysis
        df['Date'] = pd.to_datetime(df['Date'])
        
        print("\n📋 DETAILED ANALYSIS REPORT")
        print("=" * 40)
        
        # Weekly analysis
        df['Week'] = df['Date'].dt.isocalendar().week
        weekly_sales = df.groupby('Week')['Revenue ($)'].sum()
        print(f"Weekly Revenue Peak: Week {weekly_sales.idxmax()} (${weekly_sales.max():,.2f})")
        
        # Product performance
        product_stats = df.groupby('Product').agg({
            'Quantity Sold': 'sum',
            'Revenue ($)': 'sum'
        }).sort_values('Revenue ($)', ascending=False)
        
        print("\nProduct Performance Ranking:")
        for i, (product, stats) in enumerate(product_stats.iterrows(), 1):
            print(f"{i}. {product}: {stats['Quantity Sold']} units, ${stats['Revenue ($)']:,.2f}")
            
    except Exception as e:
        print(f"Error generating detailed report: {e}")

if __name__ == "__main__":
    # Create the sample CSV file in root directory if it doesn't exist
    create_sample_csv()
    
    # Perform the main analysis
    perform_data_analysis()
    
    # Generate detailed report
    generate_detailed_report()