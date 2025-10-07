# 📊 Sentiment Analysis Web Application

## 🧠 Overview
This Flask web application provides sentiment analysis capabilities for text input. It exposes two endpoints:
- `/`: Renders the main index page
- `/sentimentAnalyzer`: Performs sentiment analysis on text provided as a query parameter

## 🚀 Features
- **Real-time Sentiment Analysis**: Analyzes text and returns sentiment label (positive, negative, neutral) with confidence scores
- **User-Friendly Interface**: Simple web interface for text input and result display
- **Error Handling**: Validates input and provides meaningful error messages for invalid inputs

## 🛠️ Installation
1. Clone the repository
2. Install dependencies using `pip install -r requirements.txt`
3. Run the application with `python server.py`

## 🌐 Endpoints
### GET `/sentimentAnalyzer`
**Description**: Performs sentiment analysis on provided text
**Query Parameter**: `textToAnalyze` - The text to analyze
**Response**: Formatted string with sentiment label and confidence score

### GET `/`
**Description**: Renders the main index page
**Response**: Rendered HTML template for the application interface

## 📝 Usage Examples
```
GET /sentimentAnalyzer?textToAnalyze=I love this product!
Response: The given text has been identified as positive with a score of 0.98.

GET /sentimentAnalyzer?textToAnalyze=This is terrible!
Response: The given text has been identified as negative with a score of 0.95.
```

## 📁 Project Structure
```
.
├── server.py              # Main Flask application
├── SentimentAnalysis/     # Sentiment analysis module
│   └── sentiment_analysis.py
├── templates/             # HTML templates
│   └── index.html
└── requirements.txt       # Dependencies
```

## ⚠️ Error Handling
The application handles the following error cases:
- No text provided: Returns "Invalid input! Try again."
- Blank text provided: Returns "Please enter text to analyze."
- Invalid input: Returns "Invalid input! Try again."

## 📈 Sentiment Analysis Details
The sentiment analysis is performed using a machine learning model that classifies text into:
- Positive sentiment
- Negative sentiment  
- Neutral sentiment

Confidence scores are provided for each classification.

