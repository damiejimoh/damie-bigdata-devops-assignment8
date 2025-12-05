"""
Sample data generator for testing
"""
import csv

def generate_sample_data():
    """Generate sample CSV data"""
    data = [
        ['value'],
        [10],
        [20],
        [30],
        [40],
        [50]
    ]
    
    with open('data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    
    print("Sample data.csv created successfully!")

if __name__ == "__main__":
    generate_sample_data()