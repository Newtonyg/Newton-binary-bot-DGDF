import requests
import json

# Replace 'YOUR_API_TOKEN' with your actual Deriv API token
API_TOKEN = 'YOUR_API_TOKEN'

# Deriv API base URL
API_BASE_URL = 'https://api.deriv.com'

def place_digit_differ_trade(symbol, contract_type, duration, amount, prediction):
    # Construct the API endpoint URL
    endpoint = f'{API_BASE_URL}/binary/options'

    # Define the trade parameters
    trade_params = {
        'symbol': symbol,                     # Symbol of the asset to trade (e.g., 'R_10')
        'contract_type': contract_type,       # Type of the contract (always 'DIGITDIFF')
        'duration': duration,                 # Duration of the trade in seconds
        'amount': amount,                     # Amount to trade
        'basis': 'stake',                     # Basis for the trade (always 'stake' for binary options)
        'prediction': prediction              # Prediction for the trade (0-9 for 'Digit Differ')
    }

    headers = {
        'Authorization': f'Bearer {API_TOKEN}',
        'Content-Type': 'application/json'
    }

    # Send the request to place the trade
    response = requests.post(endpoint, data=json.dumps(trade_params), headers=headers)

    # Check the response status
    if response.status_code == 200:
        trade_result = response.json()
        print("Trade placed successfully.")
        print("Transaction ID:", trade_result['transaction_id'])
    else:
        print("Failed to place the trade.")
        print("Response:", response.text)

# Example usage
symbol = 'R_10'             # Replace with the symbol of the asset you want to trade
contract_type = 'DIGITDIFF'     # Specify the contract type as 'DIGITDIFF'
duration = 60              # Replace with the duration of the trade in seconds
amount = 10                # Replace with the amount to trade
prediction = 5             # Replace with your prediction (0-9 for 'Digit Differ')

# Place the digit differ trade
place_digit_differ_trade(symbol, contract_type, duration, amount, prediction)

