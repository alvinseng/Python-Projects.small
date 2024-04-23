# import smtplib
#
# my_email = "kuromew84@gmail.com"
# password = "hvhnqkmtulbpptme"
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="kuromew@myyahoo.com",
#         msg="Subject:Hello\n\nThis is the body of my email"
#     )

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_the_week = now.weekday()
# print(day_of_the_week)

date_of_birth = dt.datetime(year=1994, month= 6, day=15)
print(date_of_birth)

