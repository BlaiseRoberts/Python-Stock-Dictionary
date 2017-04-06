stockDict = { 'GM': 'General Motors',
 'CAT':'Caterpillar', 'EK':"Eastman Kodak" }

purchases = [ ( 'GM', 100, '10-sep-2001', 48 ),
 ( 'CAT', 100, '1-apr-1999', 24 ),
 ( 'GM', 200, '1-jul-1998', 56 ) ]

purchase_history = dict()

for item in purchases:
 	for key, value in stockDict.items():
 		purchase_history[key] = list()
 		if item[0] == key:
 			print(value+' was purchased for: $'+str((item[1]*item[3])))

print('==========')

for key, value in purchase_history.items():
	for purchase in purchases:
		if purchase[0] == key:
			value.append(purchase)
	print(key)
	print('-------')
	print(value)
	print()








