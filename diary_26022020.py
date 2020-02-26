Python 3.7.5 (default, Nov 20 2019, 09:21:52) 
[GCC 9.2.1 20191008] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> fhand = open('mbox.txt')
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    fhand = open('mbox.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'mbox.txt'
>>> fhand = open('stuff.txt')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    fhand = open('stuff.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'stuff.txt'
>>> From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
SyntaxError: invalid syntax
>>> stuff = 'Hello\nWorld!'
>>> stuff
'Hello\nWorld!'
>>> print(stuff)
Hello
World!
>>> stuff = 'X\nY'
>>> print(stuff)
X
Y
>>> len(stuff)
3
>>> fhand = open('mbox-short.txt')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    fhand = open('mbox-short.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'mbox-short.txt'
>>> fruit = 'banana'
>>> letter = frit[1]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    letter = frit[1]
NameError: name 'frit' is not defined
>>> letter = fruit[1]
>>> print(letter)
a
>>> letter = fruit[3]
>>> print(letter)
a
>>> letter = fruit[0]
>>> print(letter)
b
>>> letter = fruit[2]
>>> print(letter)
n
>>> fruit = 'banana'
>>> len(fruit)
6
>>> length = len(fruit)
>>> last = fruit[lelgth]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    last = fruit[lelgth]
NameError: name 'lelgth' is not defined
>>> last = fruit[length]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
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
>>> for char in fruit
SyntaxError: invalid syntax
>>> for char in fruit:
	print(char)

	
b
a
n
a
n
a
>>> s = 'Monty Python'
>>> print(s[0:5])
Monty
>>> print(s[6:12])
Python
>>> print(s[1:10])
onty Pyth
>>> fruit = 'banana'
>>> fruit[:3]
'ban'
>>> fruit[3:]
'ana'
>>> fruit[3:3]
''
>>> greeting = 'Hello world!'
>>> greeting[0] = 'J'
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    greeting[0] = 'J'
TypeError: 'str' object does not support item assignment
>>> new_greeting = 'J' + greeting[1:]
>>> print(new_greeting)
Jello world!
>>> word = 'banana'
>>> count = 0
>>> for letter in word:
	if letter == 'a':
		count = count + 1
		print(cunt)
		print(count)

		
Traceback (most recent call last):
  File "<pyshell#56>", line 4, in <module>
    print(cunt)
NameError: name 'cunt' is not defined
>>> print(count)
1
>>> word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)
SyntaxError: multiple statements found while compiling a single statement
>>> word = 'banana'

count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)
SyntaxError: multiple statements found while compiling a single statement
>>> count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)
SyntaxError: multiple statements found while compiling a single statement
>>> 'a' in 'banana;
SyntaxError: EOL while scanning string literal
>>> 'a' in banana'
SyntaxError: EOL while scanning string literal
>>> 'a' in 'banana'
True
>>> 'seed' in banana
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    'seed' in banana
NameError: name 'banana' is not defined
>>> 'seed' in 'banana'
False
>>> if word < 'banana':
	print('Your word,' + word + ', comes before banana.')
	elif word > 'banana':
		
SyntaxError: invalid syntax
>>> if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
	print('Your word,' + word + ', comes after banana.')
else:
	print('All right, bananas.')

	
All right, bananas.
>>> k
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    k
NameError: name 'k' is not defined
>>> stuff = 'Hello world'
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
>>> new_word = word.lower()
>>> print(new_word)
banana
>>> word = 'banana'
>>> index = word.find('a')
>>> priint(index)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    priint(index)
NameError: name 'priint' is not defined
>>> print(index)
1
>>> word.find(na)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    word.find(na)
NameError: name 'na' is not defined
>>> word.find('na')
2
>>> word.find('na', 3)
4
>>> line = '   Here we go  '
>>> line.strip()
'Here we go'
>>> line = 'Have a nice day'
>>> line.starswith('Have')
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    line.starswith('Have')
AttributeError: 'str' object has no attribute 'starswith'
>>> line.startswit('Have')
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    line.startswit('Have')
AttributeError: 'str' object has no attribute 'startswit'
>>> line.startswith('Have')
True
>>> line.startwith('h')
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    line.startwith('h')
AttributeError: 'str' object has no attribute 'startwith'
>>> line.startswith('h')
False
>>> line.lower()
'have a nice day'
>>> line.lower().startswith('h')
True
>>> line.upper()
'HAVE A NICE DAY'
>>> line.upper().startswith('H')
True
>>> data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
>>> atpos = data.find('@')
>>> print(atpos)
21
>>> sppos = data.find(' ', atpos)
>>> print(sppos)
31
>>> host = data[atpos+1:sppos)
SyntaxError: invalid syntax
>>> host = data[atpos+a:sppos]
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    host = data[atpos+a:sppos]
NameError: name 'a' is not defined
>>> host = data[atpos+1:sppos]
>>> print(host)
uct.ac.za
>>> camles = 42
>>> '%d' % camels
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    '%d' % camels
NameError: name 'camels' is not defined
>>> '%d' % camles
'42'
>>> print(host)
uct.ac.za
>>>  'In %d years I have spotted %g %s.' % (3, 0.1, 'camels')
'In 3 years I have spotted 0.1 camels.'
SyntaxError: unexpected indent
>>> 'In %d years I have spotted %g %s.' % (3, 0.1, 'camels')
'In 3 years I have spotted 0.1 camels.'
SyntaxError: multiple statements found while compiling a single statement
>>> 'In %d years I have spotted %g %s.' % (3, 0.1, 'camels')
'In 3 years I have spotted 0.1 camels.'
>>> while True:
	line = input('? ')
	if line[0] == '#':
		continue
	if line == 'done':
		break
	print(line)
print('Done')
SyntaxError: invalid syntax
>>> print('Done!')
Done!
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
  File "<pyshell#137>", line 3, in <module>
    if line[0] == '#':
IndexError: string index out of range
>>> 
>>> 
>>> 
