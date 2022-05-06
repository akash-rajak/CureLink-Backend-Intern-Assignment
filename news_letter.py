
# imported various library to be used
import schedule
import time
import smtplib
import sqlite3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# this is the email and password , from which email is being send
email = ""
password = ""

# creating list of subscriber to store subscriber and send the newsletter to them
subscribers = []
# creating dictionary messages, to store the message corresponding to the particular message heading or task
messages = {}


# function defined to fetch the data from both the table
def fetch_data_from_table():
	try:
		sqliteConnection = sqlite3.connect('newsletter.db')
		cursor = sqliteConnection.cursor()

		sqlite_select_query_1 = """SELECT * from Subscriber"""
		cursor.execute(sqlite_select_query_1)

		# fetched data is stored in subscribers list
		records = cursor.fetchall()
		for row in records: 
			subscribers.append(row[2])

		sqlite_select_query_2 = """SELECT * from Newsletter"""
		cursor.execute(sqlite_select_query_2)

		# fetched data is stored into messages dictionary
		result = cursor.fetchall()
		for row in result:
			messages[row[1]] = row[2]
			
		cursor.close()
		
	except sqlite3.Error as error:
		print("Failed to read data from sqlite table", error)
	
	finally:
		if sqliteConnection:
			sqliteConnection.close()
			print("The SQLite connection is closed")

# called the function for fetching the data
fetch_data_from_table()

# sends mail by changing the message content according to type of email
def send_mail(title):
	smtp = smtplib.SMTP('smtp.gmail.com', 587)
	smtp.ehlo()
	smtp.starttls()
	smtp.login(email, password)

	subject = "Your Weekly Newsletter Message"
	content = messages[title]
	msg = MIMEMultipart()
	msg['Subject'] = subject
	msg.attach(MIMEText(content))

	smtp.sendmail(from_addr=email, to_addrs=subscribers, msg=msg.as_string())
	print("Weekly Newsletter Sent to the Subscriber Successfully.")
	smtp.quit()


# function defined to send the message regarding yoga
def weekly_yoga():
	send_mail("yoga")

# function defined to send the message regarding workout
def weekly_workout():
	send_mail("workout")

# function defined to send the message regarding walk
def weekly_walk():
	send_mail("walk")

# function defined to send the message regarding diet
def weekly_diet():
	send_mail("diet")

# function defined to send the message regarding rest
def weekly_rest():
	send_mail("rest")

# function defined to send the message regarding water
def weekly_water():
	send_mail("water")

# function defined to send the message regarding sleep
def weekly_sleep():
	send_mail("sleep")


# message schedule for each day of the week for different timing
schedule.every().monday.at("06:00").do(weekly_yoga)
schedule.every().tuesday.at("07:00").do(weekly_workout)
schedule.every().wednesday.at("08:00").do(weekly_walk)
schedule.every().thursday.at("09:00").do(weekly_diet)
schedule.every().friday.at("10:00").do(weekly_rest)
schedule.every().saturday.at("11:00").do(weekly_water)
schedule.every().sunday.at("12:00").do(weekly_sleep)

while True:
	schedule.run_pending()
	time.sleep(1)