Python 3.7.5 (default, Nov 20 2019, 09:21:52) 
[GCC 9.2.1 20191008] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> message = 'And now for something completely different'
>>> n = 17
>>> pi = 3.1415926535897931
>>> print(n)
17
>>> print(pi)
3.141592653589793
>>> type(message)
<class 'str'>
>>> type(n)
<class 'int'>
>>> type(pi)
<class 'float'>
>>> 76trombones = 'big parade'
SyntaxError: invalid syntax
>>> more@ = 100000
SyntaxError: invalid syntax
>>> class = 'Advanced Theoretical zymurgy'
SyntaxError: invalid syntax
>>> print(1)
1
>>> x = 2
>>> print(x)
2
>>> 20+32
52
>>> hour-1
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    hour-1
NameError: name 'hour' is not defined
>>> hour -1
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    hour -1
NameError: name 'hour' is not defined
>>> hour=60
>>> hour-1
59
>>> minute=60
>>> hour*60+minute
3660
>>> hour = 1
>>> hour*60+minute
120
>>> minute/60
1.0
>>> 5**2
25
>>> (5+9)*(15-7)
112
>>> minute=59
>>> minute/60
0.9833333333333333
>>> minute//60
0
>>> 17
17
>>> x
2
>>> x+17
19
>>> 1+1
2
>>> 5
5
>>> x=5
>>> x+1
6
>>> quotient = 7//3
>>> print(quotient)
2
>>> remainder = 7%3
>>> print(remainder)
1
>>> first=10
>>> second=15
>>> print(first+second)
25
>>> first = '100'
>>> scond = '150'
>>> print(first+scond)
100150
>>> first = 'Test'
>>> second = 3
>>> print(first*second)
TestTestTest
>>> inp = input()
some silly stuff
>>> print(inp)
some silly stuff
>>> name = input('What is your name?\n')
What is your name?
Dylan
>>> print(name)
Dylan
>>> prompt = 'What...is the airspeed velocity of an unladen swallow?/n'
>>> speed = input(prompt)
What...is the airspeed velocity of an unladen swallow?/n
>>> prompt = 'What... is the airspeed velocity of an unladen swallow?\n'
>>> speed = input(prompt)
What... is the airspeed velocity of an unladen swallow?
17
>>> int(speed)
17
>>> int(speed)+5
22
>>> speed = input(prompt)
What... is the airspeed velocity of an unladen swallow?
what do you mean, an African or an European swallow?
>>> int(speed)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    int(speed)
ValueError: invalid literal for int() with base 10: 'what do you mean, an African or an European swallow?'
>>> # compute the percentage of the hour that hs elapsed
>>> percentage = (minute *100)/60
>>> percentage = (minute * 100) / 60      #Percentage of an hour
>>> v = 5       #assogn 5 to v
>>> v=5      #velocity in meters/second
>>> a = 35.0
>>> b=12.50
>>> c=a*b
>>> print(c)
437.5
>>> hours = 35.0
>>> rate = 12.50
>>> pay = hours*rate
>>> print(pay)
437.5
>>> x1q3z9afd = 35.0
>>> x1q3z9ahd = 12.5
>>> x1q3p9afd=x1q3z9ahd*x1q3z9afd
>>> print(x1q3p9afd)
437.5
>>> for word in words:
	print(word)

	
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    for word in words:
NameError: name 'words' is not defined
>>> bad name = 5
SyntaxError: invalid syntax
>>> month=09
SyntaxError: invalid token
>>> princpial = 327.68
>>> interest = principle*rate
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    interest = principle*rate
NameError: name 'principle' is not defined
>>> 1.0/2.0*pi
1.5707963267948966
>>> 5==5
True
>>> 5==6
False
>>> type(true)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    type(true)
NameError: name 'true' is not defined
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
>>> x !=y
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    x !=y
NameError: name 'y' is not defined
>>> 17 and True
True
>>> if x>0:
	print('x is positive')

	
x is positive
>>> if x<0:
	pass           # need t handle negative values!

>>> x=3
>>> if x<10:
	print('small')

	
small
>>> x=3
>>> if x<10:
	print('small')
	print('Done')

	
small
Done
>>> if x%2==0:
	print('x is even')
	else:
		
SyntaxError: invalid syntax
>>> if x%2==0:
	print('x is even')
else:
	print ('x is odd')
x=5
SyntaxError: invalid syntax
>>> if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')

    
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    if x < y:
NameError: name 'y' is not defined
>>> if choice == 'a':
    print('Bad guess')
elif choice == 'b':
    print('Good guess')
elif choice == 'c':
    print('Close, but not correct')

    
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    if choice == 'a':
NameError: name 'choice' is not defined
>>> if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')

        
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    if x == y:
NameError: name 'y' is not defined
>>> y=5
>>> if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')

        
x is less than y
>>> if 0 < x:
    if x < 10:
        print('x is a positive single-digit number.')

        
x is a positive single-digit number.
>>> x=0
>>> if 0 < x and x < 10:
    print('x is a positive single-digit number.')

    
>>> 
>>> 
>>> x=2
>>> if 0 < x and x < 10:
    print('x is a positive single-digit number.')

    
x is a positive single-digit number.
>>> prompt = "What is the air velocity of an unladen swallow?\n"
>>> speed = input(prompt)
What is the air velocity of an unladen swallow?
What do you mean, an African or a European swallow?
SyntaxError: multiple statements found while compiling a single statement
>>> int(speed)
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    int(speed)
ValueError: invalid literal for int() with base 10: 'what do you mean, an African or an European swallow?'
>>> inp = input('Enter Fahrenheit Temperature: ')
fahr = float(inp)
cel = (fahr - 32.0) * 5.0 / 9.0
print(cel)
SyntaxError: multiple statements found while compiling a single statement
>>> inp = input('Enter Fahrenheit Temperature: ')
Enter Fahrenheit Temperature: 70
>>> fahr = float(inp)
>>> cel = (fahr - 32.0) * 5.0 / 9.0

>>> print(cel)
21.11111111111111
>>> python fahren.py
SyntaxError: invalid syntax
>>> inp = input('Enter Fahrenheit Temperature:')
Enter Fahrenheit Temperature:-20
>>> try:
	fahr = float(inp)
	cel = (fahr - 32.0)* 5.0/9.0
	print(cel)
except:
	print('Please enter a number')

	
-28.88888888888889
>>> 75
75
>>> 
x=6
>>> x=6
>>> y=2
>>> x >= 2 and (x/y) > 2
True
>>> x=1
>>> y=0
>>> x>=2 and(x/y) >2
False
>>> x=6
>>> y=0
>>> x>=2 and (x/y) >2
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    x>=2 and (x/y) >2
ZeroDivisionError: division by zero
>>> x=1
>>> y=0
>>> x>=2 and y !=0 and (x/y) >2
False
>>> x=6
>>> y=0
>>> x>=2 and y !=0 and (x/y) >2
False
>>> x >= 2 and (x/y) > 2 and y != 0
Traceback (most recent call last):
  File "<pyshell#168>", line 1, in <module>
    x >= 2 and (x/y) > 2 and y != 0
ZeroDivisionError: division by zero
>>> x = 5
>>> y = 6
>>>  y = 6
 
SyntaxError: unexpected indent
>>> 
