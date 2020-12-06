# NSE program to see given details. it is using Web scrapping
import requests
from bs4 import BeautifulSoup

def func(stocknames):
    stock_symbol = stocknames

    stock_url = 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=' + str(stock_symbol)

    headers = { 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
    response = requests.get(stock_url,headers=headers)  # this will help us to get only div id part and not the extra one


    soup = BeautifulSoup(response.text, 'html.parser')
    data_array = soup.find(id='responseDiv').getText().strip().split(":")
    type(data_array) # collection of all the required data

    Data_required = ['previousClose', 'open', 'High', 'Low', 'Close', 'totalTradedValue', 'quantityTraded',
                     'deliveryQuantity', 'deliveryToTradedQuantity']

    d = dict() # a dictionary so that we can return required data
    for item in data_array:
        for i in range(0,9): # to fetch the values for required data
            if Data_required[i] in item:
                index = data_array.index(item) + 1
                value = data_array[index].split('"')[1]
                d[Data_required[i]] = str(value) #storing in dictionary
            else:
                continue

    return (d) #return dictionary

Input_stock_list = ['RELIANCE', 'HDFCBANK', 'ADANIPORTS', 'ITC', 'SBIN', 'IOC', 'RBLBANK']

for i in range(1,7):
    print(str(i)+'.'+ Input_stock_list[i] + ":\n")
    #for keys in Data_required:
    d=func(Input_stock_list[i]) # d is a returned dictionary wihth key = data required and value contain value for different input stock list

    for key, value in d.items():
        print(key, ' = ', value)
    print('\n')


