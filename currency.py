from forex_python.converter import CurrencyRates

c = CurrencyRates()
amount = int(input("Digite o valor que você quer converter\n"))
from_currency = input("From\n").upper()
to_corrency = input("to\n").upper()
print(from_currency, "To", to_corrency, amount)
result = c.convert(from_currency, to_corrency, amount)
print(result)