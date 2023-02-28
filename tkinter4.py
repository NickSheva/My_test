import requests


class Currency_convertor:
    # empty dict to store the conversion rates
    rates = {}

    def __init__(self, url):
        data = requests.get(url).json()
        self.rates = data["rates"]

        # function to do a simple cross multiplication between

    # the amount and the conversion rates
    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'EUR':
            amount = amount / self.rates[from_currency]
        output = amount * self.rates[to_currency]

        # limiting the precision to 2 decimal places
        output = round(amount * self.rates[to_currency], 2)
        print('{} {} = {} {}'.format(initial_amount, from_currency, output, to_currency))


if __name__ == "__main__":
    url = 'http://data.fixer.io/api/latest?access_key=95e8617f265030569da10ad979de7ed4'
    c = Currency_convertor(url)
    from_country = input("From Country: ")
    to_country = input("TO Country: ")
    amount = int(input("Amount: "))

    c.convert(from_country, to_country, amount)











