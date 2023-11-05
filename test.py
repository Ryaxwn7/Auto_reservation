import datetime
import time

SERVICE_CATEGORY = "2c9c486e4f821a19014f82381feb0001"  # This is the category ID for "Sports Reservation". It usually doesn't change.

# Fill in these data
USER_ID = "21307130025"
USER_PASSWORD = "Mmmmjl123123"
CAMPUS_NAME = "邯郸校区"
SPORT_NAME = "网球"
SPORT_LOCATION = "南区网球场"
DATE = "2023-11-04"
TIME_1 = "20:00"
TIME_2 = "21:00"
TIME_3 = "19:00"
TIME_4 = "18:00"

# Optional data
EMAILS = ["jialunma88@163.com"]  # Receive error notifications by email
YOUR_EMAIL = "jialunma88@163.com"  # Account to send email from
EMAIL_PASSWORD = "mmmjl123123"  # Password for the email account


if __name__ == '__main__':
    now = datetime.datetime.now()
    formatted_time = now.strftime("%M%S")
    print("运行时间：", formatted_time)
    while(formatted_time!="5500"):
        now = datetime.datetime.now()
        formatted_time = now.strftime("%M%S")
        time.sleep(0.3)
    
