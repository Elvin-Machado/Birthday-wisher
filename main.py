##################### Extra Hard Starting Project ######################
from pandas import*
import datetime as dt
from random import*
import smtplib
import os
email=os.environ.get("MY_EMAIL")
password=os.environ.get("MY_PASSWORD")
# 1. Update the birthdays.csv

today=dt.datetime.now()
today_date=(today.month,today.day)


data=read_csv("birthdays.csv",dtype=object)
data_dict={(data_row["month"],data_row["day"]):data_row for (index,data_row) in data.iterrows()}
if today_date in data_dict:
    birthday_person=data_dict[today_date]
    with open(f"letter_templates/letter_{randint(1,3)}.txt")as letter:
        content=letter.read()
        content=content.replace("[NAME]",birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
           connection.starttls()
           connection.login(user=email,password=password)
           connection.sendmail(from_addr=email,to_addrs=f"{birthday_person["email"]}",msg=f"Subject:Wishing Birthaday\n\n {content}")
# 2. Check if today matches a birthday in the birthdays.csv


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




