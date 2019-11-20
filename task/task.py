import requests
import csv
import schedule
import time
import arrow
from datetime import datetime,timezone



class Schedulesms:

	apikey = "sm89229d1f340e464cb04810509d9f763f"
	url = "http://api.onehop.co/v1/sms/send/bulk"
	
	now = datetime.now(timezone.utc)
	attime = arrow.get(now)
	
	def __init__(self):
		#schedule time hour=8, minute=0
		self.scheduled_time = self.now.replace(hour=8, minute=0)
		print(self.now)
	
	# fetch data from CSV
	def get_data(self):
		result = {}
		try:
			with open('data.csv') as fcsv:
				read_csv = csv.reader(fcsv,delimiter=',')
				for row in read_csv:
					# stroing data in dict
					try:
						if row[1] in result:
							result[row[1]].append(row[0])
						else:
							result[row[1]] = [row[0]]
					except IndexError as index_error:
						continue
		except FileNotFoundError as fnf_error:
			print(fnf_error)
		return result
		
	# Send sms using onehop API
	def send_sms(self,phones):
		text = 'helloWorld'
		label = 'labelMarket';
		sender_id = 'market';
		for phone in phones:
			payload = "mobile_number="+phone+"&sms_text="+text+"&label="+label+"&sender_id="+sender_id
			print(payload)
			headers = {
			   'apikey': self.apikey,
			   'content-type': "application/x-www-form-urlencoded",
			   }
			response = requests.request("POST", self.url, data=payload, headers=headers)
			print(response.text)

	def run(self):
		data = self.get_data()
		for time_zone in data.keys():
			time_zone_time = self.attime.to(time_zone)
			if(time_zone_time.strftime("%H:%M") != self.scheduled_time.strftime("%H:%M")):
				print(True)
				self.send_sms(data[time_zone])

obj = Schedulesms()
obj.run()

#remove the multiple lines (''') to excude the scheduler
'''schedule.every().minutes.do(obj.run)

while i < 10:
	schedule.run_pending()
	time.sleep(1)'''