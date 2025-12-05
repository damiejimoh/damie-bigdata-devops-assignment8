"""
PySpark ETL Job for Big Data Processing
Author: BDAT1008 DevOps Team
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, sum, count

def create_spark_session():
    """Initialize Spark Session"""
    spark = SparkSession.builder \
        .appName("BigDataPipeline") \
        .getOrCreate()
    return spark

def load_data(spark, file_path):
    """Load CSV data into Spark DataFrame"""
    df = spark.read.csv(file_path, header=True, inferSchema=True)
    return df

def perform_analytics(df):
    """Perform basic analytics on data"""
    print("=== Data Analytics Results ===")
    
    # Show sample data
    df.show(5)
    
    # Calculate statistics
    stats = df.select(
        avg("value").alias("average"),
        sum("value").alias("total"),
        count("value").alias("count")
    ).collect()[0]
    
    print(f"Average: {stats['average']}")
    print(f"Total Sum: {stats['total']}")
    print(f"Count: {stats['count']}")
    
    return stats

def main():
    """Main ETL pipeline"""
    spark = create_spark_session()
    
    # Load data
    df = load_data(spark, "data/input.csv")
    
    # Perform analytics
    perform_analytics(df)
    
    spark.stop()

if __name__ == "__main__":
    main()