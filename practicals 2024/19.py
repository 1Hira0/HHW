print("""Write  a  menu  driven  program  in  Python  to  print  the  given  patterns  (star, 
letters, number).  
*       A        1 
***     A B      22 
*****   A B C    333 
        A B C D  4444""")
while True: 
	c = input("""Menu->
	Please choose the number from the following options of your choice:-
	(1). *       (2).A        (3).1 
	     ***         A B          22 
	     *****       A B C        333 
	                 A B C D      4444
	anything else to exit
	""")
	n = int(input("Enter number of rows: "))
	if '1' in c:
		for i in range(1, 2*n, 2):
			print(i*'*')
	
	if '2' in c:
		for i in range(65, 65+n):
			for j in range(65, i+1):
				print(chr(j), end=' ')
			print()

	if '3' in c:
		for i in range(1, n+1):
			for j in range(1, i+1):
				print(i, end='')
			print()
	if '123'.strip(c):
		break