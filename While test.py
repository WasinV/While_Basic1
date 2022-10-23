# while1.py

money = 10000000
transfer = 10000000

print('Check:', money < transfer)

while money < transfer:
	print('Please fill out the correct value')
	transer = float(input('New transfer:  '))
	if transfer > 1000000:		
		print('Manager approval requriment')
		break

print('Able to transer when having manager approval requriment')

