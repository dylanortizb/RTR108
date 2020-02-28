Python 3.7.5 (default, Nov 20 2019, 09:21:52) 
[GCC 9.2.1 20191008] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> m
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    m
NameError: name 'm' is not defined
>>> largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    print(num)

print("Maximum", largest)
SyntaxError: multiple statements found while compiling a single statement
>>> while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')
SyntaxError: invalid syntax
>>> while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
    print('Done!')

    
> 
Traceback (most recent call last):
  File "<pyshell#5>", line 3, in <module>
    if line[0] == '#':
IndexError: string index out of range
>>> while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
    print('Done!')

    
> 1
1
Done!
> 2
2
Done!
> 3
3
Done!
> 4
4
Done!
> 5
5
Done!
> 6
6
Done!
> 7
7
Done!
> 8
8
Done!
> done
>>> while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
    print('Done!')

    
> v
v
Done!
> d
d
Done!
> csdc
csdc
Done!
> done
>>> while True:
    line = input('> ')
    if line[0] = '#':
        continue
    if line == 'done':
        break
    print(line)
    print('Done!')

    
SyntaxError: invalid syntax
>>> while True:
    line = input('> ')
    if line[0] = #:
        continue
    if line == 'done':
        break
    print(line)
    print('Done!')
    
SyntaxError: invalid syntax
>>> while True:
    line = input('> ')
    if line == '#':
        continue
    if line == 'done':
        break
    print(line)
    print('Done!')

    
> 5
5
Done!
> 6
6
Done!
> 4
4
Done!
> 

Done!
> 

Done!
> 

Done!
> done
>>> largest = None
>>> smallest = None
>>> while True:
	num = input("Enter a Number: ")
	if num == "done" : break
	print(num)
	elif largest is None or num > largest:
		
SyntaxError: invalid syntax
>>> while True:
	num = input("Enter a Number: ")
	try:
		num = int(num)
	Except ValueError:
		
SyntaxError: invalid syntax
>>> while True:
	num = input("Enter a Number: ")
	try:
		num = int(num)
	except ValueError:
		print("Invalid input")
	if num == "done" : break

	
Enter a Number: 5
Enter a Number: 4
Enter a Number: 6
Enter a Number: 54
Enter a Number: d
Invalid input
Enter a Number: done
Invalid input
>>> while True:
	num = input("Enter a Number: ")
	try:
		num = int(num)
	except ValueError:
		print("Invalid input")
	if num == "done" : break
	elif largest is None or num > largest:
		largest = num
	print(largest)

	
Enter a Number: 1
1
Enter a Number: 2
2
Enter a Number: 3
3
Enter a Number: 4
4
Enter a Number: 5
5
Enter a Number: d
Invalid input
Traceback (most recent call last):
  File "<pyshell#36>", line 8, in <module>
    elif largest is None or num > largest:
TypeError: '>' not supported between instances of 'str' and 'int'
>>> done
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    done
NameError: name 'done' is not defined
>>> while True:
	num = input("Enter a Number: ")
	try:
		num = int(num)
	except ValueError:
		print("Invalid input")
	if num == "done" : break
	elif largest is None or num > largest:
		largest = num
	print(largest)

	
Enter a Number: 4
5
Enter a Number: 8
8
Enter a Number: 6
8
Enter a Number: 5
8
Enter a Number: 2
8
Enter a Number: done
Invalid input
>>> while True:
	num = input("Enter a Number: ")
	try:
		num = int(num)
	except ValueError:
		print("Invalid input")
	if num == "done" : break
	for itervar in num:
		if largest is None or itervar > largest:
			largest = itervar
		print(itervar, largest)

		
Enter a Number: 1
Traceback (most recent call last):
  File "<pyshell#45>", line 8, in <module>
    for itervar in num:
TypeError: 'int' object is not iterable
>>> while True:
	num = input("Enter a Number: ")
	try:
		num = int(num)
	except ValueError:
		print("Invalid input")
	if num == "done" : break
	elif largest is None or num > largest:
		largest = num
	print('Largest: 'largest)
	
SyntaxError: invalid syntax
>>> while True:
	num = input("Enter a Number: ")
	try:
		num = int(num)
	except ValueError:
		print("Invalid input")
	if num == "done" : break
	elif largest is None or num > largest:
		largest = num
	print('Largest: ', largest)

	
Enter a Number: 1
Largest:  8
Enter a Number: 2
Largest:  8
Enter a Number: 3
Largest:  8
Enter a Number: 4
Largest:  8
Enter a Number: 5
Largest:  8
Enter a Number: 9
Largest:  9
Enter a Number: 15
Largest:  15
Enter a Number: done
Invalid input
>>> while True:
	num = input("Enter a Number: ")
		print("Invalid input")
	if num == "done" : break
	try:
		num = int(num)
	except ValueError:
	elif largest is None or num > largest:
		largest = num
	print(largest)
	
SyntaxError: unexpected indent
>>> while True:
	num = input("Enter a number: ")
	if num == "done" : break
	try:
		num = int(num)
	except ValueError:
		print("Invalid input")
	elif largest is None or num > largest:
		
