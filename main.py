from pandas import*
import datetime as dt
from random import*
import smtplib
import os

email=os.environ.get("MY_EMAIL")
password=os.environ.get("MY_PASSWORD")


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





