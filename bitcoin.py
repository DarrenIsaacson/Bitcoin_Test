import requests




def main():

    amount = get_amount()
    total = convert(amount)
    display(total)


def get_amount():
    while True:
        try:
             return float(input("How many bitcoins do you have:"))

        except:
            print("\nYou can only enter in a value.\n")


def convert(dollars):
    url = get_url()

    data = get_json(url)

    rate = get_rate(data)

    return dollars * rate


def get_url():
    return 'https://api.coindesk.com/v1/bpi/currentprice.json'

def get_json(url):
    return requests.get(url).json()

def get_rate(data):
    return data['bpi']['USD']['rate_float']

def display(total):

    print(f'The rate of bitcoin is currently ${total}')

if __name__ == '__main__':
    main()
