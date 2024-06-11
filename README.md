## 💰 Real-time Cryptocurrency Price Dashboard
Welcome to the Real-time Cryptocurrency Price Dashboard! This Streamlit app allows users to track the latest prices and 24-hour changes of various cryptocurrencies. The app provides an intuitive and visually appealing interface for monitoring real-time cryptocurrency data.

## Features
Real-time Data: Fetches the latest cryptocurrency prices and 24-hour percentage changes from the CoinGecko API.
Customizable View: Users can select which cryptocurrencies to monitor.
Dynamic Refresh: Set the refresh interval to update prices at your preferred frequency.
Visual Indicators: Displays upward (🔺) or downward (🔻) trends based on 24-hour price changes.
Demo

## Installation
To run the app locally, follow these steps:

Clone the repository:

```bash
Copy code
git clone https://github.com/yourusername/crypto-dashboard.git
cd crypto-dashboard
Create a virtual environment:
```
```bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install dependencies:
```
```bash
Copy code
pip install -r requirements.txt
Run the Streamlit app:
```
```bash
Copy code
streamlit run app.py
Usage
Open the app in your browser.
Select the cryptocurrencies you want to monitor from the multiselect dropdown.
Adjust the refresh interval slider to set how often the data should be updated.
The dashboard will display the current prices, 24-hour changes, and trend indicators for the selected cryptocurrencies.
```
## Code Overview
The main parts of the code include:

Fetching Data: The get_crypto_data function retrieves data from the CoinGecko API.
Formatting Data: The prices and changes are formatted for display.
Streamlit Layout: The app uses Streamlit components like multiselect, slider, table, and dataframe to create the user interface.

## Special thanks: 
ATGTG