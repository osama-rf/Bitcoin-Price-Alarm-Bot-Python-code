import requests
import time

#global variables
api_key: str = 'Enter your Api key here'
bot_key = 'Enter your telegram bot key here'
chat_id = 'Enter your chat id here'
limit = 53000
time_interval = 5 * 60



def get_price():
    url = "Write coin market cap api link here"
    parameters = {
        'start':'1',
        'limit':'2'
    }
    headers = {
        'Accepts': 'application/json',
        'Write_API_KEY': api_key,
    }

    response = requests.get(url, headers=headers, params=parameters).json()
    btc_price = response['data'][0]['quote']['USD']['price']
    return btc_price
def send_update(chat_id, msg):
    url = f'https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={chat_id}&text={msg}'
    print()
    requests.get(url)

def main():
    while True:
         price = get_price()
         print(price)
         if price < limit:
            send_update(chat_id, f':shit{price}')
         time.sleep(time_interval)
main()