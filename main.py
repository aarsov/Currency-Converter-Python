import requests

API_KEY = "c9aa3cd40d80206acefc63ed"

def get_exchange_rate(base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    if data["result"] == "success":
        exchange_rate = data["conversion_rates"][target_currency]
        return exchange_rate
    else:
        print("Error retrieving exchange rates.")
        return None

def convert_currency(amount, base_currency, target_currency):
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    if exchange_rate is not None:
        converted_amount = amount * exchange_rate
        return converted_amount
    else:
        return None

def main():
    print("Currency Converter App")

    base_currency = input("Enter base currency: ")
    target_currency = input("Enter target currency: ")
    amount = float(input("Enter amount to convert: "))

    converted_amount = convert_currency(amount, base_currency.upper(), target_currency.upper())

    if converted_amount is not None:
        print(f"{amount} {base_currency} is equal to {converted_amount} {target_currency}")
    else:
        print("Conversion failed.")

if __name__ == '__main__':
    main()
