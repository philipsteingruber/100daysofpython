##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

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
