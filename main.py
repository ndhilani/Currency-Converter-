import forex_python

from forex_python.converter import CurrencyRates #will import
from forex_python.converter import CurrencyCodes
c = CurrencyRates()
d = CurrencyCodes()


AvailableCurrencies = ['EUR', 'JPY', 'BGN', 'CZK', 'DKK', 'GBP', 'HUF', 'PLN', 'RON', 'SEK', 'CHF', 'ISK', 'NOK', 'TRY', 'AUD', 'BRL', 'CAD', 'CNY', 'HKD', 'IDR', 'INR', 'KRW', 'MXN', 'MYR', 'NZD', 'PHP', 'SGD', 'THB', 'USD', 'ZAR']

while True:
    AvailableCounter = 0
    while AvailableCounter == 0:
        FirstCurrency = input("What is your original currency: ")
        for i in AvailableCurrencies:
            if i == str(FirstCurrency):
                AvailableCounter = 1
            else:
                pass
        if AvailableCounter == 0:
            print("That's not an available currency, please leave in the form of 3 capital letters.")
    while AvailableCounter == 1:
        Amount = float(input("How much do you want to convert: "))
        AvailableCounter = 2
    while AvailableCounter == 2:
        SecondCurrency = input("What is the new currency: ")
        for i in AvailableCurrencies:
            if i == str(SecondCurrency):
                AvailableCounter = 3
            else:
                pass
        if AvailableCounter == 2:
            print("That's not an available currency, please leave in the form of 3 capital letters.")
    FirstCurrnecySymbol = str(d.get_symbol(FirstCurrency))
    SecondCurrnecySymbol = str(d.get_symbol(SecondCurrency))
    multiplier = float(c.get_rate(str(FirstCurrency), str(SecondCurrency)))
    NewAmount = float(Amount*multiplier)
    NewAmount = str(round(NewAmount, 2))
    print(str(FirstCurrnecySymbol) + str(Amount) + " in " + str(FirstCurrency) + ", is " + str(SecondCurrnecySymbol) + str(NewAmount) + " in " + str(SecondCurrency))
    print("")
    stayIn = input("Carry on? Yes(Y) or No(N)")
    if stayIn == "y" or stayIn == "Y" or stayIn == "yes" or stayIn == "YES":
        pass
    else:
        print("OK, exiting program")
        break
   
