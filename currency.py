from uagents import Agent
import requests
from twilio.rest import Client
from uagents import Context
from uagents.setup import fund_agent_if_low


cashycutie = Agent(name="cashycutie", 
        port=8000,
        endpoint=["http://127.0.0.1:8000/submit"],
        seed="cashycutie recovery phrase",
)

# Twilio credentials
TWILIO_ACCOUNT_SID = "ACec4afe80a90e9005cad99598ee21a139"
TWILIO_AUTH_TOKEN = "310feada69450f637cb147b27d950083"
TWILIO_PHONE_NUMBER = "+12563882434"
TO_PHONE_NUMBER = "+917265090669"  # Replace with the recipient's phone number

# Function to send SMS alerts
def send_sms_alert(message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(
        to=TO_PHONE_NUMBER,
        from_=TWILIO_PHONE_NUMBER,
        body=message
    )

# Function to fetch the exchange rate
def get_exchange_rate(base_currency, target_currency):
    response = requests.get(f'https://v6.exchangerate-api.com/v6/86639d518e130c5da8c502d2/latest/{base_currency}')
    data = response.json()
    conversion_rates = data.get('conversion_rates', {})
    exchange_rate = conversion_rates.get(target_currency)
    return exchange_rate

# Function to check thresholds and send alerts
def check_thresholds():
    base_currency = input('Enter the base currency: ').upper()
    target_currency = input('Enter the target currency (e.g., INR): ').upper()
    upper_threshold = float(input('Enter the upper threshold: '))
    lower_threshold = float(input('Enter the lower threshold: '))
    exchange_rate = get_exchange_rate(base_currency, target_currency)

    if exchange_rate is not None:
        print(f'current rate of 1 {base_currency} is {exchange_rate} {target_currency}\n You will be notified when currency rate crosses the threshold')

        if exchange_rate > upper_threshold:
            return (f'Alert: {base_currency} to {target_currency} rate is above {upper_threshold}')
            
        elif exchange_rate < lower_threshold:
            return (f'Alert: {base_currency} to {target_currency} rate is below {lower_threshold}')
            
@cashycutie.on_interval(period=28800.0)
async def time_interval(ctx:Context):
    currency = check_thresholds()
    ctx.logger.info(currency)
    if "below" in currency or "above" in currency :
        await send_sms_alert(currency)                                                                                          

if __name__ == '__main__':
    cashycutie.run()