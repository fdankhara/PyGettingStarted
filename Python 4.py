Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 0xFF, (15*(16**1))+(15*(16**0))
(255, 255)
>>> 0x2F, (2*(16*1))+(2*(16**0))
(47, 34)
>>> 0x2F, (2*(16*1))+(15*(16**0))
(47, 47)
>>> 0xF
15
>>> 0b1111
15
>>> 0xF, 0b1111, (1*(2**3)+1*(2**2)+1*(2**1)+1*(2**0))
(15, 15, 15)
>>> oct(64), hex(64), bin(64)
('0o100', '0x40', '0b1000000')
>>> 64, 0o100, 0x40, 0b1000000
(64, 64, 64, 64)
>>> int('64'), int('100' 8), int('40', 16), int('1000000', 2)
SyntaxError: invalid syntax
>>> int('64'), int('100', 8), int('40', 16), int('1000000', 2)
(64, 64, 64, 64)
>>> int('0x40', 16), int('0b1000000', 2)
(64, 64)
>>> eval('64'), eval('0o100'), eval('0x40'), eval('0b1000000')
(64, 64, 64, 64)
>>> '{0:o, {1:x}, {2:b}'. format(64, 64, 64)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    '{0:o, {1:x}, {2:b}'. format(64, 64, 64)
ValueError: unmatched '{' in format spec
>>> '{0:o}, {1:x}, {2:b}'. format(64, 64, 64)
'100, 40, 1000000'
>>> '%o, %x, %x, %X' % (64, 64, 255, 255)
'100, 40, ff, FF'
>>> oct(172), hex(172), bin(172)
('0o254', '0xac', '0b10101100')
>>> 172, 0o254, 0xac, 0b10101100
(172, 172, 172, 172)
>>> int('172'), int('254', 8), int('ac', 16), int('10101100', 2)
(172, 172, 172, 172)
>>> int('0xac', 16), int('0b10101100', 2)
(172, 172)
>>> eval('64'), eval('0o254'), eval('0xac'), eval('0o10101100')
(64, 172, 172, 2130496)
>>> eval('173
     
SyntaxError: EOL while scanning string literal
>>> eval('172')m
SyntaxError: invalid syntax
>>> eval('172'), eval('0o254'), eval('0xac'), eval('0b10101100')
(172, 172, 172, 172)
>>> '{0:o}, {1:x}, {2:b}'. format(172, 172, 172)
'254, ac, 10101100'
>>> format
<built-in function format>
>>> oct
<built-in function oct>
>>> '%o, %x, %x, %X' % (64, 64, 172, 172)
'100, 40, ac, AC'
>>> 0o1, 0o20, 0o377
(1, 16, 255)
>>> 01, 020, 0377
SyntaxError: invalid token
>>> 'Yes'
'Yes'
>>> '!!!'
'!!!'
>>> 0o10
8
>>> 0o16
14
>>> 0o34
28
>>> 0o67
55
>>> 0o18
SyntaxError: invalid syntax
>>> 0o18
SyntaxError: invalid syntax
>>> 0o20
16
>>> 0o19
SyntaxError: invalid syntax
>>> 0o15
13
>>> 0o17
15
>>> 0076
SyntaxError: invalid token
>>> 0o76
62
>>> X = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFF
>>> X
5192296858534827628530496329220095
>>> oct(X)
'0o17777777777777777777777777777777777777'
>>> bin(X)
'0b1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111'
>>> Y = 0o10
>>> Y
8
>>> oct(Y)
'0o10'
>>> hex(Y)
'0x8'
>>> Y = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
>>> Y
24519928653854221733733552434404946937899825954937634815
>>> oct(Y)
'0o17777777777777777777777777777777777777777777777777777777777777'
>>> hex(Y)
'0xffffffffffffffffffffffffffffffffffffffffffffff'
>>> bin(Y)
'0b1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111'
>>> Z =0oFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
SyntaxError: invalid token
>>> Z = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
>>> Z
60383398797144661635864873295812302254670739526663046854019300803929986598274381633378027602842540280663494000492221518396329354078796682120982948022923136698390325231615
>>> octS
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    octS
NameError: name 'octS' is not defined
>>> oct(Z)
'0o77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777'
>>> bin(Z)
'0b111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111'
>>> x = 1
>>> x << 2
4
>>> x | 2
3
>>> x & 1
1
>>> bin(4)
'0b100'
>>> 0001 | 0010
SyntaxError: invalid token
>>> 0001&0001
SyntaxError: invalid token
>>> 0001&0001 = 0001
SyntaxError: invalid token
>>> 1&1
1
>>> 000001&0000000000000001
SyntaxError: invalid token
>>> (0001)&(00000000000000001)
SyntaxError: invalid token
>>> (000000001 & 000000000001)
SyntaxError: invalid token
>>> 
>>> eval('000001')&eval('000000000000001')
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    eval('000001')&eval('000000000000001')
  File "<string>", line 1
    000001
         ^
SyntaxError: invalid token
>>> 1&1
1
>>> 2&2
2
>>> 2&3
2
>>> 9&7
1
>>> X = 0xFF
>>> X
255
>>> oct(X)
'0o377'
>>> bin(X)
'0b11111111'
>>> X ^ 0b10101010
85
>>> bin(X ^ 0b10101010)
'0b1010101'
>>> int('01010101', 2)
85
>>> hex(85)#
'0x55'
>>> X = 0b0001
>>> X << 2
4
>>> bin(X << 2)
'0b100'
>>> bin(X | 0b010)
'0b11'
>>> bin(X & 0b1)
'0b1'
>>> X = 99
>>> bin(X), X.bit_length(), len(bin(X)) - 2
('0b1100011', 7, 7)
>>> bin(256), (256).bit_length(), len(bin(256)) - 2
('0b100000000', 9, 9)
>>> pow
<built-in function pow>
>>> abs
<built-in function abs>
>>> powers
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    powers
NameError: name 'powers' is not defined
>>> absolute values
SyntaxError: invalid syntax
>>> 'pow = powers'
'pow = powers'
>>> 'abs = absolute values'
'abs = absolute values'
>>> import math
>>> math.pi, math.e
(3.141592653589793, 2.718281828459045)
>>> math.sin(2*math.pi/180)
0.03489949670250097
>>> math.sqrt(144), math.sqrt(2)
(12.0, 1.4142135623730951)
>>> pow(2, 4), 2 **4, 2.0 ** 4.0
(16, 16, 16.0)
>>> abs(-42.0), sum((1, 2, 3, 4,))
(42.0, 10)
>>> min(3, 1, 2, 4), max(3, 1, 2, 4)
(1, 4)
>>> math.floor(2.567), math.floor(-2.567)
(2, -3)
>>> math.trunc(2.567), math.trunc(-2.567)
(2, -2)
>>> int(2.567), int(-2.567)
(2, -2)
>>> round(2.567), round(2,467), round(2.567, 2)
(3, 2, 2.57)
>>> '%.1f' % 2.567, '{0:2f}'. format(2.567)
('2.6', '2.567000')
>>> '%.1f' % 2.567, '{0:2f}'. format(2.567)
('2.6', '2.567000')
>>> (1/3.0), round(1/3.0, 2), ('%.2f' % (1/3.0))
(0.3333333333333333, 0.33, '0.33')
>>> import math
>>> math.sqrt
