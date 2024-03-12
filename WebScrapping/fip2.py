import requests
import pandas
from bs4 import BeautifulSoup

#Getting access from the web by sending a Request to the Website
response = requests.get("https://www.ebay.com/globaldeals?_trkparms=pageci%3Af27a734b-7e3d-11ee-b5dd-0a6b2e0db9ac%7Cparentrq%3Aaf33fd6218b0a8cea2b2407fffffadc0%7Ciid%3A1")

#Using BeautifulSoup and Parse of HTML code getting the code 
soup = BeautifulSoup(response.content, 'html.parser') # Parse

#using below code From the HTML content selecting a group of names which are presented in a specific Tag which class cotainted all the names
names = soup.find_all('span', class_='ebayui-ellipsis-2')
name = []
for i in names[0:]:
    d = i.get_text()
    name.append(d)
#print(name)
    
#using below code Same as like above here we are getting the prices and so on....
prices = soup.find_all('span', class_='first')
price = []
for i in prices[0:]:
    d = i.get_text()
    price.append(d)
#print(price)
    
#using below code Pandas DataFrame we are storing all of them into a csv file. 
df = pandas.DataFrame()
data = {'Names':pandas.Series(names),
        'Prices':pandas.Series(price),
        'Actual_Price':pandas.Series(Ac_price),
        'Discounts': pandas.Series(Discount)
        }
df = pandas.DataFrame(data)
#print(df)
df.to_csv("eBay-Daily_Deals_data.csv")


Actual_Price = soup.find_all('span', class_='itemtile-price-strikethrough')
Ac_price = []
for i in Actual_Price[0:]:
    d = i.get_text()
    Ac_price.append(d)
#print(Ac_price)

Discounts = soup.find_all('span', class_='itemtile-price-bold')
Discount = []
for i in Discounts[0:]:
    d = i.get_text()
    Discount.append(d)
#print(Discount)


#using below code Pandas DataFrame we are storing all of them into a csv file. 
df = pandas.DataFrame()
#print(df)

data = {'Names':pandas.Series(names),
        'Prices':pandas.Series(price),
        'Actual_Price':pandas.Series(Ac_price),
        'Discounts': pandas.Series(Discount)
        }
#print(data)
df = pandas.DataFrame(data)
#print(df)

df.to_csv("eBay-Daily_Deals_data.csv")


