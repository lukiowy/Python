import smtplib
import datetime as dt
import random
my_email = ""
password = ""
now = dt.datetime.now()
today = now.weekday()

if today == 1:
    with open("C:/Python/Day 32/quotes.txt") as f:
        quotes = f.readlines()
    random_quote = random.choice(quotes)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs="", msg=f"Subject: Hello\n\n{random_quote}")