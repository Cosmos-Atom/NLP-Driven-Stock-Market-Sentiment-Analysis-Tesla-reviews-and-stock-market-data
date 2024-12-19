# NLP-Driven-Stock-Market-Sentiment-Analysis-Tesla-reviews-and-stock-market-data

Overview

This project analyzes public sentiment surrounding Tesla (TSLA) by collecting textual data from platforms like Reddit, YouTube, and news articles. The sentiment is evaluated using Natural Language Processing (NLP) and the TextBlob library in Python. The sentiment scores are compared with Tesla's stock prices over the same period to identify correlations. The results are displayed on a web interface built using Flask, with an admin dashboard and user view. MySQL is used to manage and preprocess the data.

Features
Text Data Collection: Collects Tesla-related data from Reddit, YouTube, and news articles through APIs.
Sentiment Analysis: Uses TextBlob to perform sentiment analysis on the collected textual data.
Stock Market Comparison: Compares sentiment scores with Tesla's stock prices over the same period.
Data Visualization: Visualizes sentiment trends and stock price movements.
Flask Web Interface: Displays the analysis results through an interactive web interface with an admin dashboard and user view.
MySQL Integration: Manages and preprocesses data using MySQL.


Prerequisites
Before running this project, ensure you have the following installed:

Python 3.x
MySQL Database
Flask
TextBlob
Other dependencies in requirements.txt
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/tesla-sentiment-analysis.git
cd tesla-sentiment-analysis

Install the required Python libraries:
bash
Copy code
pip install -r requirements.txt

Set up the MySQL database:
Create a MySQL database and tables for storing the data using the sql file available.

Run the Flask application:
bash
Copy code
python app.py
Access the application:
Open your browser and go to http://127.0.0.1:5000 to view the app.

Usage
Admin Dashboard: The admin dashboard allows you to manage the data collection process and review sentiment analysis results.
User View: The user view displays the sentiment analysis results and stock price comparisons in an easy-to-understand format.

If you need the code for Data Collection: ping me on kavyasreekammari2090@gmail.com with proper details

Sentiment Analysis
TextBlob is used to calculate sentiment scores based on the collected textual data. Positive, neutral, and negative sentiments are classified, and the corresponding sentiment score is stored in the database.
