"""
Data driven Test Cases using the unittest.TestSuite class, 
which will allow you to dynamically construct a set of unittest.TestCase instances 
which will get run separately. 
The unittest.TestCase subclass should define just one test method, 
with the class accepting a construction parameter passing in the value 
to test against for that particular instance
"""
import unittest, re

# Implement method to verify if IP4 address is valid:
# valid values: 0-255.1-255.1-255.1-255
# Leading 0 >> False (0), example: 123.01.123.123

def validate_ip4_address(address):
    #print 'add:',address
    ppp = "^([0]|[1-9]\d?|[1]\d?\d?|2[1-4]\d|25[0-5])(\.([1-9]\d?|[1]\d?\d?|2[1-4]\d|25[0-5])){3}"
    match = re.search(ppp, address)
    if match:
        #print  match.group(), True
        return 1
    else:
        #print address, False
        return 0

class DataTestCase(unittest.TestCase):
    def __init__(self, number):
        unittest.TestCase.__init__(self, methodName='test_ip4_address')
        self.number = number

    def test_ip4_address(self):
        #print self.number[0], self.number[1]
        self.assertEqual(validate_ip4_address(self.number[0]), self.number[1])

    def shortDescription(self):
        # We need to distinguish between instances of this test case.
        return 'DataTestCase for IP address:', self.number[0], 'Expected result', self.number[1]

def get_test_data_suite():
    data = [('0.1.1.1', 1),('255.255.255.255', 1),('10.25.30.99', 1),('0.9.9.9', 1),('1.1.1.1', 1),
            ('9.1.1.1', 1),('100.100.100.100', 1),('255.1.1.1', 1),('0.25.254.1', 1),('0.254.254.1', 1),
            ('-1.101.222.234', 0),('122.0.111.123', 0),('256.123.155.10', 0),('0.001.255.1', 0),('00.19.11.111', 0),
            ('122.0.111.123', 0),('a.1.1.1', 0),('100..100.100', 0),('255.1.1', 0),('', 0)]
    print 'data:',data
    return unittest.TestSuite([DataTestCase(n) for n in data])

if __name__ == '__main__':
    testRunner = unittest.TextTestRunner()
    testRunner.run(get_test_data_suite())
    validate_ip4_address('0.1.1.1')


# Unix commands: sed, awk to  remove empty lines from file 

# sed -i '/^$/d' file.txt
# The -i means it will edit the file in-place

# sed '/^$/d' file.txt
# ^$ is a regular expression matching only a blank line, a line start followed by a line end.
# d is the sed command to delete a line. 
"""
https://stackoverflow.com/questions/14570489/how-to-remove-blank-lines-from-a-unix-file
awk 'NF' filename
awk 'NF > 0' filename
sed -i '/^$/d' filename
awk '!/^$/' filename
awk '/./' filename
The NF also removes lines containing only blanks or tabs, the regex /^$/ does not.

Use grep to match any line that has nothing between the start anchor (^) and the end anchor ($):
grep -v '^$' infile.txt > outfile.txt
If you want to remove lines with only whitespace, you can still use grep. 
Using Perl regular expressions in this example, but here are other ways:
grep -P -v '^\s*$' infile.txt > outfile.txt
or, without Perl regular expressions:

grep -v '^[[:space:]]*$' infile.txt > outfile.txt
"""

# SQL find second max salary and employee ID
"""
Query 1.1 Find the Employee with the Highest Salary

SELECT EmployeeId, Salary FROM
(Select EmployeeId, Salary, ROW_NUMBER() OVER(Order by Salary Desc) as Salary_Order from Employee) DT
WHERE DT. Salary_Order = 1 ;

Second Highest salary and EmployeeId

select EmployeeId, Salary FROM Employee 
where Salary = (
SELECT MAX(salary) FROM Employee WHERE Salary NOT IN ( SELECT Max(Salary) FROM Employee));

SELECT Id, Salary FROM Employee e WHERE 2=(SELECT COUNT(DISTINCT Salary) FROM Employee p WHERE e.Salary<=p.Salary)
MySQL:
SELECT TOP 1 Salary FROM ( SELECT TOP 2 Salary FROM Employee ORDER BY Salary DESC) AS MyTable ORDER BY Salary ASC


"""





