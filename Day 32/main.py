##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
import pandas
import datetime as dt
import random
import smtplib

now = dt.datetime.now()
month = now.month
day = now.day

my_email = ""
password = ""

df = pandas.read_csv("C:/Python/Day 32/birthdays.csv")
birthdays = df.to_dict(orient="records")

for i in range (len(birthdays)):
    if month == birthdays[i]["month"] and day == birthdays[i]["day"]:
        name = birthdays[i]["name"]
        email = birthdays[i]["email"]
        random_number = random.randint(1,3)

        with open(f"C:/Python/Day 32/letter_templates/letter_{random_number}.txt") as f:
            letter = f.read()
        final_letter = letter.replace("[NAME]", name)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(from_addr=my_email,to_addrs=email, msg=f"Subject: Happy Birthday!\n\n{final_letter}")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