SyntaxError: invalid syntax
>>> while True:
	num = input("Enter a number: ")
	if num == "done" : break
	elif largest is None or num > largest:
		num = largest
	try:
		num = int(num)
	except ValueError:
		print("Invalid input")

		
Enter a number: 1
Traceback (most recent call last):
  File "<pyshell#63>", line 4, in <module>
    elif largest is None or num > largest:
TypeError: '>' not supported between instances of 'str' and 'int'
>>> while True:
	num = input("Enter a number: ")
	if num == "done" : break
	elif largest is None or num > largest:
		num = largest
	num = int(num)
	except ValueError:
		print("Invalid input")
		
SyntaxError: invalid syntax
>>> while True:
	num = input("Enter a Number: ")
	try:
		num = int(num)
	except ValueError:
		print("Invalid input")
	if num == "done" : break
	elif largest is None or num > largest:
		largest = num
	print('Largest: ', largest)

	
Enter a Number: 1
Largest:  15
Enter a Number: 2
Largest:  15
Enter a Number: 3
Largest:  15
Enter a Number: 5
Largest:  15
Enter a Number: 25
Largest:  25
Enter a Number: 13
Largest:  25
Enter a Number: done
Invalid input
>>> while True:
	num = input("Enter a Number: ")
	try:
		num = int(num)
	except:
		num == "done"
		print("Invalid input")
	if num == "done" : break
	elif largest is None or num > largest:
		largest = num
	print('Largest: ', largest)

	
Enter a Number: 1
Largest:  25
Enter a Number: 5
Largest:  25
Enter a Number: 6
Largest:  25
Enter a Number: 8
Largest:  25
Enter a Number: d
False
Invalid input
Traceback (most recent call last):
  File "<pyshell#68>", line 9, in <module>
    elif largest is None or num > largest:
TypeError: '>' not supported between instances of 'str' and 'int'
>>> while True:
	num = input("Enter a Number: ")
	try:
		num = int(num)
	except:
		num == "done"
		print("Invalid input")
	if num == "done" : break
	elif largest is None or num > largest:
		largest = num
	print('Largest: ', largest)

	
Enter a Number: done
True
Invalid input
>>> while True:
	num = input("Enter a Number: ")
	try:
		num = int(num)
	except ValueError:
		num == "done"
		print("Invalid input")
	if num == "done" : break
	elif largest is None or num > largest:
		largest = num
	print('Largest: ', largest)

	
Enter a Number: 5
Largest:  25
Enter a Number: 6
Largest:  25
Enter a Number: done
True
Invalid input
>>> while True:
	num = input("Enter a Number: ")
	try:
		num = int(num)
	except ValueError:
		num == "done"
		print("Invalid input")
	if num == "done" : break
	elif largest is None or num > largest:
		largest = num
	print('Largest: ', largest)

Enter a Number: 
False
Invalid input
Traceback (most recent call last):
  File "<pyshell#73>", line 9, in <module>
    elif largest is None or num > largest:
TypeError: '>' not supported between instances of 'str' and 'int'
>>> while True:
	num = input("Enter a Number: ")
	try:
		num = int(num)
	except ValueError:
		num == "done"
		print("Invalid input")
	if num == "done" : break
	elif largest is None or num > largest:
		largest = num
	print('Largest: ', largest)

Enter a Number: d
False
Invalid input
Traceback (most recent call last):
  File "<pyshell#74>", line 9, in <module>
    elif largest is None or num > largest:
TypeError: '>' not supported between instances of 'str' and 'int'
>>> while True:
	num = input("Enter a Number: ")
	try:
		num = int(num)
	except ValueError:
		num == "done"
		print("Invalid input")
	if num == "done" : break
	elif largest is None or num > largest:
		largest = num
	print('Largest: ', largest)
        elif smallest is None or num < smallest:
		
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> while True:
	num = input("Enter a Number: ")
	try:
		num = int(num)
	except ValueError:
		num == "done"
		print("Invalid input")
	if num == "done" : break
	elif largest is None or num > largest:
		largest = num
	print('Largest: ', largest)
	elif smalles is None or num < smallest:
		
SyntaxError: invalid syntax
>>> while True:
	num = input("Enter a Number: ")
	try:
		num = int(num)
	except ValueError:
		num == "done"
		print("Invalid input")
	if num == "done" : break
	elif largest is None or num > largest:
		largest = num
	elif smallest is None or num < smallest:
		smallest = num
	print('Largest: ', largest)
	print('Smallest: ', smallest)

	
Enter a Number: 0
Largest:  25
Smallest:  0
Enter a Number: 5
Largest:  25
Smallest:  0
Enter a Number: 5
Largest:  25
Smallest:  0
Enter a Number: done
True
Invalid input
>>> while True:
	num = input("Enter a Number: ")
	try:
		num = int(num)
	except ValueError:
		num == "done"
		print("Invalid input")
	if num == "done" : break
	elif largest is None or num > largest:
		largest = num
	elif smallest is None or num < smallest:
		smallest = num
	print('Largest: ', largest)
	print('Smallest: ', smallest)
