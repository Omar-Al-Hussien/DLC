import requests
import json

currency = input('Choose currency to convert ')
currency = currency.upper()
req = requests.get(url="https://free.currencyconverterapi.com/api/v5/convert?q="+currency+"_EGP&compact=y")
req.content.decode("utf-8")
data = req.json()
currency_value = data.get(currency+'_EGP')
if currency_value == None:
    print("Invalid Currency")
if currency_value!=None:
    #print (currency_value)
    value = currency_value.get('val')
    print(value)
