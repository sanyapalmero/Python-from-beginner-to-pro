import requests
import json

def main():
    url = "https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC&tsyms=USD,EUR,RUR"
    r = requests.get(url)
    str_json = r.text
    print(str_json)
    parsed_json = json.loads(str_json)
    print(parsed_json)
    rur = parsed_json["BTC"]["RUR"]
    eur = parsed_json["BTC"]["EUR"]
    usd = parsed_json["BTC"]["USD"]
    message = f"1 биткоин равен {rur} рублям, {eur} евро, {usd} долларов"
    print(message)

if __name__ == '__main__':
    main()
