Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 0o1, 0o2, 0o377
(1, 2, 255)
>>> 0x01, 0x10, 0xFF
(1, 16, 255)
>>> 0b1, 0b10000, 0b11111111
(1, 16, 255)
>>> 0xFF, (15 * (16 ** 1)) + (15 * (16 ** 0))
(255, 255)
>>> 0xFF, (13 * (14 ** 1)) + (13 * (14 ** 0))
(255, 195)
>>> 15 * 15
225
>>> 0xF
15
>>> 0x2F
47
>>> 0x2F, (2 * (16 ** 1)) + (15 * (16 ** 0))
(47, 47)
>>> (15 * (16 ** 0))
15
>>> (2 * (16 ** 1))
32
>>> 0xF, 0b1111, (1*(2**3) + 1*(2**2) + 1*(2**0))
(15, 15, 13)
>>> Ob1
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    Ob1
NameError: name 'Ob1' is not defined
>>> 0b11
3
>>> 0b1
1
>>> 0b111
7
>>> 0b1111
15
>>> 0xF, 0b1111, (1*(2**3) + 1*(2**2) + 1*(2**1) 1*(2**0))
SyntaxError: invalid syntax
>>> F
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    F
NameError: name 'F' is not defined
>>> 0xFF
255
>>> 0xFFF
4095
>>> 255 * 15
3825
>>> 255 * 255
65025
>>> 255 * 47
11985
>>> 0xF, 0b1111, (1*(2**3) + 1*(2**2) + 1*(2**1) + 1*(2**0))
(15, 15, 15)
>>> oct(64), hex(64), bin(64)
('0o100', '0x40', '0b1000000')
>>> oct
<built-in function oct>
>>> oct(64)
'0o100'
>>> 0o100
64
>>> 64, 0o100, 0x40, 0b10000000
(64, 64, 64, 128)
>>> 64, 0o100, 0x40, 0b1000000
(64, 64, 64, 64)
>>> int('0x40', 16), int('ob1000000', 2)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    int('0x40', 16), int('ob1000000', 2)
ValueError: invalid literal for int() with base 2: 'ob1000000'
>>> int('0x40', 16), int('ob1000000', 2)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    int('0x40', 16), int('ob1000000', 2)
ValueError: invalid literal for int() with base 2: 'ob1000000'
>>> int ('0x40', 16), int('ob1000000', 2)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    int ('0x40', 16), int('ob1000000', 2)
ValueError: invalid literal for int() with base 2: 'ob1000000'
>>> int('64'), int('100', 8), int('40', 16), int('1000000', 2)
(64, 64, 64, 64)
>>> int('0x40', 16), int('ob1000000', 2)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    int('0x40', 16), int('ob1000000', 2)
ValueError: invalid literal for int() with base 2: 'ob1000000'
>>> eval('64'), eval('0o100'), eval('0x40'), eval('ob1000000')
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    eval('64'), eval('0o100'), eval('0x40'), eval('ob1000000')
  File "<string>", line 1, in <module>
NameError: name 'ob1000000' is not defined
>>> ob1000000
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    ob1000000
NameError: name 'ob1000000' is not defined
>>> bin(64)
'0b1000000'
>>> int('64'), int('100', 8), int('40', 16), int('0b1000000', 2)
(64, 64, 64, 64)
>>> int('0x40', 16), int('0b1000000', 2)
(64, 64)
>>> eval('64'), eval('0o100'), eval('0x40'), eval('0b1000000')
(64, 64, 64, 64)
>>> eval
<built-in function eval>
>>> 64
64
>>> 
