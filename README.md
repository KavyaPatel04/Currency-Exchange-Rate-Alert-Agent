
#  Currency Exchange Rate Alert




## overview

Monitor currency exchange rates and receive alerts when rates cross specified thresholds with this Currency Exchange Rate Alert application. This Python script integrates with the Twilio API to send SMS alerts and uses the "uagents" library to run an agent that periodically checks exchange rates.
## Features

- Currency Exchange Rate Monitoring: Input your base currency, target currency, upper threshold, and lower threshold to monitor exchange rates.
- SMS Alerts: Receive SMS alerts via Twilio when exchange rates cross specified thresholds.
- Background Agent: Utilizes the "uagents" library to run an agent that periodically checks exchange rates.
- Cross platform


## Installation

On your computer, you may need to install:

Python 3.8, 3.9 or 3.10.

PIP (Python Installs Packages).

Poetry for virtual environments (optional).

uAgents framework, 

Twilio framework for sending messages.

for more info visit:
(https://fetch.ai/docs/guides/agents/installing-uagent)
    
## API Usage

This Currency Exchange Rate Alert application exposes a simple API endpoint that allows you to submit currency exchange rate alerts programmatically. To interact with the API, follow these steps:

-> Request Format:  
To submit an alert, send a POST request to the API endpoint with the following parameters:
 
- 'base_currency': The base currency code (e.g., USD, EUR).
- 'target_currency': The target currency code (e.g., INR, GBP).
- 'upper_threshold': The upper threshold for the exchange rate.
- 'lower_threshold': The lower threshold for the exchange rate.


API site : https://www.exchangerate-api.com/

-> Response Format:

- Upon successful submission of an alert, the API will respond with a confirmation message. For example:

("Alert submitted successfully for USD to EUR rate. You will be notified when the rate crosses the specified thresholds.")


## Notification Sending with Twilio

This Currency Exchange Rate Alert application utilizes the Twilio API to send SMS notifications when exchange rates cross the specified thresholds. Follow these steps to configure and use Twilio for sending notifications:

Twilio Account Setup:

- If you don't already have one, sign up for a Twilio account at Twilio.
- Once registered, you'll need to obtain the following credentials:
- Twilio Account SID
- Twilio Auth Token
- Twilio Phone Number (a phone number you've purchased or received from Twilio)
- Recipient Phone Number (the phone number where you want to receive notifications)

Configuration in the Script:

Open the Python script and replace the following placeholders with your Twilio credentials:

TWILIO_ACCOUNT_SID = 'YOUR_TWILIO_ACCOUNT_SID'
TWILIO_AUTH_TOKEN = 'YOUR_TWILIO_AUTH_TOKEN'
TWILIO_PHONE_NUMBER = 'YOUR_TWILIO_PHONE_NUMBER'
TO_PHONE_NUMBER = 'RECIPIENT_PHONE_NUMBER'
## Source Code

The Source Code of this Program:
(https://github.com/KavyaPatel04/Currency-Exchange-Rate-Alert-Agent.git)