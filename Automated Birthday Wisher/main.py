##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import random
import pandas


MY_EMAIL = "kuromew84@gmail.com"
PASSWORD = "hvhnqkmtulbpptme"

# 1. Update the birthdays.csv

now = dt.datetime.now()
today = (now.month, now.day)  #date tuple
birthday = pandas.read_csv("birthdays.csv")
# print(birthday)
birthday_dict = {(birthday_row['month'],birthday_row['day']): birthday_row for (index, birthday_row) in birthday.iterrows()}
# print(birthday_dict)

# 2. Check if today matches a birthday in the birthdays.csv
if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!!\n\n{contents}"
        )





