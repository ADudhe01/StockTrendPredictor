# Stock Trend Prediction

This project predicts stock price trends using a machine learning model built with Keras and TensorFlow. It uses historical stock data to train the model and makes predictions on future prices. The app is built with Streamlit for an interactive user interface where users can input stock tickers and visualize price trends, moving averages, and predictions.

## Installation

To run this project locally, follow the steps below:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/StockTrendPredictor.git
   cd StockTrendPredictor
   ```
2. Create a virtual environment (optional but recommended):
  ```bash
  python3 -m venv myenv
  source myenv/bin/activate 
  ```
  On Windows,
  ```bash
  use myenv\Scripts\activate
  ```

3. Install the required libraries:
  ```bash
  pip install -r requirements.txt
  ```
4. Make sure you have the keras_model.h5 model file in your project directory. This is the pre-trained model that the application uses to predict stock trends.

## Usage:
To run the application, use the following command:
  ```bash
  streamlit run app.py
```
Enter a stock ticker (e.g., AAPL for Apple Inc.) when prompted. The app will download historical stock data and show the following visualizations:
 - Stock Data: Descriptive statistics of the stock from 2000 to the present.
 - Price vs Time: A plot of the closing price over time.
 - Moving Averages: A chart showing the closing price along with 100-day and 200-day moving averages.
 - Predictions vs Original: A comparison of the model's predictions against the actual stock prices.
