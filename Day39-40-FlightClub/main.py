from dotenv import load_dotenv
import requests , os


load_dotenv()

API_KEY = os.getenv('API_KEY')

endpoint = f'https://api.flightapi.io/onewaytrip/{API_KEY}/CJB/MAA/2024-05-20/1/0/0/Economy/INR'

response = requests.get(url=endpoint)
response.raise_for_status()

result = response.json()
for prices in result['itineraries'][:6]:

    cheapest = prices['cheapest_price']['amount']
    score = prices['score']
    
    for p in prices['pricing_options']:
        agents = p['agent_ids']
        amt = p['price']['amount']

        if amt < 7000:
            print(f'{agents} | {amt}')


    


