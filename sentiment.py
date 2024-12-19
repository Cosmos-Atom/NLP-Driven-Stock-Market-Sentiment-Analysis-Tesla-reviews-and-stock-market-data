import mysql.connector
from textblob import TextBlob  # You can install this with `pip install textblob`

# Database connection configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "ish@sql",  # Replace with your actual password
    "database": "dbmsstock"     # Replace with your database name
}

# Connect to the database
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Fetch data from 'newstable' - Select the 'id' and 'content' columns
cursor.execute("SELECT id, content FROM newstable")
rows = cursor.fetchall()

# Perform sentiment analysis using TextBlob (without preprocessing)
def get_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity  # Returns a float between -1 (negative) and 1 (positive)
    
    # Print the sentiment score
    print(f"Sentiment Score: {sentiment_score}")
    
    # Threshold to classify as positive or negative (e.g., > 0 is positive, <= 0 is negative)
    if sentiment_score > 0:
        return 'positive'
    else:
        return 'negative'

# Process each row to determine sentiment and print the sentiment score
sentiments = []
for row in rows:
    content = row[1]  # content column
    sentiment = get_sentiment(content)
    sentiments.append((row[0], sentiment))  # (id, sentiment)

# Print all sentiments for review
print("\nSentiment Results (id, sentiment):")
for sentiment_data in sentiments:
    print(sentiment_data)

# Close the connection
cursor.close()
conn.close()

print("Sentiment analysis completed and results printed!")
