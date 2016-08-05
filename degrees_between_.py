def degrees(hours, minutes):
	if hours > 24 or minutes > 60 or hours < 0 or minutes < 0: # check if hours or minutes out of range
		print("Error")
		exit(0)
	elif hours > 12 and hours < 24: # convert to 12-hour format
		hours = hours - 12 
	hours_angel = 360 / 12 * hours 
	minutes_angel = 360 / 60 * minutes
	angel = abs(hours_angel - minutes_angel)
	print('angel ', angel)
	#print('hours_angel ', hours_angel)
	#print('minutes_angel', minutes_angel)	
	#print(hours, minutes)

degrees(1,10)


