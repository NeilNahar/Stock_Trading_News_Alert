import requests
import smtplib

API_KEY_STOCK="VWTJG6HNK9ETHY2C"
API_KEY_NEWS="b8794789270a448da90235acd965e527"
my_email="aj0040976@gmail.com"
password="uvqyhozbxiumjibq"
recieving_email="aj311840@gmail.com"

parameter1={"function":"TIME_SERIES_INTRADAY","symbol":"TSLA","interval":"60min","apikey":API_KEY_STOCK}
parameter2={"q":"tsla","apikey":API_KEY_NEWS}

response1 = requests.get(f"https://www.alphavantage.co/query",params=parameter1)

response1.raise_for_status()
data = response1.json()["Time Series (60min)"]

value1=float(data[list(data)[0]]["4. close"])
value2=float(data[list(data)[16]]["4. close"])

variation=round(((value1-value2)/value2)*100,1)
sign=None
if variation>=10:
    sign="⬆️"
else:
    sign="⬇️"
if variation>=10 or variation<=-10:
    print("Major Change")
    response2 = requests.get(f"https://newsapi.org/v2/everything",params=parameter2)
    response2.raise_for_status()
    Articles=response2.json()["articles"][:3]

    connection=smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email,password=password)

    for i in range(3):
        connection.sendmail(from_addr=my_email,to_addrs=recieving_email,msg=f"subject: TESLA {sign}{variation}%\n {Articles[i]['title']}\n\n{Articles[i]['description']}")
        connection.close()

else:
    print("Not major change")
