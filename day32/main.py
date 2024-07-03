import datetime as dt
import random
from smtplib import SMTP

import pandas as pd

MY_EMAIL = "philip.steingruber@gmail.com"

people = pd.read_csv("birthdays.csv")
connection = SMTP()

today = dt.datetime.today().date()

for index, row in people.iterrows():
    birthday = dt.datetime(
        year=int(row.year), month=int(row.month), day=int(row.day)
    ).date()
    print(birthday, today)
    if birthday == today:
        template = random.choice(
            [
                "letter_1.txt",
                "letter_2.txt",
                "letter_3.txt",
            ]
        )
        with open(f"./letter_templates/{template}") as file:
            letter = file.read().replace("[NAME]", row.first_name)
        with SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, "ftxl ogos sklr hppm")
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Happy birthday!\n\n{letter}",
            )
