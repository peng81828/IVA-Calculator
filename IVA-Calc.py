print ("Welcome to Peng81828's Simple Tax & Tip Calculator!")
goodinput = False
while not goodinput:
	try:
		input_var = float(raw_input("Enter the price of your item here: $ "))
		goodinput = True
	except ValueError:
		print ("Invalid Input! Are you sure that's a number?")
iva= 0.115
price= (input_var + input_var * iva)
price= round (price,2)
print ("The price of your item after taxes is $"),price
tipcalc = raw_input("Would you like to give a tip? ").lower()
if tipcalc.startswith('n'):
	print ('Alright!')
if tipcalc.isdigit():
	goodinput = False
	while not goodinput:
		print ("Only letters please!")
		tipcalc = raw_input("Would you like to give a tip? ").lower()
		break
if tipcalc.startswith('y'):
	goodinput = False
	while not goodinput:
		try:
			tipcalc = float(raw_input("What percentage would you like to tip? "))
			goodinput = True
		except ValueError:
			print ("Invalid Input! Are you sure that's a number?")
	tipcalc2 = (tipcalc/100)
	tip= (price + price * tipcalc2)
	tip= round (tip,2)
	print ("Your total with a"), tipcalc,("% tip is $"), tip
print ("Thank you for using Peng81828's Tax & Tip Calculator!")
