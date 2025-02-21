from datetime import datetime, date  # Import both datetime and date
from pymongo import MongoClient
from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_replace, count

# Initialize Spark session
spark = SparkSession.builder \
    .appName("ETL Pipeline") \
    .getOrCreate()

# Read the CSV file
df = spark.read.csv("customers-1000.csv", header=True, inferSchema=True)

# Remove duplicates
df = df.dropDuplicates()

# Format phone numbers
df = df.withColumn("Phone 1", regexp_replace("Phone 1", "[^0-9]", ""))
df = df.withColumn("Phone 2", regexp_replace("Phone 2", "[^0-9]", ""))

# Fill missing values
df = df.fillna({"Phone 1": "N/A", "Phone 2": "N/A"})

# Show schema and first 5 rows
df.printSchema()
df.show(5)

# Number of clients per country
df_country = df.groupBy("Country").agg(count("Customer Id").alias("ClientCount"))
df_country.show()

# Convert Spark DataFrame to Pandas DataFrame
data = df.toPandas().to_dict("records")

# Convert datetime.date to datetime.datetime
for record in data:
    if isinstance(record["Subscription Date"], date):  # Use 'date' here
        record["Subscription Date"] = datetime.combine(
            record["Subscription Date"], datetime.min.time()
        )

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["customer_db"]
collection = db["customers"]

# Insert data into MongoDB
collection.insert_many(data)
print("Data successfully loaded into MongoDB!")