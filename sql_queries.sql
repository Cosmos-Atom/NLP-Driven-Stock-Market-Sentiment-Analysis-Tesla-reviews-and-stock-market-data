create database tesla_app;
use tesla_app;

CREATE TABLE UserCredentials (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

INSERT INTO UserCredentials (email, password) 
VALUES 
('kavya@gmail.com', 'password1'),
('sharanya@gmail.com', 'password2'),
('ishvarya@gmail.com', 'password3'),
('lasya@gmail.com', 'password4');


Select * from UserCredentials;


CREATE TABLE newstable (
    id INT AUTO_INCREMENT PRIMARY KEY,
    `date` DATE NOT NULL,  
    title TEXT NOT NULL,
    content TEXT NOT NULL
);

Drop table newstable;

CREATE TABLE stockdata (
    id INT AUTO_INCREMENT PRIMARY KEY,
    `date` DATE NOT NULL,    -- Using backticks to escape the reserved keyword 'date'
    stock_value DECIMAL(10, 2) NOT NULL  -- stock_value with 10 digits, 2 of which are after the decimal point
);

INSERT INTO stockdata (`date`, stock_value)
VALUES
('2024-11-25', 338.59),
('2024-11-22', 352.56),
('2024-11-21', 339.64),
('2024-11-20', 342.03),
('2024-11-19', 346.00),
('2024-11-18', 338.74),
('2024-11-15', 320.72),
('2024-11-14', 311.18),
('2024-11-13', 330.24),
('2024-11-12', 328.49),
('2024-11-11', 350.00),
('2024-11-08', 321.22),
('2024-11-07', 296.91),
('2024-11-06', 288.53),
('2024-11-05', 251.44),
('2024-11-04', 242.84),
('2024-11-01', 248.98),
('2024-10-31', 249.85),
('2024-10-30', 257.55),
('2024-10-29', 259.52),
('2024-10-28', 262.51),
('2024-10-25', 269.19),
('2024-10-24', 260.48),
('2024-10-23', 213.65),
('2024-10-22', 217.97),
('2024-10-21', 218.85);



CREATE TABLE newstable (
    id INT AUTO_INCREMENT PRIMARY KEY,
    `date` DATE NOT NULL,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    sentiment_score float,
   sentiment varchar(20)
);

select * from newstable;

CREATE TABLE reviewtable (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    review TEXT NOT NULL,
    sentiment_score FLOAT,
    sentiment VARCHAR(20)
);

select * from reviewtable;

CREATE TABLE combined_table (
    date DATE,
    sentiment_score FLOAT
);

CREATE TABLE review_auto_date (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each record
    date DATE DEFAULT (CURRENT_DATE),   -- Automatically sets the current date
    review TEXT NOT NULL,               -- Column for review text
    sentiment_score FLOAT               -- Column for sentiment score
);

Select * from review_auto_date;


CREATE TABLE avg_sentiment_table (
    date DATE NOT NULL,
    avg_sentiment_score FLOAT,
    PRIMARY KEY (date)
);

SElect * from avg_sentiment_table;


DELIMITER $$

CREATE TRIGGER update_avg_sentiment
AFTER INSERT ON review_auto_date
FOR EACH ROW
BEGIN
    -- Declare variables to store the sum of sentiment scores and the count of reviews
    DECLARE total_score FLOAT DEFAULT 0;
    DECLARE review_count INT DEFAULT 0;
    DECLARE avg_sentiment FLOAT DEFAULT 0;
    DECLARE existing_avg_sentiment FLOAT;
    
    -- Get the sentiment scores for all reviews on the same day
    SELECT SUM(sentiment_score), COUNT(*) INTO total_score, review_count
    FROM (
        SELECT sentiment_score FROM review_auto_date WHERE date = NEW.date
        UNION ALL
        SELECT sentiment_score FROM newstable WHERE date = NEW.date
        UNION ALL
        SELECT sentiment_score FROM reviewtable WHERE date = NEW.date
    ) AS all_reviews;
    
    -- Calculate the average sentiment score
    IF review_count > 0 THEN
        SET avg_sentiment = total_score / review_count;
    END IF;
    
    -- Check if the average sentiment score already exists for this date
    SELECT avg_sentiment_score INTO existing_avg_sentiment 
    FROM avg_sentiment_table 
    WHERE date = NEW.date;
    
    -- If the entry exists, update the average sentiment score, otherwise, insert a new row
    IF existing_avg_sentiment IS NOT NULL THEN
        UPDATE avg_sentiment_table
        SET avg_sentiment_score = avg_sentiment
        WHERE date = NEW.date;
    ELSE
        INSERT INTO avg_sentiment_table (date, avg_sentiment_score)
        VALUES (NEW.date, avg_sentiment);
    END IF;
END $$

DELIMITER ;

show triggers;
