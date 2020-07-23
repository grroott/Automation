def myfunc():
    from selenium import webdriver
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.common.by import By
    import time
    import os
    from apiclient.discovery import build
    from google_auth_oauthlib.flow import InstalledAppFlow
    import pickle
    from datetime import datetime, timedelta


    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

    #driver = webdriver.Chrome(executable_path='F:\chromedriver_win32\chromedriver.exe')

    #Stackoverflow

    driver.get('https://stackoverflow.com/')

    driver.maximize_window()

    driver.find_element_by_xpath('/html/body/header/div/ol[2]/li[2]/a[1]').click()

    driver.find_element_by_xpath('//*[@id="email"]').click()
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(os.environ.get('USERNAME'))
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="password"]').click()
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(os.environ.get('PASSWORD'))
    time.sleep(2)

    driver.find_element_by_xpath('//*[@id="submit-button"]').click()
    time.sleep(2)

    driver.get('https://stackoverflow.com/users/11321166/gokul-nath')

    result = driver.find_element_by_xpath('//*[@id="top-cards"]/aside[2]/div/div/div[2]/div[2]/div/div[1]/span').text
    print(result)
    time.sleep(5)

    driver.close()

    # Google Calendar API


    #scopes = ["https://www.googleapis.com/auth/calendar"]
    #flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
    #credentials = flow.run_console()
    #pickle.dump(credentials, open("token.pkl", "wb"))

    credentials = pickle.load(open("token.pkl", "rb"))

    service = build("calendar", "v3", credentials=credentials)

    cal_result = service.calendarList().list().execute()  # returns all calendars

    calendar_id = cal_result['items'][0]['id']

    eve_result = service.events().list(calendarId=calendar_id).execute()  # returns all events

    start_time = datetime.now() + timedelta (minutes = 360)
    end_time = datetime.now() + timedelta (minutes = 375)

    event = {
      'summary': "Today: " + str(result),
      'location': 'home',
      'description': 'Automating stack overflow login with python',
      'start': {
        'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
        'timeZone': 'Asia/Kolkata',
      },
      'end': {
        'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
        'timeZone': 'Asia/Kolkata',
      },
      'reminders': {
        'useDefault': False,
        'overrides': [
          {'method': 'popup', 'minutes': 10},
        ],
      },
    }

    service.events().insert(calendarId=calendar_id, body=event).execute()

    print("Event created successfully!!")


from time import gmtime, strftime
desired_time = '02:30'
if strftime("%H:%M", gmtime()) == '02:30' or '02:31' or '02:32':
    myfunc()
else:
    print("Not an scheduled run")
