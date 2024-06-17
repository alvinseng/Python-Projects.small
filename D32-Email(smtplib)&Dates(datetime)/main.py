import smtplib
import datetime as dt
import random

MY_EMAIL = "kuromew84@gmail.com"
PASSWORD = "hvhnqkmtulbpptme"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            # to_addrs="kuromew@myyahoo.com",
            to_addrs=MY_EMAIL,
            msg=f"Subject:Weekly Motivation\n\n{quote}"
        )


