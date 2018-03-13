with open('test.txt', 'w') as t:
	
	
	one = raw_input('1: ')
    two = raw_input("2: ")
	three = raw_input("3: ")
	
	x = t.write("{} \n{} \n{}".format(one, two, three))
	yy = t.write('x')
	print yy

t.close()




	




