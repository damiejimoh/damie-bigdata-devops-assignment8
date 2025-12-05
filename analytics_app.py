"""
Simple Analytics Application
Performs basic statistical analysis on CSV data
"""
import pandas as pd
import sys

def load_and_analyze(file_path):
    """Load CSV and perform analytics"""
    try:
        # Read CSV file
        df = pd.read_csv(file_path)
        
        print("=" * 50)
        print("DATA ANALYTICS REPORT")
        print("=" * 50)
        print(f"\nDataset: {file_path}")
        print(f"Total Rows: {len(df)}")
        print(f"Columns: {', '.join(df.columns)}")
        
        # Analyze 'value' column
        if 'value' in df.columns:
            print("\n--- Statistics for 'value' column ---")
            print(f"Average: {df['value'].mean():.2f}")
            print(f"Sum: {df['value'].sum():.2f}")
            print(f"Min: {df['value'].min():.2f}")
            print(f"Max: {df['value'].max():.2f}")
            print(f"Median: {df['value'].median():.2f}")
            print(f"Std Dev: {df['value'].std():.2f}")
        
        print("\n--- First 5 Rows ---")
        print(df.head())
        
        print("\n" + "=" * 50)
        print("Analysis Complete!")
        print("=" * 50)
        
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found!")
        sys.exit(1)
    except Exception as e:
        print(f"Error during analysis: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    load_and_analyze("data.csv")