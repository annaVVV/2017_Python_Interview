import re

"""
Description
"(([01]?\d?\d|2[1-4]\d|25[0-4])\.){3}([01]?\d?\d|2[1-4]\d|25[0-4])"
^		#start of the line
 (		#  start of group #1
   [01]?\d\d? #    Can be one or two digits. If three digits appear, it must start either 0 or 1
		#    e.g ([0-9], [0-9][0-9],[0-1][0-9][0-9])
    |		#    ...or
   2[0-4]\d	#    start with 2, follow by 0-4 and end with any digit (2[0-4][0-9])
    |           #    ...or
   25[0-5]      #    start with 2, follow by 5 and ends with 0-5 (25[0-5])
 )		#  end of group #2
  \.            #  follow by a dot "."
{3}            # repeat with 3 times (3x)
$		#end of the line
"""


"""
Validate ip address with regular expression
1.1.1.1, 255.255.255.255,192.168.1.1
10.10.1.1, 132.254.111.10, 26.10.2.10,
127.0.0.1
"""

IPADDRESS_PATTERN = "(([01]?\d?\d|2[1-4]\d|25[0-4])\.){3}([01]?\d?\d|2[1-4]\d|25[0-4])"

# without validation
# [01]?\d?\d


str = "bal ghjhjk  55.254.111.99 "
match = re.search(IPADDRESS_PATTERN, str)
if match:
    print  match.group()

