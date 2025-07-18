import requests
import json

def lambda_handler(event, context):
    # NYC coordinates
    latitude = '40.71427'
    longitude = '-74.00597'
    
    api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&temperature_unit=fahrenheit"
    
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()  # Raise error for non-200 status
        data = response.json()

        current_temp = data['current_weather']['temperature']
        print(f"Current temperature: {current_temp} °F")

        return {
            'statusCode': 200,
            'body': json.dumps(f"Current NYC temperature is {current_temp} degrees Fahrenheit")
        }

    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps("Failed to retrieve temperature data.")
        }

# Optional: Local test
if __name__ == "__main__":
    print(lambda_handler('', ''))
