from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from textblob import TextBlob
import mysql.connector
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key'

db_config = {
    'host': 'localhost',
    'user': 'kavya_dbms',
    'password': 'kavyasree',
    'database': 'tesla_app'
}

@app.route('/')
def home():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    query = """
        SELECT review, sentiment_score
        FROM review_auto_date
        WHERE sentiment_score > 0.4
        AND LENGTH(TRIM(review)) - LENGTH(REPLACE(review, ' ', '')) + 1 > 15
        ORDER BY sentiment_score DESC
        LIMIT 4;
    """
    cursor.execute(query)
    reviews = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('index.html', reviews=reviews)


@app.route('/submit_review', methods=['POST'])
def submit_review():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        review_text = request.form['reviewText']
        if not review_text.strip():
            return "Error: Review cannot be empty", 400

        sentiment = TextBlob(review_text).sentiment.polarity

        query = """
        INSERT INTO review_auto_date (review, sentiment_score)
        VALUES (%s, %s)
        """
        cursor.execute(query, (review_text, sentiment))
        conn.commit()

        return redirect(url_for('home'))

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return "Database error occurred", 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return render_template('login.html', error_message="Invalid email format.", email=email)

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM UserCredentials WHERE email = %s", (email,))
        user = cursor.fetchone()

        if not user:
            cursor.close()
            conn.close()
            return render_template('login.html', error_message="No admin found with this email.", email=email)

        if user[2] != password:
            cursor.close()
            conn.close()
            return render_template('login.html', error_message="Incorrect password.", email=email)

        session['user_id'] = user[0]
        cursor.close()
        conn.close()
        return redirect(url_for('admin_dashboard'))

    return render_template('login.html')


@app.route('/admin_dashboard')
def admin_dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    return render_template('d2.html')


@app.route('/get_data')
def get_data():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT date, stock_value 
        FROM stockdata 
        WHERE date >= '2024-10-26'
    """)
    stock_data = cursor.fetchall()
    stock_dates = [str(row[0]) for row in stock_data]
    stock_values = [row[1] for row in stock_data]

    cursor.execute("SELECT date, avg_sentiment_score FROM avg_sentiment_table")
    sentiment_data = cursor.fetchall()
    sentiment_dates = [str(row[0]) for row in sentiment_data]
    sentiment_scores = [row[1] for row in sentiment_data]

    cursor.close()
    conn.close()

    return jsonify(
        stock_data={'dates': stock_dates, 'values': stock_values},
        sentiment_data={'dates': sentiment_dates, 'scores': sentiment_scores}
    )



if __name__ == '__main__':
    app.run(debug=True)
