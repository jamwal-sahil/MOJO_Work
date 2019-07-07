
a=str(input("Enter the Client MAC Address: "))
x='Y'
while x.upper()=='Y':
	b=int(input(''' Select operation 
	            1) Display SSID 
	            2) Dispaly User Session Duration
	            3) Display Smart Device Type
	            4) Dispaly Local Time Zone
	            5) Privacy ALert! Users Domain Accessed
	            6) Dispalay User Data Transfer From Device (MB) UPLINK
	            7) Display Data Transfer To Device (MB) DOWNLINK   
	            8) Display Various Analytical Graphs   '''))

	if b==1:
		print('Displaying SSIDs corresponding to given MAC Address')
		import function1
		function1.fun(a)
	elif b==2:
		print('Displaying User Session Duration corresponding to given MAC Address')
		import function2
		function2.fun(a)
	elif b==3:
		print('Displaying Smart Device Type corresponding to given MAC Address')
		import function3
		function3.fun(a)
	elif b==4:
		print('Displaying Local Time Zone corresponding to given MAC Address')
		import function4
		function4.fun(a)
	elif b==5:
		print('Displaying Domain Accessed corresponding to given MAC Address')
		import function5
		function5.fun(a)
	elif b==6:
		print('Displaying UPLINK(Bytes) corresponding to given MAC Address')
		import function6
		function6.fun(a)
	elif b==7:
		print('Displaying DOWNLINK(Bytes) corresponding to given MAC Address')
		import function7
		function7.fun(a)
	elif b==8:
		print('Displaying Various Analytical Graphs')
		import function8
		function8.fun()
	else: print('INVALID ENTRY!!!')
	x=str(input('Do you wnat to continiue(Y or N)').upper())
	if(x=='N'):
		break;
