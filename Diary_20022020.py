Python 3.7.5 (default, Nov 20 2019, 09:21:52) 
[GCC 9.2.1 20191008] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> while True:
	line = input('> ')
	if line == 'done' :
		break
	print(line)
	print('Done!')

	
> 

Done!
> 

Done!
> 

Done!
> 

Done!
> 

Done!
> 

Done!
> 

Done!
> 

Done!
> done
>>> hello there
SyntaxError: invalid syntax
>>> while True:
	line = input('> ')
	if line == 'done' :
		break
	print(line)
	print('Done!')

	
> hello there
hello there
Done!
> finished
finished
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

	
> 
Traceback (most recent call last):
  File "<pyshell#18>", line 3, in <module>
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

> 5
5
Done!
> 6
6
Done!
> dmasda
dmasda
Done!
> ohhhh yeahhh
ohhhh yeahhh
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

> 
Traceback (most recent call last):
  File "<pyshell#20>", line 3, in <module>
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

> hello there
hello there
Done!
> # don't rint this
> #jlsnfew
> done
>>> friends = ['Joseph', 'Glenn', 'Sally']
>>> for friend in friends:
	print('Happy New y
	      
SyntaxError: EOL while scanning string literal
>>> friends = ['Joseph', 'Glenn', 'Sally']
>>> for friend in friends:
	print('Happy New Year:', friend)
	print('Done!')

	
Happy New Year: Joseph
Done!
Happy New Year: Glenn
Done!
Happy New Year: Sally
Done!
>>> count = 0
>>> for intervar in [3, 41, 12, 9, 74, 15]:
	count = count + 1
	print('Count:  ', count)

	
Count:   1
Count:   2
Count:   3
Count:   4
Count:   5
Count:   6
>>> total =
SyntaxError: invalid syntax
>>> total = 0
>>> for intervar in [3, 41, 12, 9, 74, 15]:
	total = total + intervar
	print('Total:  ', total)

	
Total:   3
Total:   44
Total:   56
Total:   65
Total:   139
Total:   154
>>> Before: None
>>> Loop: 3 3
SyntaxError: invalid syntax
>>> largest = None
>>> print('Before:' largest)
SyntaxError: invalid syntax
>>> largest = None
>>> print('Before:', largest)
Before: None
>>> for itervar in [3, 41, 12, 9, 74, 15]:
	if largest is None or itervar > largest :
		largest = itervar
		print('Loop:', itervar, largest)
		print('Largest:', largest)

		
Loop: 3 3
Largest: 3
Loop: 41 41
Largest: 41
Loop: 74 74
Largest: 74
>>> largest = None
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        largest = itervar
    print('Loop:', itervar, largest)
print('Largest:', largest)
SyntaxError: multiple statements found while compiling a single statement
>>> largest = None
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        largest = itervar
    print('Loop:', itervar, largest)
print('Largest:', largest)
SyntaxError: multiple statements found while compiling a single statement
>>> largest = None
>>> print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        largest = itervar
    print('Loop:', itervar, largest)
print('Largest:', largest)
SyntaxError: multiple statements found while compiling a single statement
>>> largest = None
>>> print('Before:', largest)
Before: None
>>> for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        largest = itervar
    print('Loop:', itervar, largest)
print('Largest:', largest)
SyntaxError: invalid syntax
>>> smallest = None
>>> print('Before:', smallest)
Before: None
>>> for itervar in [3, 41, 12, 9, 74, 15]:
	if smallest is None or itervar < smallest:
		smallest = itervar
	print('Loop:', itervar, smallest)
print('Smallest:', smallest)
SyntaxError: invalid syntax
>>> for itervar in [3, 41, 12, 9, 74, 15]:
	if smallest is None or itervar < smallest:
		smallest = itervar
	print('Loop:', itervar, smallest)
	print('Smallest:', smallest)

	
Loop: 3 3
Smallest: 3
Loop: 41 3
Smallest: 3
Loop: 12 3
Smallest: 3
Loop: 9 3
Smallest: 3
Loop: 74 3
Smallest: 3
Loop: 15 3
Smallest: 3
>>> def min(values):
	smallet = None
	for value in values:
		if smallest is None or value < smallest:
			smallest = value
		return smallest

	
>>> fruit = 'banana'
>>> letter = fruit[1]
>>> print(letter)
a
>>> letter = fruit[0]
>>> print(letter)
b
>>> print(letter)
b
>>> letter = fruit[1.5]
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    letter = fruit[1.5]
TypeError: string indices must be integers
>>> fruit = 'banana'
>>> len(fruit)
6
>>> length = len(fruit)
>>> last = fruit[length]
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    last = fruit[length]
IndexError: string index out of range
>>> last = fruit[length-1]
>>> print(last)
a
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index + 1

	
b
a
n
a
n
a
>>> for char in fruit:
	print(char)

	
b
a
n
a
n
a
>>> name = Dylan
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    name = Dylan
NameError: name 'Dylan' is not defined
>>> def name = dylan
SyntaxError: invalid syntax
>>> s = 'Monty Python'
>>> print(s[0:5])
Monty
>>> print(s[6:12])
Python
>>> fruit = banana
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    fruit = banana
NameError: name 'banana' is not defined
>>> fruit[:3]
'ban'
>>> fruit[3:]
'ana'
>>> fruit[:5]
'banan'
>>> fruit = 'banana'
>>> fruit[3:3]
''
>>> name = 'Dylan'
>>> for char in name:
	print(char)

	
D
y
l
a
n
>>> greeting = 'Hello, world!'
>>> greeting[0] = 'J'
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    greeting[0] = 'J'
TypeError: 'str' object does not support item assignment
>>> greeting = 'Hello, world!'
>>> new_greeting = 'J' + greeting[1:]
>>> print(new_greeting)
Jello, world!
>>> word = 'banana'
>>> count = 0
>>> for letter in word:
	in letter == 'a':
		
SyntaxError: invalid syntax
>>> word = 'banana'
>>> count = 0
>>> for letter in word:
	if letter == 'a':
		count = count + 1
	print(count)

	
0
1
1
2
2
3
>>> 'a' in 'banana'
True
>>> 'seed' in 'banana'
False
>>> if word == 'banana':
	print('All right, bananas.')

	
All right, bananas.
>>> if word < 'banana':
	print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
	print('Your word,' + word + ', comes after banana,')
else:
	print('All right, bananas.')

	
All right, bananas.
>>> stuff = 'Hellos world'
>>> type(stuff)
<class 'str'>
>>> dir(stuff)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(str.capitalize)
Help on method_descriptor:

capitalize(self, /)
    Return a capitalized version of the string.
    
    More specifically, make the first character have upper case and the rest lower
    case.

>>> word = 'banana'
>>> new_word = word.upper()
>>> print(new_word)
BANANA
>>> word = 'banana'
>>> index = word.find('a')
>>> print(index)
1
>>> word.find('na')
2
>>> word.find('na;, 3)
	  
SyntaxError: EOL while scanning string literal
>>> word.find('na', 3)
4
>>> line = '  Here we go   '
>>> line.strip()
'Here we go'
>>> line = 'Have a nice day'
>>> line.startswith('h')
False
>>> line.lower()
'have a nice day'
>>> ine.lower().startswith('h')
Traceback (most recent call last):
  File "<pyshell#162>", line 1, in <module>
    ine.lower().startswith('h')
NameError: name 'ine' is not defined
>>> line.lower().startswith('h')
True
>>> data = 'From stephen.marquar@uct.ac.za Sat Jan 5 09:14:16 2008'
>>> atpos = data.find('@')
>>> print(atpos)
20
>>> sppos = data.find(' ', atpos)
>>> print(sppos)
30
>>> hot = data[atpos+1:sppos]
>>> print(hot)
uct.ac.za
>>> camels = 42
>>> '%d' % camels
'42'
>>> camels = 42
>>> 'I have spotted %d camels.' % camels
'I have spotted 42 camels.'
>>> 'In %d years I have spotted %g %s.' % (3, 0.1, 'camels')
'In 3 years I have spotted 0.1 camels.'
>>> '%d %d %d' % (1, 2)
Traceback (most recent call last):
  File "<pyshell#176>", line 1, in <module>
    '%d %d %d' % (1, 2)
TypeError: not enough arguments for format string
>>> '%d' % 'dollars'
Traceback (most recent call last):
  File "<pyshell#177>", line 1, in <module>
    '%d' % 'dollars'
TypeError: %d format: a number is required, not str
>>> while True:
	line = input('> ')
	if line[0] == '#':
		continue
	if line == 'done':
		break
	print(line)
	print('Done!')

	
> hello there
hello there
Done!
> # don't print
> #njdasndjlasndas
> #kasdmkasdm
> hi
hi
Done!
> khorosho
khorosho
Done!
> 
Traceback (most recent call last):
  File "<pyshell#186>", line 3, in <module>
    if line[0] == '#':
IndexError: string index out of range
>>> if line.starswith('#'):

	continue
SyntaxError: 'continue' not properly in loop
>>> if len(line) > 0 and line[0] == '#':
