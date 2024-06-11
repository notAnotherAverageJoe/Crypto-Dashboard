import streamlit as st
import requests
import pandas as pd
import time

# Function to get cryptocurrency data from CoinGecko
def get_crypto_data(crypto_ids):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(crypto_ids)}&vs_currencies=usd&include_24hr_change=true"
    response = requests.get(url)
    return response.json()

#setting up my streamlit app
st.set_page_config(page_title="Crypto Dashboard", page_icon=":money_with_wings:", layout="wide")

st.title("💰 Real-time Cryptocurrency Price Dashboard")

crypto_options = ["bitcoin", "ethereum", "dogecoin", "litecoin", "ripple"]
selected_cryptos = st.multiselect("Select cryptocurrencies to view", crypto_options, default=["bitcoin", "ethereum"])

refresh_interval = st.slider("Refresh interval (seconds)", min_value=5, max_value=60, value=10, help="Select the refresh interval")

st.markdown("---")

placeholder = st.empty()

def format_price(price):
    return f"${price:.2f}"


while True:
    # Used a while loop to ensure the prices are refreshed.
    if selected_cryptos:
        crypto_data = get_crypto_data(selected_cryptos)
        
        # Format data
        formatted_data = []
        for crypto in selected_cryptos:
            if crypto in crypto_data:
                price = format_price(crypto_data[crypto]['usd'])
                change_24h = crypto_data[crypto]['usd_24h_change']
                formatted_data.append([
                    crypto.capitalize(), 
                    price, 
                    f"{change_24h:.2f}%", 
                    "🔺" if change_24h >= 0 else "🔻"
                ])
        
        # Create DataFrame
        df = pd.DataFrame(formatted_data, columns=["Cryptocurrency", "Price (USD)", "24h Change", "Trend"])
        
        with placeholder.container():
            st.write("### Current Prices")
            st.dataframe(df, height=300)
        
    time.sleep(refresh_interval)
