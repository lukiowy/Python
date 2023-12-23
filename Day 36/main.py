import requests
from datetime import datetime, timedelta
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = ""
NEWS_API_KEY = ""
STOCK_URL = "https://www.alphavantage.co/query?"
NEWS_URL = "https://newsapi.org/v2/everything?"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": STOCK_API_KEY
}

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 
time_now = datetime.now()
yesterday = datetime.now() - timedelta(1)
before_yesterday = yesterday - timedelta(1)
before_yesterday = before_yesterday.date()
yesterday = yesterday.date()
yesterday = f"{yesterday}"
before_yesterday=f"{before_yesterday}"

response = requests.get(url=STOCK_URL, params=stock_parameters)
response.raise_for_status()
data = response.json()
print(data)
yesterday_data = float(data["Time Series (Daily)"][yesterday]["4. close"])
before_yesterday_data = float(data["Time Series (Daily)"][before_yesterday]["4. close"])
print(yesterday_data)
print(before_yesterday_data)
difference = abs(yesterday_data - before_yesterday_data)
print(difference)
five_percent = yesterday_data * 0.05
print(five_percent)

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator
if difference > five_percent:
    news_parameters = {
        "q": COMPANY_NAME,
        "from": yesterday,
        "to": yesterday,
        "language": "en",
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(url=NEWS_URL, params=news_parameters)
    response.raise_for_status()
    data = response.json()
    news = []
    titles = []
    for i in range(0,3):
        title = data["articles"][i]["title"]
        new = data["articles"][i]["description"]
        titles.append(title)
        news.append(new)
    difference = 1.2

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    # Send a separate message with each article's title and description to your phone number. 
    #HINT 1: Consider using a List Comprehension.
    print(f"{STOCK}: 🔺{difference}%\nHeadline: {titles[0]}\nBrief: {news[0]}")


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

