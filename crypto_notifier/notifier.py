import requests
import json

BOT_TOKEN = "-- YOUR TOKEN --"
CHAT_ID = "111111111"


def get_coin_data(name):
    coin_r = requests.get(
        f"https://panel.arzplus.net/_next/data/Tw1MTHtcEv_v9_otGjO5T/price/{name}.json"
    )

    coin_data = json.loads(coin_r.content)
    coin_price = coin_data["pageProps"]["fallbackData"][0]["price_irt"]
    coin_1h_change = coin_data["pageProps"]["fallbackData"][0]["change_1h"]
    name_fa = coin_data["pageProps"]["fallbackData"][0]["name_fa"]

    return {"price": coin_price, "1h_change": coin_1h_change, "name_fa": name_fa}


def send_telegram_message(chat_id, text):
    requests.get(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={text}"
    )


def generate_message_for_coin(data):
    rounded_change = round(data["1h_change"], 2)
    message = f"💰  {data["name_fa"]}: {data["price"]} ({rounded_change}%)"
    return message


coins = [
    "bitcoin",
    "tether",
    "ethereum",
]
for coin in coins:
    coin_data = get_coin_data(coin)
    message = generate_message_for_coin(coin_data)
    send_telegram_message(CHAT_ID, message)
    send_telegram_message(CHAT_ID, message)
