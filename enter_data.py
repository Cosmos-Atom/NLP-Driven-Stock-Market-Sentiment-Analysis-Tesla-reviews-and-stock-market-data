import pandas as pd
import mysql.connector

# Read the CSV file into a DataFrame
csv_file = 'sentiment_review_weekly.csv'  # Replace with your actual CSV file name
df = pd.read_csv(csv_file)

# Connect to MySQL
db_connection = mysql.connector.connect(
    host="localhost",           # MySQL host (localhost for local)
    user="kavya_dbms",          # Your MySQL username
    password="kavyasree",       # Your MySQL password
    database="tesla_app"        # Your database name
)

cursor = db_connection.cursor()

# Iterate over the DataFrame and insert data into the table
for index, row in df.iterrows():
    # Insert data into the avg_sentiment_table
    cursor.execute("""
        INSERT INTO avg_sentiment_table (date, avg_sentiment_score)
        VALUES (%s, %s)
    """, (row['date'], row['avg(sentiment_score)']))

# Commit the transaction and close the connection
db_connection.commit()
cursor.close()
db_connection.close()

print("Data inserted successfully into avg_sentiment_table")
