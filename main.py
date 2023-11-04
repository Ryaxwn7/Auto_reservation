import apis
import logs
import datetime
import time

SERVICE_CATEGORY = "2c9c486e4f821a19014f82381feb0001"  # This is the category ID for "Sports Reservation". It usually doesn't change.

# Fill in these data
USER_ID = "21307130025"
USER_PASSWORD = "Mmmmjl123123"
CAMPUS_NAME = "邯郸校区"
SPORT_NAME = "网球"
SPORT_LOCATION = "南区网球场"
DATE = "2023-11-07"
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
    formatted_time = now.strftime("%H%M%S")
    print("运行时间：", formatted_time)
    while(formatted_time!="000000"):
        now = datetime.datetime.now()
        formatted_time = now.strftime("%H%M%S")
        time.sleep(0.3)
    try:
        logged_in_session = apis.login(USER_ID, USER_PASSWORD)
        campus_id, sport_id = apis.load_sports_and_campus_id(logged_in_session, SERVICE_CATEGORY, CAMPUS_NAME, SPORT_NAME)
        service_id = apis.get_service_id(logged_in_session, SERVICE_CATEGORY, campus_id, sport_id, SPORT_LOCATION)
        
        apis.reserve(logged_in_session, service_id, SERVICE_CATEGORY, DATE, TIME_1)
        apis.reserve(logged_in_session, service_id, SERVICE_CATEGORY, DATE, TIME_2)
        apis.reserve(logged_in_session, service_id, SERVICE_CATEGORY, DATE, TIME_3)
        apis.reserve(logged_in_session, service_id, SERVICE_CATEGORY, DATE, TIME_4)
    except Exception as e:
        if EMAILS:
            import smtplib
            import datetime
            message = f"Subject: Failed to reserve sport field\n\n{logs.FULL_LOG}"
            connection = smtplib.SMTP("smtp-mail.outlook.com", 587)
            try:
                connection.ehlo()
                connection.starttls()
                connection.login(YOUR_EMAIL, EMAIL_PASSWORD)
                connection.sendmail(YOUR_EMAIL, EMAILS, message)
            finally:
                connection.quit()
