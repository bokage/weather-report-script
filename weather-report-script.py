import requests, json, smtplib

'''Phone Carriers Email Addresses: 
ATT - number@txt.att.net
TMobile - number@tmomail.net
Sprint - number@messaging.sprintpcs.com'''

coordinates = #[lat, long]
city = #city name

#sets link for weather api
darksky_api = "https://api.darksky.net/forecast/4454cd0f9b09f3329eea2f6b77a8752e/%f,%f" % (coordinates[0], coordinates[1])

response = requests.get(darksky_api)
#set data to a json-viewing object
data = response.json()
#converts into a dictionary
data_keys = data.keys()
#message
summary = "\n\nThe temperature is %s with a high of %s and a low of %s" %(data['currently']['temperature'], data['daily']['data'][0]['temperatureHigh'], data['daily']['data'][0]['temperatureLow'])

#text sending
bot_email = #'email'
bot_pass = #'password'

sent_from = bot_email
to = #list of phone numbers in an array []

body = """From: %s\nTo: %s\nSubject: %s\n\n%s""" %(sent_from, to, "Weather Update", summary)

#tries to log into email and send an email to a phone number, i.e. 1234567890@txt.att.net. This will be received by the number as a text.
try: 
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.ehlo()
	server.login(bot_email, bot_pass)
	server.sendmail(sent_from, to, body)
	server.close()
	print('Sent!')
except:
	print("Something went wrong...")