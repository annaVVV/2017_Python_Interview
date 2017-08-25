# Formatted Output

## Keyword parameter "sep" of the print function:
```
>>> q = 459
>>> p = 0.098
>>> print(q, p, p * q)
459 0.098 44.982
>>> print(q, p, p * q, sep=",")
459,0.098,44.982
>>> print(q, p, p * q, sep=" :-) ")
459 :-) 0.098 :-) 44.982
```

## Concatenation operator:
```
>>> print(str(q) + " " + str(p) + " " + str(p * q))
459 0.098 44.982
```

```
Conversion	Meaning
d	Signed integer decimal.
i	Signed integer decimal.
o	Unsigned octal.
u	Obsolete and equivalent to 'd', i.e. signed integer decimal.
x	Unsigned hexadecimal (lowercase).
X	Unsigned hexadecimal (uppercase).
e	Floating point exponential format (lowercase).
E	Floating point exponential format (uppercase).
f	Floating point decimal format.
F	Floating point decimal format.
g	Same as "e" if exponent is greater than -4 or less than precision, "f" otherwise.
G	Same as "E" if exponent is greater than -4 or less than precision, "F" otherwise.
c	Single character (accepts integer or single character string).
r	String (converts any python object using repr()).
s	String (converts any python object using str()).
%	No argument is converted, results in a "%" character in the result.
```

Examples show some example cases of the conversion rules from the table above: 
```
>>> print("%10.3e"% (356.08977))
 3.561e+02
>>> print("%10.3E"% (356.08977))
 3.561E+02
>>> print("%10o"% (25))
        31
>>> print("%10.3o"% (25))
       031
>>> print("%10.5o"% (25))
     00031
>>> print("%5x"% (47))
   2f
>>> print("%5.4x"% (47))
 002f
>>> print("%5.4X"% (47))
 002F
>>> print("Only one percentage sign: %% " % ())
Only one percentage sign: % 
```


Flag	Meaning
```
#	Used with o, x or X specifiers the value is preceded with 0, 0o, 0O, 0x or 0X respectively.
0	The conversion result will be zero padded for numeric values.
-	The converted value is left adjusted
 	If no sign (minus sign e.g.) is going to be written, a blank space is inserted before the value.
+	A sign character ("+" or "-") will precede the conversion (overrides a "space" flag).
```

Examples: 
```
>>> print("%#5X"% (47))
 0X2F
>>> print("%5X"% (47))
   2F
>>> print("%#5.4X"% (47))
0X002F
>>> print("%#5o"% (25))
 0o31
>>> print("%+d"% (42))
+42
>>> print("% d"% (42))
 42
>>> print("%+2d"% (42))
+42
>>> print("% 2d"% (42))
 42
>>> print("%2d"% (42))
42
```
Used the string modulo functionality of Python in a two layer approach as well,
i.e. first create a formatted string, which will be assigned to a variable 
and this variable is passed to the print function: 
```
>>> s = "Price: $ %8.2f"% (356.08977)
>>> print(s)
Price: $   356.09
```

## Positional parameters
```
>>> "First argument: {0}, second one: {1}".format(47,11) 
'First argument: 47, second one: 11'
>>> "Second argument: {1}, first one: {0}".format(47,11) 
'Second argument: 11, first one: 47'
>>> "Second argument: {1:3d}, first one: {0:7.2f}".format(47.42,11) 
'Second argument:  11, first one:   47.42'
>>> "First argument: {}, second one: {}".format(47,11) 
'First argument: 47, second one: 11'
>>> # arguments can be used more than once:
... 
>>> "various precisions: {0:6.2f} or {0:6.3f}".format(1.4148) 
'various precisions:   1.41 or  1.415'
``` 

In the following example we demonstrate how keyword parameters can be used with the format method:
```
>>> "Art: {a:5d},  Price: {p:8.2f}".format(a=453, p=59.058)
'Art:   453,  Price:    59.06'
>>> "{0:<20s} {1:6.2f}".format('Spam & Eggs:', 6.99)
'Spam & Eggs:           6.99'
>>> "{0:>20s} {1:6.2f}".format('Spam & Eggs:', 6.99)
'        Spam & Eggs:   6.99'
```


